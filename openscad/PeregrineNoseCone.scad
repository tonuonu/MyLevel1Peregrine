// Peregrine L1 Nose Cone
// Parametric ogive nose cone for Apogee Peregrine
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
// 300mm = 3 calibers (standard ogive)
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

/* [Ballast and Hardware] */
// Include ballast cavity
include_ballast_cavity = true;

// Ballast cavity diameter (mm)
ballast_cavity_dia = 30;

// Ballast cavity depth from shoulder end (mm)
ballast_cavity_depth = 80;

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

// Ogive radius (for tangent ogive calculation)
ogive_radius = (base_radius * base_radius + nose_length * nose_length) / (2 * base_radius);

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
    tip_solid = 20; // Solid tip region
    
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
        cylinder(h = shoulder_length + 2, r = shoulder_radius - shoulder_wall, $fn = $fn);
    }
}

// Ballast cavity (accessible from shoulder end)
module ballast_cavity() {
    translate([0, 0, nose_length + shoulder_length - ballast_cavity_depth])
    cylinder(h = ballast_cavity_depth + 1, d = ballast_cavity_dia, $fn = 64);
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

// ============================================
// Info Echo
// ============================================

echo("=== Peregrine Nose Cone Parameters ===");
echo(str("Body tube OD: ", body_tube_od, " mm"));
echo(str("Body tube ID: ", body_tube_id, " mm"));
echo(str("Shoulder OD: ", shoulder_radius * 2, " mm"));
echo(str("Nose length: ", nose_length, " mm"));
echo(str("Shoulder length: ", shoulder_length, " mm"));
echo(str("Total length: ", nose_length + shoulder_length, " mm"));
echo(str("Wall thickness: ", wall_thickness, " mm"));
echo(str("Shape: ", shape_type == 0 ? "Ogive" : shape_type == 1 ? "Conical" : shape_type == 2 ? "Elliptical" : "Parabolic"));

if (include_ballast_cavity) {
    // Approximate ballast volume in cm³
    ballast_vol = PI * pow(ballast_cavity_dia/2, 2) * ballast_cavity_depth / 1000;
    echo(str("Ballast cavity volume: ", ballast_vol, " cm³"));
    echo(str("Lead shot capacity: ~", ballast_vol * 7.0, " g"));
    echo(str("Steel shot capacity: ~", ballast_vol * 4.8, " g"));
}

echo(str("Fits Bambu P1S (256mm): ", nose_length + shoulder_length <= 256 ? "YES" : "NO - use split_for_printing=true"));
