// Peregrine L1 Ejection Piston
// Piston-style ejection system to protect parachute from hot gases
//
// The piston sits between the motor bay and recovery bay.
// Ejection gases push the piston, which pushes the parachute out.
// Shock cord passes through center hole, retaining the piston.
//
// RETENTION: Shock cord knot/washer below piston (standard practice)
// No external lip - that design was flawed (wouldn't fit in tube)
//
// Author: Generated for Tõnu's L1 Certification Project
// License: MIT

/* [Body Tube Dimensions] */
// Body tube inner diameter (mm) - piston slides inside this
body_tube_id = 99.1;

// Clearance between piston and tube wall (mm per side)
// Too tight = sticks, too loose = gas blows past
piston_clearance = 0.8;

/* [Piston Dimensions] */
// Total piston height (mm)
piston_height = 35;

// Cup cavity depth (mm) - deeper = more gas capture
cup_depth = 20;

// Cup wall thickness (mm)
cup_wall = 3.0;

// Base thickness below cup (mm)
base_thickness = 5;

/* [Shock Cord Retention] */
// Center hole diameter for shock cord (mm)
// Typical tubular nylon: 8-12mm, add clearance
cord_hole_dia = 14;

// Cord hole reinforcement thickness (mm)
cord_reinforce = 2;

// Cord hole reinforcement height above base (mm)
cord_reinforce_height = 10;

// Retention washer recess (for washer + knot below piston)
washer_recess = true;

// Washer outer diameter (mm) - e.g., M8 fender washer = 24mm
washer_od = 24;

// Washer recess depth (mm)
washer_recess_depth = 2;

/* [Vent Holes] */
// Include vent holes (REQUIRED - prevents vacuum lock during descent)
include_vents = true;

// Number of vent holes
vent_count = 6;

// Vent hole diameter (mm)
vent_dia = 5;

// Vent hole distance from center (mm)
vent_radius = 30;

/* [O-Ring Seal (Optional)] */
// Include O-ring groove for better gas seal
include_oring = false;

// O-ring cross-section diameter (mm) - standard 3mm
oring_dia = 3;

// O-ring groove depth (mm)
oring_groove_depth = 1.5;

// O-ring position from piston top (mm)
oring_position = 10;

/* [Print Settings] */
// Resolution
$fn = 100;

/* [Calculated Values] */
// Piston outer diameter
piston_od = body_tube_id - (2 * piston_clearance);

// Piston radius
piston_r = piston_od / 2;

// Cup inner diameter
cup_id = piston_od - (2 * cup_wall);

// Cup inner radius
cup_ir = cup_id / 2;

// ============================================
// Modules
// ============================================

// Main piston body (cylinder)
module piston_body() {
    cylinder(h = piston_height, r = piston_r, $fn = $fn);
}

// Cup cavity (hollows out the top - GAS SIDE)
// This captures ejection gas pressure
module cup_cavity() {
    translate([0, 0, base_thickness])
    cylinder(h = cup_depth + 1, r = cup_ir, $fn = $fn);
}

// Center hole for shock cord
module cord_hole() {
    translate([0, 0, -1])
    cylinder(h = piston_height + 2, d = cord_hole_dia, $fn = 64);
}

// Reinforcement ring around cord hole (inside cup)
module cord_reinforcement() {
    translate([0, 0, base_thickness])
    difference() {
        cylinder(h = cord_reinforce_height, d = cord_hole_dia + (2 * cord_reinforce), $fn = 64);
        translate([0, 0, -1])
        cylinder(h = cord_reinforce_height + 2, d = cord_hole_dia, $fn = 64);
    }
}

// Washer recess on bottom (PARACHUTE SIDE)
// Allows washer+knot to sit flush, retaining piston on cord
module washer_recess() {
    translate([0, 0, -0.01])
    cylinder(h = washer_recess_depth + 0.01, d = washer_od, $fn = 64);
}

