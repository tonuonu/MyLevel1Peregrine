// Aerotech J420R-14A Motor Mass Equivalent Model
// Solid PLA with steel rod cavity and retainer shoulder

// === MOTOR SPECIFICATIONS ===
motor_diameter = 38;      // mm
motor_length = 337;       // mm
motor_mass = 650;         // grams

// === AFT CLOSURE SHOULDER ===
shoulder_diameter = 41;   // mm (38mm RMS aft closure)
shoulder_thickness = 8;   // mm

// === MATERIAL DENSITIES ===
pla_density = 1.24;       // g/cm³
steel_density = 7.85;     // g/cm³

// === STEEL ROD PARAMETERS ===
rod_diameter = 12;        // mm (12mm rod recommended)
rod_clearance = 0.3;      // mm

// === CALCULATIONS ===
motor_radius = motor_diameter / 2;
shoulder_radius = shoulder_diameter / 2;
rod_radius = rod_diameter / 2;
cavity_radius = rod_radius + rod_clearance;

// Body length (excluding shoulder)
body_length = motor_length - shoulder_thickness;

// Volumes (cm³)
body_volume_mm3 = PI * pow(motor_radius, 2) * body_length;
shoulder_volume_mm3 = PI * pow(shoulder_radius, 2) * shoulder_thickness;
solid_volume_cm3 = (body_volume_mm3 + shoulder_volume_mm3) / 1000;

pla_mass_if_solid = solid_volume_cm3 * pla_density;
mass_deficit = motor_mass - pla_mass_if_solid;

// Required steel rod
steel_volume_needed_cm3 = mass_deficit / steel_density;
rod_length_needed = (steel_volume_needed_cm3 * 1000) / (PI * pow(rod_radius, 2));

// Cavity positioning (centered in body, avoiding shoulder)
cavity_length = ceil(rod_length_needed) + 2;
cavity_offset = shoulder_thickness + (body_length - cavity_length) / 2;

// Final mass calculation
cavity_volume_cm3 = (PI * pow(cavity_radius, 2) * cavity_length) / 1000;
pla_volume_cm3 = solid_volume_cm3 - cavity_volume_cm3;
pla_mass = pla_volume_cm3 * pla_density;
rod_volume_cm3 = (PI * pow(rod_radius, 2) * rod_length_needed) / 1000;
rod_mass = rod_volume_cm3 * steel_density;
total_mass = pla_mass + rod_mass;

// === CONSOLE OUTPUT ===
echo("========================================");
echo("  AEROTECH J420R-14A MASS EQUIVALENT");
echo("========================================");
echo(str("Target mass: ", motor_mass, " g"));
echo(str("Body length: ", body_length, " mm"));
echo(str("Shoulder: ", shoulder_diameter, "mm x ", shoulder_thickness, "mm"));
echo("----------------------------------------");
echo(str("Steel rod: ", rod_diameter, "mm x ", rod_length_needed, "mm"));
echo(str("Cut rod to: ", ceil(rod_length_needed), " mm"));
echo("----------------------------------------");
echo(str("PLA mass: ", pla_mass, " g"));
echo(str("Steel mass: ", rod_mass, " g"));
echo(str("TOTAL MASS: ", total_mass, " g"));
echo(str("Target: ", motor_mass, " g (error: ", total_mass - motor_mass, " g)"));
echo("========================================");
echo("");
echo("NOTE: 337mm exceeds most print beds.");
echo("Suggested cut point: ~160mm from aft end");
echo("(keeps rod cavity in one piece)");

// === NOZZLE COSMETIC DETAIL ===
nozzle_exit_diameter = 14;
nozzle_depth = 6;

// === MODEL ===
module motor_with_shoulder() {
    difference() {
        union() {
            // Aft shoulder (at z=0, this is the aft/nozzle end)
            cylinder(h = shoulder_thickness, r = shoulder_radius, $fn = 72);
            
            // Main body
            translate([0, 0, shoulder_thickness])
                cylinder(h = body_length, r = motor_radius, $fn = 72);
        }
        
        // Rod cavity
        translate([0, 0, cavity_offset])
            cylinder(h = cavity_length + 0.1, r = cavity_radius, $fn = 48);
        
        // Nozzle detail (aft end)
        translate([0, 0, -0.1])
            cylinder(h = nozzle_depth + 0.1, 
                    r1 = nozzle_exit_diameter/2, 
                    r2 = nozzle_exit_diameter * 0.35, 
                    $fn = 48);
    }
}

motor_with_shoulder();
