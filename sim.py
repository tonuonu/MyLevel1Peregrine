#!/usr/bin/env python3
"""Peregrine ascent simulator and CATS replay/calibration viewer.

Passive 6-DOF ascent model only. No active-control or actuator commands.
"""
from __future__ import annotations
import base64, math, struct
from dataclasses import dataclass
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation

G=9.80665
REC_ID_MASK=0x0F
RECORDS={0x010:("IMU",12,"<6h"),0x020:("BARO",8,"<2i"),0x040:("FLIGHT_INFO",12,"<3f"),0x080:("ORIENTATION_INFO",8,"<4h"),0x100:("FILTERED_DATA_INFO",8,"<2f"),0x200:("FLIGHT_STATE",4,"<I"),0x400:("EVENT_INFO",8,None),0x800:("ERROR_INFO",4,"<I"),0x1000:("GNSS_INFO",9,"<2fB"),0x2000:("VOLTAGE_INFO",2,"<H")}
FSM={0:"INVALID",1:"CALIBRATING",2:"READY",3:"THRUSTING",4:"COASTING",5:"DROGUE",6:"MAIN",7:"TOUCHDOWN"}

@dataclass(frozen=True)
class Motor:
    name:str; curve:np.ndarray; total_mass:float; prop_mass:float; length:float
    @property
    def case_mass(self): return self.total_mass-self.prop_mass
    @property
    def burn_time(self): return float(self.curve[-1,0])
    def thrust(self,t): return float(np.interp(t,self.curve[:,0],self.curve[:,1],left=0,right=0))
    def remaining_prop(self,t):
        # Propellant depletion proportional to delivered impulse.
        tt=self.curve[:,0]; ff=self.curve[:,1]
        cum=np.r_[0,cumulative_trapezoid(ff,tt)]; total=max(cum[-1],1e-9)
        delivered=float(np.interp(t,tt,cum,left=0,right=total))
        return self.prop_mass*max(0,1-delivered/total)

J350=Motor("AeroTech J350W (1.9 s curve)",np.array([[0,0],[.1,598.37],[.2,571.28],[.3,562.33],[.4,545.92],[.5,517.35],[.6,506.91],[.7,460.65],[.8,448.72],[1.0,400.75],[1.2,345.32],[1.4,269.23],[1.5,155.39],[1.7,44.76],[1.8,17.95],[1.9,0]],float),.650,.375,.340)
J420=Motor("AeroTech J420R",np.array([[0,0],[.03,61.08],[.10,563.47],[.16,525.28],[.22,521.24],[.29,527.37],[.35,537.09],[.42,535.14],[.48,534.62],[.55,530.25],[.61,526.45],[.67,517.2],[.74,510.28],[.80,500.89],[.87,479.45],[.93,460.68],[1,438.59],[1.06,409.65],[1.12,383.45],[1.19,361.02],[1.25,339.74],[1.32,319.19],[1.38,296.71],[1.45,195.19],[1.51,61.98],[1.58,7.22],[1.61,0]],float),.659,.381,.337)
MOTORS={m.name:m for m in (J350,J420)}

@dataclass
class Vehicle:
    ignition_mass:float=3.0; diameter:float=.1016; cp:float=1.379; ignition_cg:float=1.25
    motor_cg:float=1.58; Ixx:float=.010; Iyy:float=.55; cd:float=.65; cd2:float=.20; cna:float=15.56; cmq:float=12
    rho:float=1.225; rail_len:float=.9144; rail_tilt_deg:float=0; wind_e:float=0; wind_n:float=0
    @property
    def area(self): return math.pi*self.diameter**2/4

@dataclass
class Result:
    t:np.ndarray; y:np.ndarray; tilt:np.ndarray; heading:np.ndarray; qdyn:np.ndarray; rail_exit_t:float
    @property
    def altitude(self): return self.y[2]
    @property
    def speed(self): return np.linalg.norm(self.y[3:6].T,axis=1)
    @property
    def horizontal(self): return np.linalg.norm(self.y[:2].T,axis=1)
    @property
    def rates_deg_s(self): return np.rad2deg(self.y[10:13].T)

def q_to_R(q):
    w,x,y,z=q/np.linalg.norm(q)
    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],[2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],[2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])
def q_dot(q,w):
    p,qy,r=w; return .5*np.array([[0,-p,-qy,-r],[p,0,r,-qy],[qy,-r,0,p],[r,qy,-p,0]])@q

