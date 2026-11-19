#!/usr/bin/env python3
"""Portable STL validator using only the Python standard library.

Checks binary STL framing, nondegenerate triangles, outward consistency,
closed two-face-per-edge mesh topology, dimensions and positive signed volume.
It is NOT a physical print qualification or a 3D-printer slicer.
"""
from pathlib import Path
import hashlib,json,math,struct,collections,argparse


def verify_stl(path:Path,expected_extents=(40.,40.,33.),tol_mm=0.025):
    buf=path.read_bytes()
    if len(buf)<84:raise ValueError('truncated binary STL')
    n=struct.unpack_from('<I',buf,80)[0]
    if len(buf)!=84+n*50 or n<100:raise ValueError('STL length or triangle count invalid')
    edges=collections.Counter();vertices=set();tris=[]
    lower=[float('inf')]*3;upper=[float('-inf')]*3
    vol=0.0;max_error=0.0
    for i in range(n):
        row=struct.unpack_from('<12fH',buf,84+i*50)
        nx,ny,nz=row[:3]
        a=row[3:6];b=row[6:9];c=row[9:12]
        if not all(math.isfinite(x) for x in row[:12]):raise ValueError('nonfinite facet')
        cross=((b[1]-a[1])*(c[2]-a[2])-(b[2]-a[2])*(c[1]-a[1]),
               (b[2]-a[2])*(c[0]-a[0])-(b[0]-a[0])*(c[2]-a[2]),
               (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
        length=math.sqrt(sum(x*x for x in cross))
        if length<1e-6:raise ValueError(f'degenerate triangle {i}')
        dot=(nx*cross[0]+ny*cross[1]+nz*cross[2])/length
        if dot<.99:raise ValueError('face normal inconsistent with triangle')
        max_error=max(max_error,abs(1.0-dot))
        for point in (a,b,c):
            for k in range(3):lower[k]=min(lower[k],point[k]);upper[k]=max(upper[k],point[k])
        # 1-micron vertex-merge threshold: handles floating-point seams.
        v=[tuple(round(x,3) for x in p) for p in (a,b,c)]
        if len(set(v))!=3:raise ValueError('collapsed triangle at tolerance')
        vertices.update(v)
        for j,k in ((0,1),(1,2),(2,0)):
            edges[tuple(sorted((v[j],v[k])))]+=1
        vol+=(a[0]*(b[1]*c[2]-b[2]*c[1])+a[1]*(b[2]*c[0]-b[0]*c[2])+a[2]*(b[0]*c[1]-b[1]*c[0]))/6
    nonmanifold=[(edge,c) for edge,c in edges.items() if c!=2]
    if nonmanifold:raise ValueError(f'mesh not watertight by edge adjacency: {nonmanifold[:2]}')
    extents=[b-a for a,b in zip(lower,upper)]
    if any(abs(actual-expected)>tol_mm for actual,expected in zip(extents,expected_extents)):
        raise ValueError(f'mesh bounds differ from intended envelope: {extents} versus {expected_extents}')
    if vol<=1:raise ValueError(f'nonpositive or implausible solid volume {vol}')
    return {'schema':'atlas.offline-print-mesh-audit/1','result':'passed_digital_geometry_only',
        'file':path.name,'bytes':len(buf),'sha256':hashlib.sha256(buf).hexdigest(),
        'triangles':n,'vertices_merged_0_001_mm':len(vertices),
        'unique_edges':len(edges),'all_edges_have_two_incident_faces':True,
        'outward_face_normals_verified':True,'signed_volume_mm3':round(vol,3),
        'bounds_mm':[[round(v,4) for v in lower],[round(v,4) for v in upper]],
        'extents_mm':[round(v,4) for v in extents],
        'slicer_gcode_generated':False,'physical_print_tested':False,'fit_measured':False}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('stl',type=Path)
    p.add_argument('--width',type=float,default=40)
    p.add_argument('--height',type=float,default=33)
    p.add_argument('--out',type=Path)
    a=p.parse_args()
    r=verify_stl(a.stl,(a.width,a.width,a.height))
    if a.out:
        a.out.parent.mkdir(exist_ok=True,parents=True)
        a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__':main()
