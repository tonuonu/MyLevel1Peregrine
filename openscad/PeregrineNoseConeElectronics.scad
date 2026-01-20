// Peregrine L1 Nose Cone with Electronics Bay
// Parametric ogive nose cone with CATS Vega mount and battery holder
// Designed to fit body tube ID 99.1mm, OD 102mm
// 
// Author: Generated for Tõnu's L1 Certification Project
// License: MIT

/* [Main Dimensions] */
// Body tube outer diameter (mm)
body_tube_od = 102;

// Body tube inner diameter (mm)
body_tube_id = 99.1;

// Nose cone length (mm) - typically 3-5 calibers
// 150mm = 1.5 calibers (blunter, more drag, slower flight)
// For P1S single-piece print: max ~150mm nose + 100mm shoulder = 250mm
nose_length = 150;

// Shoulder length (mm) - typically 1-1.5 calibers
shoulder_length = 100;

/* [Wall and Fit] */
// Wall thickness (mm)
wall_thickness = 2.5;

// Shoulder clearance (mm) - gap for easy fit into tube
shoulder_clearance = 0.6;

// Shoulder wall thickness (mm)
shoulder_wall = 2.0;

/* [Nose Cone Shape] */
// Shape: 0=Ogive, 1=Conical, 2=Elliptical, 3=Parabolic
shape_type = 0; // [0:Ogive, 1:Conical, 2:Elliptical, 3:Parabolic]

// Ogive shape factor (1.0 = tangent ogive, higher = more blunt)
ogive_factor = 1.0;

/* [CATS Vega Flight Computer] */
// Include CATS Vega mount
include_vega_mount = true;

// CATS Vega PCB length (mm) - from catsystems.io specs
vega_length = 100;

// CATS Vega PCB width (mm) - from catsystems.io specs
vega_width = 33;

// CATS Vega PCB thickness (mm)
vega_thickness = 1.6;

// CATS Vega total height with components (mm) - without antenna
vega_height = 21;

// Mounting hole diameter (mm)
vega_mount_hole_dia = 3.2;

// Distance from edge to mounting holes (mm)
vega_mount_edge_dist = 3;

// Clearance around PCB (mm)
vega_clearance = 1.0;

/* [Battery Holder] */
// Include battery holder
include_battery_holder = true;

// Number of AA batteries
num_batteries = 2; // [1:4]

// AA battery length (mm)
aa_length = 50.5;

// AA battery diameter (mm)
aa_diameter = 14.5;

// Battery holder wall thickness (mm)
battery_wall = 1.5;

// Battery clearance (mm)
battery_clearance = 0.5;

/* [Sled Configuration] */
// Sled thickness (mm)
sled_thickness = 3;

// Sled position from shoulder end (mm)
sled_position = 20;

// Mounting screw holes diameter (mm)
sled_screw_dia = 4;

/* [Ballast Cavity] */
// Include ballast cavity (in tip, for epoxy/lead shot)
include_ballast_cavity = true;

// Ballast cavity diameter (mm)
ballast_cavity_dia = 30;

// Ballast cavity depth from tip (mm)
ballast_cavity_depth = 50;

/* [Print Settings] */
// Resolution (higher = smoother but slower)
$fn = 100;

// Split into two parts for printing
split_for_printing = false;

// Split position from base (mm) - only used if split_for_printing=true
split_position = 125;

// Joint overlap (mm)
joint_overlap = 15;

// Joint clearance (mm)
joint_clearance = 0.3;

/* [Calculated Values] */
// Base radius (outer)
base_radius = body_tube_od / 2;

// Shoulder outer radius (fits inside body tube)
shoulder_radius = (body_tube_id - shoulder_clearance) / 2;

// Shoulder inner radius
shoulder_inner_radius = shoulder_radius - shoulder_wall;

// Ogive radius (for tangent ogive calculation)
ogive_radius = (base_radius * base_radius + nose_length * nose_length) / (2 * base_radius);

// Sled width (fits inside shoulder)
sled_width = (shoulder_inner_radius - 2) * 2;

// ============================================
// Nose Cone Profile Functions
// ============================================

// Tangent Ogive profile
function ogive_radius_at(x) = 
    let(rho = ogive_radius * ogive_factor)
    sqrt(rho * rho - (nose_length - x) * (nose_length - x)) - rho + base_radius;

// Conical profile
function conical_radius_at(x) = base_radius * x / nose_length;

// Elliptical profile  
function elliptical_radius_at(x) = base_radius * sqrt(1 - ((nose_length - x) / nose_length) * ((nose_length - x) / nose_length));

// Parabolic profile
function parabolic_radius_at(x) = base_radius * sqrt(x / nose_length);

// Select profile based on shape_type
function profile_radius_at(x) = 
    shape_type == 0 ? ogive_radius_at(x) :
    shape_type == 1 ? conical_radius_at(x) :
    shape_type == 2 ? elliptical_radius_at(x) :
    parabolic_radius_at(x);