def mass_cg(t,v,motor):
    prop=motor.remaining_prop(t); motor_mass=motor.case_mass+prop
    dry=v.ignition_mass-motor.total_mass
    if dry<=0: raise ValueError("Ignition mass must exceed motor mass")
    # Derive dry CG so ignition configuration exactly matches user-entered CG.
    dry_cg=(v.ignition_mass*v.ignition_cg-motor.total_mass*v.motor_cg)/dry
    mass=dry+motor_mass; cg=(dry*dry_cg+motor_mass*v.motor_cg)/mass
    return mass,cg

def rail_phase(v,motor):
    tilt=math.radians(v.rail_tilt_deg); rail=np.array([math.sin(tilt),0,math.cos(tilt)])
    def f(t,x):
        s,sd=x; mass,_=mass_cg(t,v,motor); Vrel=sd*rail-np.array([v.wind_e,v.wind_n,0]); V=np.linalg.norm(Vrel)
        cd_eff=max(0.01,v.cd+v.cd2*(V/200.0)**2)
        drag_vector=-.5*v.rho*V*v.area*cd_eff*Vrel
        along=motor.thrust(t)+float(np.dot(drag_vector,rail))-mass*G*rail[2]
        if s <= 0 and sd <= 0 and along <= 0:
            return [0.,0.]
        return [sd,along/mass]
    def exit_event(t,x): return x[0]-v.rail_len
    exit_event.terminal=True; exit_event.direction=1
    sol=solve_ivp(f,(0,5),[0,0],events=exit_event,max_step=.001,rtol=1e-8,atol=1e-10)
    if len(sol.t_events[0])==0: raise ValueError("Rocket does not leave the rail with these inputs")
    te=float(sol.t_events[0][0]); se,ve=sol.y_events[0][0]
    quat=Rotation.from_euler("y",tilt).as_quat()[[3,0,1,2]]
    y=np.r_[rail*se,rail*ve,quat,np.zeros(3)]
    return te,y

def free_dynamics(t,y,v,motor):
    pos=y[:3]; vel=y[3:6]; quat=y[6:10]/np.linalg.norm(y[6:10]); omega=y[10:13]; R=q_to_R(quat)
    mass,cg=mass_cg(t,v,motor); wind=np.array([v.wind_e,v.wind_n,0]); air_b=R.T@(vel-wind); V=np.linalg.norm(air_b)
    force_b=np.array([0.,0.,motor.thrust(t)]); moment_b=np.zeros(3)
    if V>.2:
        qdyn=.5*v.rho*V*V; cd_eff=max(0.01,v.cd+v.cd2*(V/200.0)**2)
        force_b += -qdyn*v.area*cd_eff*air_b/V
        # Normal force opposes body-frame lateral relative velocity.
        # Bounded engineering approximation, matching CNa at small angle.
        # The previous v_lateral/v_axial formula diverged near broadside flow.
        lateral=float(np.linalg.norm(air_b[:2]))
        alpha=math.atan2(lateral,abs(float(air_b[2])))
        direction=air_b[:2]/max(lateral,1e-12)
        cn=v.cna*math.sin(alpha)*math.cos(alpha)
        normal=np.r_[-qdyn*v.area*cn*direction,0.]
        force_b+=normal
        moment_b+=np.cross(np.array([0.,0.,cg-v.cp]),normal)
        # Pitch/yaw moment: q*S*d*Cmq*(omega*d/(2V)), in N m.
        moment_b[0]+=-qdyn*v.area*v.diameter*v.cmq*(omega[0]*v.diameter/(2*V))
        moment_b[1]+=-qdyn*v.area*v.diameter*v.cmq*(omega[1]*v.diameter/(2*V))
        # Roll damping is not identified; no invented roll derivative.
    acceleration=R@force_b/mass+np.array([0,0,-G])
    inertia=np.diag([v.Iyy,v.Iyy,v.Ixx]); omega_dot=np.linalg.solve(inertia,moment_b-np.cross(omega,inertia@omega))
    return np.r_[vel,acceleration,q_dot(quat,omega),omega_dot]

