#!/usr/bin/env python3
"""ATLAS FORGE continuity toolkit: offline engineering example (noncanonical addon).

Generate a non-load-bearing coil-winding former from a mathematical profile,
export watertight binary STL using *only Python standard library*, and create an
OpenSCAD source. Optionally link exact-revision concepts from the unmodified
canonical 15-node federation. No slicer, printer, physical inspection, electrical
component certification, or internet required to generate the model.

An STL is not printer-ready G-code, nor an observed manufactured object.
"""
from __future__ import annotations
from pathlib import Path
import argparse,hashlib,importlib.util,json,math,struct,csv,io

VERSION='0.1.0'
RECORD_IDS=[
 'manufacturing-atlas:chapter-14-concept',
 'manufacturing-atlas:chapter-24-concept',
 'manufacturing-atlas:chapter-23-concept',
 'materials-atlas:process-structure-property',
 'energy-atlas:chapter-14-concept',
 'electronics-semiconductors-atlas:chapter-47-concept',
]


def as_json_bytes(obj):
    return (json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode('utf-8')


def digest(buf:bytes)->str:
    return hashlib.sha256(buf).hexdigest()


def profile(bore_d=8.4, core_d=16.0, flange_d=40.0, base_thickness=3.0,
            core_length=15.0, shoulder_rise=12.0, top_thickness=3.0):
    vals=[bore_d,core_d,flange_d,base_thickness,core_length,shoulder_rise,top_thickness]
    if any(type(x) not in (float,int) or not math.isfinite(x) for x in vals):
        raise ValueError('finite numeric dimensions in millimeters required')
    if not (2.0<=bore_d<=12.0 and bore_d+4.0<=core_d<=25.0 and
            core_d+4.0<=flange_d<=70.0 and base_thickness>=2.0 and
            core_length>=8.0 and shoulder_rise>=2.0 and top_thickness>=2.0):
        raise ValueError('outside conservative reference geometry envelope')
    if shoulder_rise+1e-8 < (flange_d-core_d)/2.0:
        raise ValueError('upper flange slope exceeds 45-degree self-support target')
    if flange_d>70 or base_thickness+core_length+shoulder_rise+top_thickness>80:
        raise ValueError('outside bounded compact demonstration size')
    ri=bore_d/2;rc=core_d/2;rf=flange_d/2
    z0=base_thickness;z1=z0+core_length;z2=z1+shoulder_rise;zt=z2+top_thickness
    return ((ri,0.0),(rf,0.0),(rf,z0),(rc,z0),(rc,z1),(rf,z2),(rf,zt),(ri,zt))


def triangles(prof,segments=96):
    if type(segments) is not int or not 24<=segments<=256 or segments%4:
        raise ValueError('segments must be divisible by 4 and between 24 and 256')
    # Each edge sweeps an annular patch around the z axis. The section is
    # counter-clockwise in (r,z), yielding outward-facing STL triangles.
    for (ar,az),(br,bz) in zip(prof,prof[1:]+prof[:1]):
        for i in range(segments):
            t=2*math.pi*i/segments;u=2*math.pi*(i+1)/segments
            a=(ar*math.cos(t),ar*math.sin(t),az)
            b=(ar*math.cos(u),ar*math.sin(u),az)
            c=(br*math.cos(t),br*math.sin(t),bz)
            d=(br*math.cos(u),br*math.sin(u),bz)
            yield (a,b,c)
            yield (b,d,c)


def normal(a,b,c):
    x=(b[1]-a[1])*(c[2]-a[2])-(b[2]-a[2])*(c[1]-a[1])
    y=(b[2]-a[2])*(c[0]-a[0])-(b[0]-a[0])*(c[2]-a[2])
    z=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    norm=math.sqrt(x*x+y*y+z*z)
    if norm<1e-12:raise ValueError('degenerate facet')
    return (x/norm,y/norm,z/norm)


def stl_bytes(prof,segments=96):
    faces=list(triangles(prof,segments))
    buf=bytearray(b'ATLAS FORGE original offline coil-former v0.1 STL'.ljust(80,b' '))
    buf.extend(struct.pack('<I',len(faces)))
    for a,b,c in faces:
        buf.extend(struct.pack('<12fH',*(normal(a,b,c)+a+b+c),0))
    return bytes(buf)


def scad_source(prof,segments=96):
    points=',\n    '.join(f'[{r:.4f},{z:.4f}]' for r,z in prof)
    return f'''// ATLAS FORGE original continuity-tutorial geometry v{VERSION}
// Units: millimeters. Nonstructural coil former, low-voltage experiments only.
// IMPORTANT: Solid CAD is NOT printer-specific G-code or manufactured qualification.
$fn={segments};
rotate_extrude(convexity=10,$fn={segments})
  polygon(points=[
    {points}
  ]);
'''


def geometry_receipt(prof,segments,blob):
    # Exact volume for profile of revolution of each section using Pappus's
    # theorem and the closed polygon's first radial moment.
    # Triangulated surface mesh volume is checked independently by tests.
    cross=0.0;moment=0.0
    for (x,y),(u,v) in zip(prof,prof[1:]+prof[:1]):
        area2=x*v-u*y
        cross+=area2
        moment+=(x+u)*area2
    area=cross/2
    if area<=0:raise ValueError('cross-section invalid orientation')
    centroid_r=moment/(6*area)
    volume=2*math.pi*centroid_r*area
    return {'schema':'atlas.offline-coil-former-design/1',
      'edition':VERSION,'dimensions_mm':{'flange_diameter':prof[1][0]*2,
          'bore_diameter':prof[0][0]*2,'core_diameter':prof[3][0]*2,
          'total_height':prof[6][1]},
      'segments':segments,'triangle_count':len(blob[84:])//50,'stl_sha256':digest(blob),
      'analytic_solid_volume_mm3':round(volume,3),'maximum_nominal_design_envelope_mm':[prof[1][0]*2,prof[1][0]*2,prof[6][1]],
      'intended_orientation':'flat broad base flange on printer bed, z axis vertical',
      'material_recommendation':'PLA or PETG for demonstration; not heat-rated or load-rated',
      'load_bearing_certification':False,'printer_profile_verified':False,
      'gcode_generated':False,'physical_print_observed':False,'coil_electrical_performance_measured':False}


def atlas_evidence(root:Path|None):
    if root is None:
        return {'atlas_checked':False,'warning':'No canonical Atlas root supplied; no source link asserted','source_records':[]}
    path=root/'tools/atlas_offline.py'
    if not path.is_file():raise ValueError('Atlas root missing tools/atlas_offline.py')
    s=importlib.util.spec_from_file_location('atlas_survival_reader_for_print_bridge',str(path))
    if s is None or s.loader is None:raise ValueError('Cannot load offline reader')
    module=importlib.util.module_from_spec(s);s.loader.exec_module(module)
    atlas=module.Atlas(root)
    # Load verifies digest of every federated node collection and every exact
    # revision relationship, rather than authoring invented scientific records.
    records=atlas.records
    links=[]
    for rid in RECORD_IDS:
        x=records.get(rid)
        if x is None:raise ValueError(f'missing exact Atlas record {rid}')
        links.append({'record_id':rid,'revision':x['revision'],'node':x['node_id'],
          'title':x['title'],'review_status':x.get('evidence',{}).get('review_status','not externally verified')})
    return {'atlas_checked':True,'edition':'Computer_Architecture_v0.5.0_continuity',
        'node_count':len(atlas.nodes),'records':len(records),
        'exact_graph_relationships':len(atlas.relations),
        'source_records':links,
        'source_link_not_material_property_certification':True}


def build(output:Path,atlas_root:Path|None=None,segments=96, **dimensions):
    output.mkdir(parents=True,exist_ok=True)
    prof=profile(**dimensions)
    stl=stl_bytes(prof,segments)
    scad=scad_source(prof,segments).encode('utf-8')
    (output/'ATLAS_COIL_FORMER.stl').write_bytes(stl)
    (output/'ATLAS_COIL_FORMER.scad').write_bytes(scad)
    receipt=geometry_receipt(prof,segments,stl)
    receipt['scad_sha256']=digest(scad)
    receipt['atlas_evidence']=atlas_evidence(atlas_root)
    (output/'DESIGN_EVIDENCE.json').write_bytes(as_json_bytes(receipt))
    guide=f'''# ATLAS FORGE / Off-grid fabrication trial — Coil former (non-safety-critical)

**Generated completely offline.** This is original, parametric example geometry
for winding a small experimental copper coil. It is not a tested generator,
transformer, motor, certified insulator, food/water device, or electrical component.

## Verified *digital* design

- Flange outer diameter: **{prof[1][0]*2:.1f} mm**; overall height: **{prof[6][1]:.1f} mm**
- Barrel/core outer diameter: **{prof[3][0]*2:.1f} mm**
- Central through bore: **{prof[0][0]*2:.1f} mm** (nominal; actual print needs caliper check)
- Lower flange thickness: **{prof[2][1]:.1f} mm**
- Straight barrel winding region: **{prof[4][1]-prof[3][1]:.1f} mm**
- Upper flange shoulder built over a **{prof[5][1]-prof[4][1]:.1f} mm rise/{prof[5][0]-prof[4][0]:.1f} mm radial step** (at most 45-degree unsupported overhang reference)
- Binary STL SHA-256: `{digest(stl)}`
- Editable OpenSCAD SHA-256: `{digest(scad)}`
- Analytic full-solid volume: **{receipt['analytic_solid_volume_mm3']:.1f} mm³**; actual filament use varies by infill and slicer

## Offline build sequence

1. Confirm your computer can open the Atlas archive *without Internet* and has a locally installed slicer matching your exact printer, nozzle, filament and saved machine profile.
2. Open `ATLAS_COIL_FORMER.scad` in OpenSCAD, or import `ATLAS_COIL_FORMER.stl` into the slicer. Both were generated with no web services.
3. Check the bounding box fits your printer's usable build volume; choose the broad **40 mm base flange flat on the bed**. Inspect the upper 45-degree shoulder and use supports if your equipment cannot print it reliably.
4. Select a manufacturer-recommended profile for your actual filament and machine. Do **not** assume temperature, speed, cooling, adhesion, supports or extrusion are correct from a generic file.
5. Slice to machine-specific G-code *locally*; review the preview and generated travel paths before printing. A slicer has **not** been provided by this artifact.
6. If grid power is unavailable, only operate a printer and ventilated work area with a safe manufacturer-approved power setup. Never power a hotend from improvised wiring or a household indoor combustion generator.
7. Print; then measure outside diameter, bore, overall height, delamination/warping and visual defects. Record actual measurements and photographs/notes. A valid STL alone is not a usable part.
8. For a *low-voltage educational experiment only*, wind **insulated** copper wire on the former and secure the ends without sharp edges. Use an appropriately current-limited low-voltage supply and instrumented experiments; do not connect to mains, batteries without current limiting, or uncontrolled heat-producing loads. No coil output or magnetic performance has been verified.

## What you still need physically

A working 3D printer, appropriate dry filament, local slicer/printer profile, safe electricity, replacement nozzle/belts/fans, calipers, suitable tools, insulated copper wire and a regulated low-voltage test supply (only if performing a coil experiment). The Atlas does not create raw copper, magnets, electronics, electricity, or printer parts from nothing.

**Release boundary:** CAD/STL geometry can be independently verified; slicing, printer operation, fitting, electrical functionality, and physical material qualification are not established. This supplement does not alter the canonical scientific federation.
'''
    (output/'PRINT_AND_INSPECT.md').write_text(guide)
    return receipt


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--atlas-root',type=Path)
    parser.add_argument('--segments',type=int,default=96)
    parser.add_argument('--bore-mm',type=float,default=8.4,help='nominal bore diameter; verify real fit')
    parser.add_argument('--core-mm',type=float,default=16.0,help='coil barrel diameter')
    parser.add_argument('--flange-mm',type=float,default=40.0,help='flange OD, must fit print volume')
    parser.add_argument('--barrel-length-mm',type=float,default=15.0)
    parser.add_argument('--shoulder-rise-mm',type=float,default=12.0)
    args=parser.parse_args()
    r=build(args.out,args.atlas_root,args.segments,bore_d=args.bore_mm,core_d=args.core_mm,flange_d=args.flange_mm,core_length=args.barrel_length_mm,shoulder_rise=args.shoulder_rise_mm)
    print(json.dumps({'result':'DIGITAL_MESH_CREATED_PHYSICAL_PRINT_NOT_VERIFIED',
      'stl_sha256':r['stl_sha256'],'stl_triangles':r['triangle_count'],
      'atlas_exact_records_linked':len(r['atlas_evidence']['source_records']),
      'printer_Gcode_created':False},indent=2))

if __name__=='__main__':main()
