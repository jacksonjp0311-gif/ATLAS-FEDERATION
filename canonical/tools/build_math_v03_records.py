#!/usr/bin/env python3
"""ATLAS FORGE v0.3.0 additive science records and contract regeneration.

Run exactly once on a verified v0.2.0 restored collection in a NEW workspace;
never overwrite a historical release. Uses canonical revision hashing and appends
records, retaining old revisioned records and relations as literal byte prefixes.
"""
from pathlib import Path
import hashlib,json,sys,shutil
R=Path(__file__).resolve().parents[1]
M=R/'MATHEMATICS-PHYSICS-ATLAS'
sys.path.insert(0,str(R/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import canonical,seal,sha,revision,AtlasStore
NODE='mathematics-physics-atlas';TODAY='2026-11-15'
CHAPTERS=[
(45,'rectangular_svd_one_sided_jacobi_and_rank','Rectangular singular-value decomposition and rank-aware numerical diagnosis','Linear algebra','ZZ-LAPACK',
'A=U Σ Vᵀ; columns satisfy A v_i=σ_i u_i; κ₂(A)=σ₁/σᵣ for full numerical rank.',
'jacobi_svd(matrix): scaled one-sided Jacobi rotations, thin reconstruction and rank threshold; finite 32×32 real matrices only.',
'Numerical rank depends on the user-specified singular-value cutoff. Near-zero singular modes and nullspace vectors are not universally identifiable.',
'dimensionless real matrices; singular values inherit matrix coefficient units; conditioning is dimensionless'),
(46,'pseudoinverse_least_squares_identifiability','SVD pseudoinverse, minimum norm and scientific identifiability','Inverse problems','ZZ-LAPACK',
'argminₓ ||Ax−b||₂; A⁺_τ b=Σ_{σᵢ>τσ₁} vᵢ(uᵢᵀb)/σᵢ; ∇½||Ax−b||²=Aᵀ(Ax−b).',
'svd_least_squares(A,b): thresholded minimum-norm solution with explicit numerical rank, residual and cutoff.',
'Rank-deficient inverse solutions are non-unique, and a small fit residual is not evidence of a unique physical parameter.',
'right-hand-side units b; parameter units depend on chosen matrix scaling and parameter definitions'),
(47,'poisson_electrostatics_finite_difference_gauss_law','Electrostatic Poisson equation, Gauss balance and Dirichlet reconstruction','Electrostatics','ZZ-MIT-PDE',
'-ε d²V/dx²=ρ; -Vᵢ₋₁+2Vᵢ−Vᵢ₊₁=ρᵢ Δx²/ε; D_right−D_left=Δx Σρᵢ.',
'poisson1d_dirichlet(rho,epsilon,L,V_left,V_right): O(N) tridiagonal solution, E-field and Gauss residual.',
'Only a 1D constant linear dielectric is modeled; semiconductor drift-diffusion, carrier statistics, interfaces and measured material properties are absent.',
'ε F/m; ρ C/m³; L m; V volt; E V/m; D C/m²'),
(48,'implicit_diffusion_stability_and_temporal_resolution','Backward Euler and Crank–Nicolson diffusion, stability versus physical accuracy','Numerical PDE','ZZ-MIT-PDE',
'u_t=αu_xx; BE: (1+2r)uⁿ⁺¹ᵢ−r(uⁿ⁺¹ᵢ₋₁+uⁿ⁺¹ᵢ₊₁)=uⁿᵢ; r=αΔt/Δx².',
'implicit_heat1d_dirichlet(initial,alpha,dx,dt,steps,method): tridiagonal backward Euler/CN, fixed Dirichlet edges.',
'CN linear stability does not guarantee nonoscillation or step accuracy; 1D constant diffusivity cannot certify real heat conduction.',
'α m²/s; dx m; dt s; u arbitrary heat/diffusion unit; r dimensionless')]

SOURCES=[
('ZZ-LAPACK','Netlib LAPACK DGESVD — authoritative routine specification; navigation only',
 'https://www.netlib.org/lapack/explore-html/d1/d7f/group__gesvd_gac6bd5d4e645049e49bb70691180abf07.html',
 'Official LAPACK real m-by-n singular value decomposition routine, factor shapes, ordering; no code/data transferred or authenticated'),
('ZZ-MIT-PDE','MIT OCW 18.336 numerical partial differential equations lecture index; navigation only',
 'https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/pages/lecture-notes/',
 'Publisher course index with Poisson, elliptic finite-difference, heat and ODE numerical-analysis topics; published PDFs not imported or hashed')]

def load(category):
    p=M/'data'/f'{category}.jsonl'
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]

def append(category,arr):
    path=M/'data'/f'{category}.jsonl'
    with path.open('ab') as f:
        for x in arr:f.write(canonical(x)+b'\n')

def source_record(code,title,url,scope):
    rec={'schema':'atlas.record/1','node_id':NODE,'record_id':f'{NODE}:source:{code}',
     'original_id':f'source:{code}','type':'source','title':title,'status':'active',
     'content':{'text':scope+' Source orientation only; official public page manually located. Original publisher bytes, retrieval receipt, license clearance, and peer review not archived.',
                'tags':['math-physics-v0.3.0','source','publisher-navigation','not-authenticated'],
                'domain':'mathematics-physics-technological-continuity','equation':'',
                'assumptions':['Only published source page existence is represented'],
                'applicability':['Bibliographic orientation and topics, not reproduced evidence'],
                'limitations':['Not original publisher transport bytes','No independent source-to-formula review'],
                'units':['Not applicable'],
                'uncertainty':['Licensing of offline source redistribution not independently verified']},
     'evidence':{'origin':'publisher_navigation_not_original_transport',
                 'review_status':'AI-assisted_bibliographic_orientation_not_peer_reviewed',
                 'locators':[],'gaps':['No authenticated publisher document','No independent expert review'],
                 'upstream_labels':{}},'sources':[],
     'rights':{'status':'local_reference','note':'This original bibliographic record is local; publisher document redistribution not authorized by this record'},
     'provenance':{'author':'James Paul Jackson ATLAS FORGE program, AI-assisted original synthesis',
                   'created_at':TODAY,'edition_added':'0.3.0','independent_review':False,
                   'primary_source_bytes_archived':False,'publisher_url':url,'source_scope':scope,
                   'rights_scope':'Reference URL only; no third-party source files retained'},'extensions':{}}
    return seal(rec)

def chapter_record(chapter,kind,sourceref):
    idx,slug,title,domain,source_id,equation,method,lim,units=chapter
    full=(M/'docs/chapters'/f'{idx}_{slug}.md').read_text()
    if kind=='concept':msg=full
    elif kind=='claim':msg=lim+' The chapter provides counterexamples and exact scope limits; computed checks are not field evidence.'
    elif kind=='equation':msg=equation+'\n'+full[0:2600]
    else:msg=method+'\n'+full[-1800:]
    rec={'schema':'atlas.record/1','node_id':NODE,'record_id':f'{NODE}:chapter-{idx}-{kind}',
    'original_id':f'chapter-{idx}-{kind}','type':kind,
    'title':title+{'concept':' — reconstruction chapter','equation':' — equation','claim':' — counterexample and limitations','method':' — numerical method'}[kind],
    'status':'active',
    'content':{'text':msg,'tags':['math-physics-v0.3.0',kind,f'chapter-{idx}',slug],
       'domain':f'mathematics-physics-technological-continuity / {domain}',
       'equation':equation if kind in ('equation','method') else '',
       'assumptions':['Stated smoothness/finite domains and boundary conditions in the original chapter','Nonlinear constitutive physics requires separate models'],
       'applicability':['Offline reconstruction and bounded scientific numerical reference, not operational device validation'],
       'limitations':[lim,'Software tests do not establish calibrated physical measurements or independent scientific acceptance'],
       'units':[units],
       'uncertainty':['Numerical truncation/roundoff, model-form uncertainty and source integrity handled separately','No authenticated original publisher document bytes']},
    'evidence':{'origin':'original_bounded_scientific_educational_synthesis',
       'review_status':'AI-assisted_original_not_independently_science_peer_reviewed',
       'locators':[{'source_id':sourceref['record_id'],'locator':(next(s[2] for s in SOURCES if s[0]==source_id)),
                    'inspected_scope':'Official publisher page description, not original publisher file download',
                    'checked_at':TODAY,'checker':'AI-assisted source orientation; not authenticated publisher transport or independent science review'}],
       'gaps':['Authenticated publisher source files not retained','Real laboratory evidence absent','Independent scientific review absent'],
       'upstream_labels':{}},
    'sources':[{'record_id':sourceref['record_id'],'revision':sourceref['revision']}],
    'rights':{'status':'local_reference','note':'Original ATLAS FORGE chapter, publisher document not mirrored'},
    'provenance':{'author':'James Paul Jackson ATLAS FORGE program, AI-assisted original educational drafting',
      'created_at':TODAY,'edition_added':'0.3.0','independent_review':False,
      'source_chapter_file':f'docs/chapters/{idx}_{slug}.md','numerical_test_scope':'constructed finite problems only'},
    'extensions':{}}
    return seal(rec)

def relation(i,kind,from_rec,to_rec):
    return seal({'schema':'atlas.relation/1','relation_id':f'{NODE}:v03-{i:04d}:{kind}',
     'type':kind,'from':{'record_id':from_rec['record_id'],'revision':from_rec['revision']},
     'to':{'record_id':to_rec['record_id'],'revision':to_rec['revision']},
     'provenance':{'origin':'authored_scientific_reconstruction_dependency','independent_review':False,
      'scope':'Source link and theory relationship, not independent proof or physical verification'}})

def refresh_manifest(node,relation_type='local'):
    old=json.loads((node/'atlas_manifest.json').read_text())
    collections={}
    for key,entry in old['collections'].items():
        p=node/entry['path'];data=p.read_bytes()
        cnt=sum(bool(x.strip()) for x in data.splitlines())
        collections[key]={'path':entry['path'],'records':cnt,'sha256':sha(data)}
    old.update(collections=collections,software_version='0.3.0',
               corpus_revision=sha(canonical(collections)),
               evidence_maturity='48 original chapters, 32 constructed cases; 1300 new NumPy/analytic comparisons, 120 negative input checks; zero physical experiments, authentic publisher files or independent peer reviews')
    (node/'atlas_manifest.json').write_bytes(canonical(old)+b'\n')

def refresh_registry(root):
    p=root/'registry.json';reg=json.loads(p.read_text())
    for node in reg['nodes']:
        if node['node_id']==NODE:
            node['manifest_sha256']=sha((root/node['manifest']).read_bytes())
    raw=canonical(reg)+b'\n';p.write_bytes(raw)
    (root/'registry.lock.json').write_bytes(canonical({'schema':'atlas.registry-lock/1','sha256':sha(raw)})+b'\n')


def main():
    existing={x['record_id'] for t in ('concepts','claims','equations','methods','sources','datasets') for x in load(t)}
    if f'{NODE}:chapter-45-concept' in existing:raise SystemExit('v0.3 already present; refuse duplicate revision append')
    lookup={x['record_id']:x for t in ('concepts','claims','equations','methods','sources','datasets') for x in load(t)}
    fresh_sources=[source_record(*s) for s in SOURCES]
    for s in fresh_sources:lookup[s['record_id']]=s
    append('sources',fresh_sources)
    by_kind={x:[] for x in ('concept','claim','equation','method')}
    added_rel=[];rel_index=0
    for ch in CHAPTERS:
        sr=lookup[f'{NODE}:source:{ch[4]}']
        recs={t:chapter_record(ch,t,sr) for t in by_kind}
        for kind,v in recs.items():by_kind[kind].append(v);lookup[v['record_id']]=v
        for type_,from_,to_ in [('supports',sr,recs['concept']),('depends_on',recs['equation'],recs['concept']),
                                ('depends_on',recs['method'],recs['equation']),('qualifies',recs['claim'],recs['method'])]:
            rel_index+=1;added_rel.append(relation(rel_index,type_,from_,to_))
    for kind,recs in by_kind.items():append(kind+'s',recs)
    append('relations',added_rel)
    # One node's local resources: exact same collection bytes, local 16-edge extension.
    local=M/'math_physics_atlas/resources/common'
    for name in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
        shutil.copy2(M/'data'/f'{name}.jsonl',local/'nodes'/NODE/'data'/f'{name}.jsonl')
    refresh_manifest(M)
    shutil.copy2(M/'atlas_manifest.json',local/'nodes'/NODE/'atlas_manifest.json')
    refresh_registry(local)
    # Full federation copy retains eight older qualified cross-node relationships.
    full=R/'common/nodes'/NODE
    for name in ('concepts','claims','equations','methods','datasets','reviews','sources'):
        shutil.copy2(M/'data'/f'{name}.jsonl',full/'data'/f'{name}.jsonl')
    with (full/'data/relations.jsonl').open('ab') as f:
        for row in added_rel:f.write(canonical(row)+b'\n')
    refresh_manifest(full)
    refresh_registry(R/'common')
    # Monotone chapter catalog; first 38 existing entries were not rewritten.
    index=M/'evidence/chapter_index.json';prev=json.loads(index.read_text())
    for i in range(39,45):
        slug=next(p.name for p in (M/'docs/chapters').glob(f'{i}_*.md'))
        prev.append({'id':f'chapter-{i}','title':slug.removesuffix('.md').replace('_',' ').strip(),
                     'domain':'Numerical methods','file':slug,'sources':['MIT-NUMERICAL-METHODS']})
    for i,slug,title,domain,src,*_ in CHAPTERS:
        prev.append({'id':f'chapter-{i}','title':title,'domain':domain,'file':f'{i}_{slug}.md','sources':[src]})
    index.write_text(json.dumps(prev,ensure_ascii=False,indent=2)+'\n')
    # Assert old exact record-revision and relation prefix preserved, then load both stores.
    before=R/'history/math_physics_v0.2.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
    for name in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
        assert (M/'data'/f'{name}.jsonl').read_bytes().startswith((before/f'{name}.jsonl').read_bytes()),name
    loc=AtlasStore(local).discover();fed=AtlasStore(R/'common').discover()
    assert (loc['records'],loc['relations'])==(207,192),(loc['records'],loc['relations'])
    assert (fed['records'],fed['relations'],len(fed['nodes']))==(2564,1719,12)
    print(json.dumps({'local_records':loc['records'],'local_relations':loc['relations'],
        'federation_records':fed['records'],'federation_relations':fed['relations'],'nodes':len(fed['nodes']),
        'added_records':18,'added_relations':16,'historical_prefix_preserved':True},indent=2))
if __name__=='__main__':main()
