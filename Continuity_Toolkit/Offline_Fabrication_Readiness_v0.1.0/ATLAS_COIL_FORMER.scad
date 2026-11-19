// ATLAS FORGE original continuity-tutorial geometry v0.1.0
// Units: millimeters. Nonstructural coil former, low-voltage experiments only.
// IMPORTANT: Solid CAD is NOT printer-specific G-code or manufactured qualification.
$fn=96;
rotate_extrude(convexity=10,$fn=96)
  polygon(points=[
    [4.2000,0.0000],
    [20.0000,0.0000],
    [20.0000,3.0000],
    [8.0000,3.0000],
    [8.0000,18.0000],
    [20.0000,30.0000],
    [20.0000,33.0000],
    [4.2000,33.0000]
  ]);