def simulate(v,motor,max_step=.005):
    te,y_exit=rail_phase(v,motor)
    def apogee(t,y): return y[5]
    apogee.terminal=True; apogee.direction=-1
    free=solve_ivp(lambda t,y:free_dynamics(t,y,v,motor),(te,40),y_exit,events=apogee,max_step=max_step,rtol=2e-7,atol=1e-9)
    # Add launch state for complete plotting.
    t=np.r_[0,te,free.t[1:]]; y=np.column_stack([np.r_[np.zeros(6),y_exit[6:10],np.zeros(3)],y_exit,free.y[:,1:]])
    q=y[6:10].T; q/=np.linalg.norm(q,axis=1)[:,None]; body_z=np.array([q_to_R(x)[:,2] for x in q])
    tilt=np.rad2deg(np.arccos(np.clip(body_z[:,2],-1,1))); heading=np.rad2deg(np.unwrap(np.arctan2(body_z[:,1],body_z[:,0])))
    heading[np.linalg.norm(body_z[:,:2],axis=1)<1e-6]=np.nan
    air=y[3:6].T-np.array([v.wind_e,v.wind_n,0]); qdyn=.5*v.rho*np.sum(air*air,axis=1)
    return Result(t,y,tilt,heading,qdyn,te)

def parse_cfl(data):
    null=data.index(b"\0"); version=data[:null].decode("ascii",errors="replace"); pos=null+1; rec={n:[] for n,_,_ in RECORDS.values()}
    while pos+8<=len(data):
        ts,raw=struct.unpack_from("<II",data,pos); typ=raw&~REC_ID_MASK; sid=raw&REC_ID_MASK
        if typ not in RECORDS: break
        name,n,fmt=RECORDS[typ]; a=pos+8; b=a+n
        if b>len(data): break
        vals=struct.unpack_from(fmt,data,a) if fmt else tuple(data[a:b]); rec[name].append((ts,sid)+vals); pos=b
    return version,rec,pos,len(data)
def decode_upload(u):
    data=u.getvalue()
    if u.name.lower().endswith(("txt","b64")):
        try:data=base64.b64decode(b"".join(data.split()),validate=True)
        except Exception:pass
    return data
def cats_frames(rec):
    states={}
    for ts,_,s in rec["FLIGHT_STATE"]:states.setdefault(FSM.get(s,str(s)),ts)
    lift=states.get("THRUSTING",rec["FLIGHT_INFO"][0][0])
    fi=pd.DataFrame(rec["FLIGHT_INFO"],columns=["ts","sid","height","velocity","accel"]);fi["t"]=(fi.ts-lift)/1000
    imu=pd.DataFrame(rec["IMU"],columns=["ts","sid","axr","ayr","azr","gxr","gyr","gzr"]);imu["t"]=(imu.ts-lift)/1000
    for a,raw in zip("xyz",("axr","ayr","azr")): imu[f"a{a}"]=imu[raw]*G/1024
    imu[["gx","gy","gz"]]=imu[["gxr","gyr","gzr"]]*.07
    ori=pd.DataFrame(rec["ORIENTATION_INFO"],columns=["ts","sid","qw","qx","qy","qz"]);ori["t"]=(ori.ts-lift)/1000
    q=ori[["qw","qx","qy","qz"]].to_numpy(float);q/=np.linalg.norm(q,axis=1)[:,None]
    bz=np.array([q_to_R(x)[:,2] for x in q]);ori["tilt"]=np.rad2deg(np.arccos(np.clip(bz[:,2],-1,1)));ori["heading"]=np.rad2deg(np.unwrap(np.arctan2(bz[:,1],bz[:,0])))
    return fi,imu,ori,{k:(v-lift)/1000 for k,v in states.items()}

def simulate_axial(v,motor):
    """Fast vertical 1-D model used only for J350 drag calibration."""
    def f(t,x):
        z,vel=x; mass,_=mass_cg(t,v,motor); V=abs(vel)
        cd_eff=max(0.01,v.cd+v.cd2*(V/200.0)**2)
        drag=.5*v.rho*V*V*v.area*cd_eff*np.sign(vel)
        return [vel,(motor.thrust(t)-drag)/mass-G]
    def apogee(t,x): return 1.0 if t < 0.25 else x[1]
    apogee.terminal=True;apogee.direction=-1
    sol=solve_ivp(f,(0,40),[0,0],events=apogee,max_step=.02,rtol=2e-6,atol=1e-8)
    return float(np.max(sol.y[1])),float(np.max(sol.y[0]))