// ============================================
// Modules
// ============================================

// Generate nose cone outer shell as rotational solid
module nose_cone_outer() {
    step = nose_length / $fn;
    
    rotate_extrude(angle = 360, $fn = $fn) {
        polygon(points = concat(
            [[0, 0]],
            [for (x = [step : step : nose_length]) 
                [profile_radius_at(x), x]],
            [[base_radius, nose_length]],
            [[0, nose_length]]
        ));
    }
}

// Generate nose cone inner cavity
module nose_cone_inner() {
    step = nose_length / $fn;
    tip_solid = ballast_cavity_depth + 10; // Solid tip region for ballast
    
    rotate_extrude(angle = 360, $fn = $fn) {
        polygon(points = concat(
            [[0, tip_solid]],
            [for (x = [tip_solid + step : step : nose_length]) 
                [max(0, profile_radius_at(x) - wall_thickness), x]],
            [[base_radius - wall_thickness, nose_length]],
            [[0, nose_length]]
        ));
    }
}

// Shoulder (slides into body tube)
module shoulder() {
    translate([0, 0, nose_length])
    difference() {
        cylinder(h = shoulder_length, r = shoulder_radius, $fn = $fn);
        
        // Hollow inside
        translate([0, 0, -1])
        cylinder(h = shoulder_length + 2, r = shoulder_inner_radius, $fn = $fn);
    }
}

// Ballast cavity (in nose tip, for epoxy fill)
module ballast_cavity() {
    translate([0, 0, 5]) // 5mm from very tip
    cylinder(h = ballast_cavity_depth, d = ballast_cavity_dia, $fn = 64);
}

// CATS Vega mounting posts
module vega_mount_posts() {
    post_height = 10;
    post_dia = vega_mount_hole_dia + 4;
    
    // Four corner posts
    hole_x = vega_width/2 - vega_mount_edge_dist;
    hole_y = vega_length/2 - vega_mount_edge_dist;
    
    for (x = [-1, 1], y = [-1, 1]) {
        translate([x * hole_x, y * hole_y, 0])
        difference() {
            cylinder(h = post_height, d = post_dia, $fn = 32);
            translate([0, 0, -1])
            cylinder(h = post_height + 2, d = vega_mount_hole_dia, $fn = 32);
        }
    }
}

// CATS Vega outline (for visualization)
module vega_board() {
    color("green", 0.5)
    translate([-vega_width/2, -vega_length/2, 10])
    cube([vega_width, vega_length, vega_thickness]);
}

// AA Battery holder (batteries laid parallel to Vega)
module battery_holder() {
    battery_slot_dia = aa_diameter + battery_clearance * 2;
    holder_height = battery_slot_dia/2 + battery_wall;
    
    // Batteries laid lengthwise, stacked vertically
    for (i = [0 : num_batteries - 1]) {
        translate([0, 0, i * (battery_slot_dia + battery_wall)])
        difference() {
            // Outer shell for one battery
            translate([-battery_slot_dia/2 - battery_wall, -aa_length/2 - battery_wall, 0])
            cube([battery_slot_dia + battery_wall * 2, aa_length + battery_wall * 2, holder_height]);
            
            // Battery slot
            translate([0, 0, holder_height])
            rotate([-90, 0, 0])
            translate([0, 0, -aa_length/2 - battery_clearance])
            cylinder(h = aa_length + battery_clearance * 2, d = battery_slot_dia, $fn = 32);
        }
    }
}

// Electronics sled (mounts inside shoulder)
// Layout: Vega and batteries side by side, not in series
module electronics_sled() {
    battery_slot_dia = aa_diameter + battery_clearance * 2;
    battery_holder_width = battery_slot_dia + battery_wall * 2;
    
    // Calculate sled length to fit Vega (100mm)
    actual_sled_length = vega_length + 10; // Add margin
    
    // Main sled plate
    difference() {
        union() {
            // Base plate - rounded rectangle
            hull() {
                translate([sled_width/2 - 5, 5, 0])
                cylinder(h = sled_thickness, r = 5, $fn = 32);
                translate([-(sled_width/2 - 5), 5, 0])
                cylinder(h = sled_thickness, r = 5, $fn = 32);
                translate([sled_width/2 - 5, actual_sled_length - 5, 0])
                cylinder(h = sled_thickness, r = 5, $fn = 32);
                translate([-(sled_width/2 - 5), actual_sled_length - 5, 0])
                cylinder(h = sled_thickness, r = 5, $fn = 32);
            }
        }
        
        // Lightening holes
        for (y = [25, 55, 85]) {
            translate([0, y, -1])
            cylinder(h = sled_thickness + 2, d = 15, $fn = 32);
        }
    }
    
    // CATS Vega mount (centered, slightly offset to make room for batteries)
    if (include_vega_mount) {
        vega_x_offset = include_battery_holder ? -battery_holder_width/2 - 2 : 0;
        translate([vega_x_offset, actual_sled_length/2, sled_thickness])
        vega_mount_posts();
    }
    
