// Peregrine L1 Ejection Piston
// Piston-style ejection system to protect parachute from hot gases
//
// The piston sits between the motor bay and recovery bay.
// Ejection gases push the piston, which pushes the parachute out.
// Shock cord passes through center hole, retaining the piston.
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

// Retention lip width (mm) - catches on tube end
lip_width = 4;

// Retention lip height (mm)
lip_height = 3;

/* [Shock Cord Hole] */
// Center hole diameter for shock cord (mm)
// Typical tubular nylon: 8-12mm, add clearance
cord_hole_dia = 14;

// Cord hole reinforcement thickness (mm)
cord_reinforce = 2;

// Cord hole reinforcement height above base (mm)
cord_reinforce_height = 10;

/* [Vent Holes] */
// Number of vent holes (prevents vacuum lock)
vent_count = 6;

// Vent hole diameter (mm)
vent_dia = 5;

// Vent hole distance from center (mm)
vent_radius = 30;

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

// Lip outer diameter (extends beyond tube ID to catch)
lip_od = body_tube_id + (2 * lip_width);

// ============================================
// Modules
// ============================================

// Main piston body (cylinder)
module piston_body() {
    cylinder(h = piston_height, r = piston_r, $fn = $fn);
}

// Cup cavity (hollows out the top)
module cup_cavity() {
    translate([0, 0, base_thickness])
    cylinder(h = cup_depth + 1, r = cup_ir, $fn = $fn);
}

// Center hole for shock cord
module cord_hole() {
    translate([0, 0, -1])
    cylinder(h = piston_height + 2, d = cord_hole_dia, $fn = 64);
}

// Reinforcement ring around cord hole
module cord_reinforcement() {
    translate([0, 0, base_thickness])
    difference() {
        cylinder(h = cord_reinforce_height, d = cord_hole_dia + (2 * cord_reinforce), $fn = 64);
        translate([0, 0, -1])
        cylinder(h = cord_reinforce_height + 2, d = cord_hole_dia, $fn = 64);
    }
}

// Vent holes in the base
module vent_holes() {
    for (i = [0 : vent_count - 1]) {
        angle = i * (360 / vent_count);
        rotate([0, 0, angle])
        translate([vent_radius, 0, -1])
        cylinder(h = base_thickness + 2, d = vent_dia, $fn = 32);
    }
}

// Retention lip at top edge
module retention_lip() {
    translate([0, 0, piston_height - lip_height])
    difference() {
        cylinder(h = lip_height, r = lip_od / 2, $fn = $fn);
        translate([0, 0, -1])
        cylinder(h = lip_height + 2, r = piston_r - 0.1, $fn = $fn);
    }
}

// O-ring groove (optional, for better seal)
module oring_groove(groove_dia = 3, groove_depth = 1.5, position_from_top = 10) {
    translate([0, 0, piston_height - position_from_top])
    rotate_extrude($fn = $fn)
    translate([piston_r - groove_depth, 0, 0])
    circle(d = groove_dia, $fn = 32);
}

// Complete piston assembly
module ejection_piston() {
    difference() {
        union() {
            // Main body
            piston_body();
            
            // Retention lip
            retention_lip();
            
            // Cord hole reinforcement
            cord_reinforcement();
        }
        
        // Subtract cup cavity
        cup_cavity();
        
        // Subtract cord hole
        cord_hole();
        
        // Subtract vent holes
        vent_holes();
        
        // Optional: O-ring groove for better gas seal
        // Uncomment if using o-ring
        // oring_groove();
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
echo(str("Lip OD: ", lip_od, " mm (catches on tube end)"));
echo(str("Vent holes: ", vent_count, " x ", vent_dia, " mm"));

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
echo("=== Assembly Notes ===");
echo("1. Print with PETG for heat resistance");
echo("2. Orient cup-side DOWN on print bed");
echo("3. Thread shock cord through center hole");
echo("4. Tie knot or use washer+knot to retain");
echo("5. Test slide fit before flight - should move freely");
echo("6. Lip catches on tube end, prevents flying away");