def calibrate_drag(v,target_v=172.559326,target_h=986.431274):
    vv=Vehicle(**vars(v)); vv.wind_e=vv.wind_n=0; vv.rail_tilt_deg=0
    def residual(x):
        vv.cd=float(x[0]); vv.cd2=float(x[1])
        try:vmax,hmax=simulate_axial(vv,J350)
        except Exception:return np.array([100.,100.])
        return np.array([(vmax-target_v)/target_v,(hmax-target_h)/target_h])
    opt=least_squares(residual,[vv.cd,vv.cd2],bounds=([.01,-1.0],[2.0,8.0]),xtol=1e-5,ftol=1e-5,gtol=1e-5,max_nfev=30)
    vv.cd=float(opt.x[0]);vv.cd2=float(opt.x[1]);r=simulate(vv,J350)
    return vv.cd,vv.cd2,r,float(np.dot(opt.fun,opt.fun))

st.set_page_config(page_title="Peregrine ascent model",layout="wide")
st.title("Peregrine passive ascent • revision 3")
with st.sidebar:
    motor=MOTORS[st.selectbox("Motor",list(MOTORS))]
    ignition_mass=st.number_input("Loaded mass (kg)",1.,10.,3.,.05); ignition_cg=st.number_input("Loaded CG from nose (m)",.5,1.6,1.25,.01)
    Iyy=st.number_input("Pitch/yaw inertia (kg m²)",.05,3.,.55,.01); Ixx=st.number_input("Roll inertia (kg m²)",.001,.5,.010,.001,format="%.3f")
    cd=st.number_input("Cd baseline",.01,2.0,.65,.01); cd2=st.number_input("Cd velocity² term",-1.0,3.0,.20,.05); cna=st.number_input("CNa (1/rad)",1.,30.,15.56,.1); cmq=st.number_input("Damping Cmq",0.,100.,12.,.5)
    cp=st.number_input("CP from nose (m)",.8,1.6,1.379,.005); wind_e=st.number_input("Wind east (m/s)",-30.,30.,12.,.5); wind_n=st.number_input("Wind north (m/s)",-30.,30.,0.,.5)
    rail_len=st.number_input("Rail length (m)",.5,10.,.9144,.1); rail_tilt=st.number_input("Rail tilt (deg)",0.,15.,0.,.1)
    do_cal=st.button("Calibrate Cd against measured J350"); do_run=st.button("Run prediction",type="primary")
v=Vehicle(ignition_mass=ignition_mass,ignition_cg=ignition_cg,Ixx=Ixx,Iyy=Iyy,cd=cd,cd2=cd2,cna=cna,cmq=cmq,cp=cp,wind_e=wind_e,wind_n=wind_n,rail_len=rail_len,rail_tilt_deg=rail_tilt)
if do_cal:
    fitted,fitted2,cal,loss=calibrate_drag(v); st.session_state.cal=(fitted,fitted2,cal,loss)
if "cal" in st.session_state:
    fitted,fitted2,cal,loss=st.session_state.cal
    message=f"J350 fit: Cd0={fitted:.3f}, Cd2={fitted2:.3f}; max V={cal.speed.max():.2f} m/s; apogee={cal.altitude.max():.2f} m; loss={loss:.6f}"
    if loss < 0.001:
        st.success(message)
        v.cd=fitted; v.cd2=fitted2
    else:
        st.error(message + " — fit rejected; predictions remain uncalibrated.")
input_signature=(motor.name,tuple(vars(v).items()))
if do_run or "result" not in st.session_state or st.session_state.get("input_signature") != input_signature:
    try:
        st.session_state.result=simulate(v,motor)
        st.session_state.input_signature=input_signature
    except Exception as ex:st.error(str(ex));st.stop()
r=st.session_state.result; ap=int(np.argmax(r.altitude)); rates=r.rates_deg_s; acc=np.array([np.rad2deg(free_dynamics(tt,yy,v,motor)[10:13]) if tt >= r.rail_exit_t else np.zeros(3) for tt,yy in zip(r.t,r.y.T)])
metrics=st.columns(6);metrics[0].metric("Rail exit",f"{r.rail_exit_t:.3f} s");metrics[1].metric("Apogee",f"{r.altitude[ap]:.1f} m");metrics[2].metric("Apogee time",f"{r.t[ap]:.2f} s");metrics[3].metric("Max speed",f"{r.speed.max():.1f} m/s");metrics[4].metric("Max q",f"{r.qdyn.max()/1000:.1f} kPa");metrics[5].metric("Apogee offset",f"{r.horizontal[ap]:.1f} m")
fig=make_subplots(rows=5,cols=1,shared_xaxes=True,subplot_titles=("Altitude / horizontal offset","Speed / dynamic pressure","Body-axis tilt / heading","Angular rates","Angular accelerations"))
for yy,n,row in [(r.altitude,"altitude m",1),(r.horizontal,"horizontal m",1),(r.speed,"speed m/s",2),(r.qdyn/1000,"q kPa",2),(r.tilt,"tilt deg",3),(r.heading,"heading deg",3)]:
    fig.add_trace(go.Scatter(x=r.t,y=yy,name=n),row=row,col=1)