    // Battery holder (beside Vega, batteries stacked)
    if (include_battery_holder) {
        battery_x_offset = include_vega_mount ? vega_width/2 + battery_holder_width/2 + 4 : 0;
        translate([battery_x_offset, actual_sled_length/2, sled_thickness])
        battery_holder();
    }
}

// Sled rails inside shoulder
module sled_rails() {
    rail_width = 5;
    rail_height = 3;
    rail_length = shoulder_length - 10;
    
    // Two rails on opposite sides
    for (angle = [0, 180]) {
        rotate([0, 0, angle])
        translate([shoulder_inner_radius - rail_width, -rail_width/2, nose_length + 5])
        cube([rail_width, rail_width, rail_length]);
    }
}

// Complete nose cone
module complete_nose_cone() {
    difference() {
        union() {
            // Main nose cone shape
            difference() {
                nose_cone_outer();
                nose_cone_inner();
            }
            
            // Shoulder
            shoulder();
            
            // Sled rails
            if (include_vega_mount || include_battery_holder) {
                sled_rails();
            }
        }
        
        // Ballast cavity
        if (include_ballast_cavity) {
            ballast_cavity();
        }
    }
}

// Split joint - female (socket)
module joint_female() {
    cylinder(h = joint_overlap, r = base_radius - wall_thickness + joint_clearance, $fn = $fn);
}

// Split joint - male (plug)
module joint_male() {
    cylinder(h = joint_overlap, r = base_radius - wall_thickness, $fn = $fn);
}

// Lower section (tip to split)
module lower_section() {
    difference() {
        intersection() {
            complete_nose_cone();
            cylinder(h = split_position, r = base_radius + 1, $fn = $fn);
        }
        
        // Female joint socket at top
        translate([0, 0, split_position - joint_overlap])
        joint_female();
    }
}

// Upper section (split to shoulder)
module upper_section() {
    difference() {
        complete_nose_cone();
        
        // Remove lower section
        cylinder(h = split_position - joint_overlap, r = base_radius + 1, $fn = $fn);
    }
    
    // Male joint plug
    translate([0, 0, split_position - joint_overlap])
    difference() {
        joint_male();
        
        // Keep it hollow
        translate([0, 0, -1])
        cylinder(h = joint_overlap + 2, r = base_radius - wall_thickness - shoulder_wall, $fn = $fn);
    }
}

// ============================================
// Render
// ============================================

if (split_for_printing) {
    // Show both parts side by side
    translate([-base_radius - 10, 0, 0])
    lower_section();
    
    translate([base_radius + 10, 0, 0])
    upper_section();
} else {
    // Complete nose cone
    complete_nose_cone();
}

// Show electronics sled separately (for printing)
if (include_vega_mount || include_battery_holder) {
    actual_sled_length = vega_length + 10;
    battery_slot_dia = aa_diameter + battery_clearance * 2;
    battery_holder_width = battery_slot_dia + battery_wall * 2;
    vega_x_offset = include_battery_holder ? -battery_holder_width/2 - 2 : 0;
    
    translate([base_radius * 3, 0, 0])
    electronics_sled();
    
    // Show CATS Vega board position (visualization only)
    %translate([base_radius * 3 + vega_x_offset, actual_sled_length/2, sled_thickness])
    vega_board();
}

// ============================================
// Info Echo
// ============================================

echo("=== Peregrine Nose Cone with Electronics ===");
echo(str("Body tube OD: ", body_tube_od, " mm"));
echo(str("Body tube ID: ", body_tube_id, " mm"));
echo(str("Shoulder OD: ", shoulder_radius * 2, " mm"));
echo(str("Nose length: ", nose_length, " mm"));
echo(str("Shoulder length: ", shoulder_length, " mm"));
echo(str("Total length: ", nose_length + shoulder_length, " mm"));
echo(str("Wall thickness: ", wall_thickness, " mm"));
echo(str("Sled width: ", sled_width, " mm"));

if (include_vega_mount) {
    echo(str("CATS Vega dimensions: ", vega_length, " x ", vega_width, " x ", vega_height, " mm (from catsystems.io)"));
}

if (include_battery_holder) {
    echo(str("Battery holder: ", num_batteries, " x AA batteries"));
}

if (include_ballast_cavity) {
    ballast_vol = PI * pow(ballast_cavity_dia/2, 2) * ballast_cavity_depth / 1000;
    echo(str("Ballast cavity volume: ", ballast_vol, " cm³"));
    echo(str("Epoxy fill capacity: ~", ballast_vol * 1.1, " g"));
    echo(str("Lead shot capacity: ~", ballast_vol * 7.0, " g"));
}

echo(str("Fits Bambu P1S (256mm): ", nose_length + shoulder_length <= 256 ? "YES" : "NO - use split_for_printing=true"));