// Vent holes through the base
// PURPOSE: Allow air to flow through during descent
// Without vents, vacuum forms behind piston, trapping parachute
module vent_holes() {
    for (i = [0 : vent_count - 1]) {
        angle = i * (360 / vent_count);
        rotate([0, 0, angle])
        translate([vent_radius, 0, -1])
        cylinder(h = base_thickness + 2, d = vent_dia, $fn = 32);
    }
}

// O-ring groove on outer surface (optional, for better gas seal)
module oring_groove() {
    translate([0, 0, piston_height - oring_position])
    rotate_extrude($fn = $fn)
    translate([piston_r - oring_groove_depth, 0, 0])
    circle(d = oring_dia, $fn = 32);
}

// Complete piston assembly
module ejection_piston() {
    difference() {
        union() {
            // Main body
            piston_body();
            
            // Cord hole reinforcement
            cord_reinforcement();
        }
        
        // Subtract cup cavity (gas side)
        cup_cavity();
        
        // Subtract cord hole
        cord_hole();
        
        // Subtract vent holes
        if (include_vents) {
            vent_holes();
        }
        
        // Subtract washer recess (parachute side)
        if (washer_recess) {
            washer_recess();
        }
        
        // Subtract O-ring groove
        if (include_oring) {
            oring_groove();
        }
    }
}

// ============================================
// Render
// ============================================

ejection_piston();

// ============================================
// Info Echo
// ============================================

echo("=== Ejection Piston Parameters ===");
echo(str("Body tube ID: ", body_tube_id, " mm"));
echo(str("Piston OD: ", piston_od, " mm"));
echo(str("Piston clearance: ", piston_clearance, " mm per side"));
echo(str("Total height: ", piston_height, " mm"));
echo(str("Cup depth: ", cup_depth, " mm"));
echo(str("Cup ID: ", cup_id, " mm"));
echo(str("Cord hole: ", cord_hole_dia, " mm"));
echo(str("Vent holes: ", include_vents ? str(vent_count, " x ", vent_dia, " mm") : "DISABLED (not recommended!)"));

// Volume estimate for pressure calculation
cup_volume_cm3 = PI * pow(cup_ir/10, 2) * (cup_depth/10);
echo(str("Cup volume: ~", cup_volume_cm3, " cm³"));

// Weight estimate (PETG ~1.27 g/cm³)
piston_vol = PI * pow(piston_r/10, 2) * (piston_height/10);
cup_vol = PI * pow(cup_ir/10, 2) * (cup_depth/10);
cord_vol = PI * pow((cord_hole_dia/2)/10, 2) * (piston_height/10);
approx_vol = piston_vol - cup_vol - cord_vol;
approx_weight = approx_vol * 1.27;
echo(str("Approx weight (PETG): ~", approx_weight, " g"));

echo("");
echo("=== HOW IT WORKS ===");
echo("1. Piston sits in body tube, cup facing MOTOR (aft)");
echo("2. Shock cord passes through center hole");
echo("3. Washer + knot BELOW piston retains it on cord");
echo("4. Parachute sits ABOVE piston (forward)");
echo("");
echo("EJECTION:");
echo("  - Motor charge fires, gas fills cup cavity");
echo("  - Pressure pushes piston forward");
echo("  - Piston pushes parachute out");
echo("  - Parachute NEVER touches hot gas!");
echo("");
echo("DESCENT (why vents matter):");
echo("  - Rocket falls, air rushes past");
echo("  - Without vents: vacuum forms behind piston");
echo("  - Vacuum holds piston in tube = parachute trapped!");
echo("  - WITH vents: air flows through, piston falls freely");
echo("");
echo("=== Assembly Notes ===");
echo("1. Print with PETG for heat resistance");
echo("2. Orient cup-side UP on print bed (base down)");
echo("3. Thread shock cord through center hole");
echo("4. Add fender washer (M8, 24mm OD) below piston");
echo("5. Tie figure-8 knot below washer");
echo("6. Test slide fit - should move freely with light resistance");