for i,n in enumerate(["p","q","r"]):fig.add_trace(go.Scatter(x=r.t,y=rates[:,i],name=n+" deg/s"),4,1)
for i,n in enumerate(["p dot","q dot","r dot"]):fig.add_trace(go.Scatter(x=r.t,y=acc[:,i],name=n+" deg/s²"),5,1)
fig.add_vline(x=r.rail_exit_t,line_dash="dot",line_color="green");fig.add_vline(x=motor.burn_time,line_dash="dash",line_color="orange");fig.update_layout(height=1150,hovermode="x unified");st.plotly_chart(fig,width="stretch")
c1,c2=st.columns(2)
with c1:
    st.subheader("2D ground track");g=go.Figure(go.Scatter(x=r.y[0],y=r.y[1],mode="lines"));g.add_scatter(x=[r.y[0,ap]],y=[r.y[1,ap]],mode="markers",marker=dict(size=12,color="red"));g.update_yaxes(scaleanchor="x",scaleratio=1,title="north m");g.update_xaxes(title="east m");st.plotly_chart(g,width="stretch")
with c2:
    st.subheader("3D ascent trajectory");g=go.Figure(go.Scatter3d(x=r.y[0],y=r.y[1],z=r.y[2],mode="lines"));g.update_layout(scene=dict(xaxis_title="east m",yaxis_title="north m",zaxis_title="altitude m",aspectmode="data"));st.plotly_chart(g,width="stretch")
st.subheader("Measured CATS replay / comparison")
u=st.file_uploader("Upload .cfl or Base64 .txt",type=["cfl","txt","b64"])
if u:
    try:
        ver,rec,br,bt=parse_cfl(decode_upload(u));fi,imu,ori,events=cats_frames(rec);k=st.slider("Replay sample",0,len(ori)-1,min(75,len(ori)-1));tm=float(ori.t.iloc[k])
        st.write(f"Firmware {ver}; parsed {br:,}/{bt:,} bytes")
        if br < bt: st.warning(f"Incomplete parse: {bt-br} trailing bytes were not decoded. Do not treat this as a complete log.")
        m=make_subplots(rows=4,cols=1,shared_xaxes=True,subplot_titles=("Height / velocity","Body-axis tilt / heading","Gyro rate","Gyro-derived angular acceleration"))
        base=float(fi.height.iloc[np.argmin(abs(fi.t))]);m.add_trace(go.Scatter(x=fi.t,y=fi.height-base,name="measured height m"),1,1);m.add_trace(go.Scatter(x=fi.t,y=fi.velocity,name="measured velocity m/s"),1,1)
        m.add_trace(go.Scatter(x=ori.t,y=ori.tilt,name="measured tilt deg"),2,1);m.add_trace(go.Scatter(x=ori.t,y=ori.heading,name="measured heading deg"),2,1)
        gi=imu[["gx","gy","gz"]].to_numpy();ga=np.column_stack([np.gradient(gi[:,i],imu.t) for i in range(3)])
        for i,n in enumerate(["gx","gy","gz"]):m.add_trace(go.Scatter(x=imu.t,y=gi[:,i],name=n+" deg/s"),3,1)
        for i,n in enumerate(["gx dot","gy dot","gz dot"]):m.add_trace(go.Scatter(x=imu.t,y=ga[:,i],name=n+" deg/s²"),4,1)
        for row in range(1,5):m.add_vline(x=tm,line_color="red",row=row,col=1)
        for name,te in events.items():m.add_vline(x=te,line_dash="dot",annotation_text=name,row=1,col=1)
        m.update_layout(height=1000,hovermode="x unified");st.plotly_chart(m,width="stretch")
    except Exception as ex:st.exception(ex)
st.warning("Revision 3 fixes launch-pad motion, rail drag projection, broadside-flow force divergence and angular-acceleration plotting. Angular predictions are not validated against the J350 gyro history. Passing runtime tests does not establish physical accuracy.")
st.caption("The calibration button fits the two-parameter Cd(V) model to the measured J350 max velocity and apogee. CNa, damping and inertia still require independent identification before angular predictions are treated as validated.")
