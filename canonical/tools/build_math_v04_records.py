#!/usr/bin/env python3
"""Append versioned Mathematics & Physics v0.4 records without rewriting v0.3.

Must run on a fresh copy of the SHA-256 verified v0.3 federation. Refuses
reapplication. Original records/relations are preserved verbatim as prefixes.
"""
from pathlib import Path
import json,shutil,sys,hashlib
R=Path(__file__).resolve().parents[1];M=R/'MATHEMATICS-PHYSICS-ATLAS'
sys.path.insert(0,str(R/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import canonical,seal,sha,AtlasStore
NODE='mathematics-physics-atlas';DATE='2026-11-15';VER='0.4.0'
SOURCES={
 'ZZ-MIT-PDE':'https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/pages/readings/',
 'ZZ-SCIPY-CG':'https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html',
 'NIST-CODATA':'https://physics.nist.gov/cgi-bin/cuu/Value?ep0'
}
CHAPTERS=[
 (49,'conservative_2d_poisson_and_dielectric_flux','Conservative 2D electrostatic Poisson and harmonic dielectric flux',
  'Numerical electrostatics','ZZ-MIT-PDE',
  '-div(epsilon grad V)=rho; a_E=epsilon_face/hx^2; a_N=epsilon_face/hy^2; V has Dirichlet boundary values.',
  'poisson2d_problem(nx,ny,lx,ly,epsilon,rho,boundary): matrix-free symmetric five-point weighted Laplacian with boundary voltage into RHS.',
  'Finite 2D linear isotropic positive epsilon, rectangular Dirichlet only; no free surface-charge jumps or semiconductor carriers.',
  'epsilon F/m; rho C/m^3; x,y m; V volt; integrated flux/charge C/m'),
 (50,'matrix_free_preconditioned_conjugate_gradient','Jacobi-preconditioned conjugate gradient and true residual',
  'Sparse numerical linear algebra','ZZ-SCIPY-CG',
  'alpha_k=(r_k^T z_k)/(p_k^T A p_k); beta_k=(r_(k+1)^T z_(k+1))/(r_k^T z_k).',
  'solve_poisson2d_cg(problem,rtol,atol,maxiter): bounded matrix-free Jacobi-PCG with true residual, explicit success and nonconvergence.',
  'Requires SPD matrix and positive diagonal; residual alone does not bound continuum or model-form error.',
  'potential V; b determined by rho and boundary field units; relative residual dimensionless'),
 (51,'manufactured_solutions_discretization_and_residuals','Manufactured solutions, refinement order, independent oracles',
  'Numerical scientific verification','ZZ-MIT-PDE',
  'V*=sin(pi*x)sin(pi*y), rho*=2*pi^2*epsilon*V*; lambda_h=8*sin^2(pi*h/2)/h^2.',
  'manufactured_sine_refinement and independent NumPy dense-matrix oracle: separates solver residual from O(h^2) grid error.',
  'Artificial smooth benchmarks do not authenticate physical ε(x,y), device measurements or empirical model accuracy.',
  'x,y m; V volt; epsilon F/m; truncation potential error V'),
 (52,'dielectric_interfaces_units_and_semiconductor_handoff','Dielectric interface flux, SI provenance and semiconductor gap map',
  'Electrostatics to semiconductor science','NIST-CODATA',
  'D=epsilon E; E=-grad V; epsilon_face=2*epsilon1*epsilon2/(epsilon1+epsilon2); div D=rho.',
  'Piecewise-positive dielectric face flux and Gauss residual; explicit unmet semiconductor coupling and material calibration gates.',
  'Scalar linear epsilon is a supplied model parameter; no carrier mobility, doping transport, quantum fields, measured interface states or device predictions.',
  'epsilon0 approx 8.8541878188e-12 F/m (CODATA 2022 standard uncertainty); D C/m^2; V volt')]

def load(cat):
 return [json.loads(line) for line in (M/'data'/f'{cat}.jsonl').read_text().splitlines() if line.strip()]

def append(cat,items):
 with (M/'data'/f'{cat}.jsonl').open('ab') as f:
  for row in items:f.write(canonical(row)+b'\n')

def source_record():
 code='ZZ-SCIPY-CG';rec={
 'schema':'atlas.record/1','node_id':NODE,'record_id':f'{NODE}:source:{code}',
 'original_id':'source:'+code,'type':'source','title':'SciPy sparse.linalg.cg documentation — publisher reference only',
 'status':'active','content':{'text':'Official SciPy reference for CG requirements and stopping semantics. Bibliographic orientation only: original upstream publisher files, source authenticity/rights and independent science review were not archived.',
  'tags':['mathematics-physics','v0.4.0','source','not-authenticated-original'],
  'domain':'mathematics-physics-technological-continuity','equation':'',
  'assumptions':['The linked documentation describes an SPD conjugate-gradient API'],
  'applicability':['Software-method orientation only; independently authored Python reference is not SciPy source'],
  'limitations':['No authenticated original publisher transport bytes','No independent source-to-formula review'],
  'units':['Not applicable'],'uncertainty':['Provider pages can change; original transport not sealed']},
 'evidence':{'origin':'publisher_navigation_not_original_transport','review_status':'AI-assisted_source_orientation_not_peer_reviewed',
  'locators':[],'gaps':['Original publisher file not archived','Rights and independently signed source review pending'],
  'upstream_labels':{}},'sources':[],
 'rights':{'status':'local_reference','note':'Original bibliographic card; publisher files not retained or redistributed'},
 'provenance':{'author':'James Paul Jackson ATLAS FORGE program, AI-assisted bibliographic synthesis',
  'edition_added':VER,'created_at':DATE,'publisher_url':SOURCES[code],
  'primary_source_bytes_archived':False,'independent_review':False},'extensions':{}}
 return seal(rec)

def chapter_record(ch,kind,source):
 num,slug,title,domain,source_key,equation,method,limits,units=ch
 full=(M/'docs/chapters'/f'{num}_{slug}.md').read_text()
 text=full if kind=='concept' else (limits+'\n'+full[0:2200] if kind=='claim' else
  equation+'\n'+full[0:2500] if kind=='equation' else method+'\n'+full[-2200:])
 record={'schema':'atlas.record/1','node_id':NODE,
  'record_id':f'{NODE}:chapter-{num}-{kind}','original_id':f'chapter-{num}-{kind}',
  'type':kind,'title':title+{'concept':' — reconstruction chapter','claim':' — limitations and counterexamples',
  'equation':' — governing equations','method':' — runnable reference procedure'}[kind],
  'status':'active','content':{'text':text,'tags':['mathematics-physics','v0.4.0',kind,f'chapter-{num}',slug],
  'domain':'mathematics-physics-technological-continuity / '+domain,
  'equation':equation if kind in ('equation','method') else '',
  'assumptions':['Finite rectangular Dirichlet domain','Prescribed strictly positive isotropic linear dielectric; smoothness where derivatives invoked'],
  'applicability':['Offline reconstruction and bounded independent numerical verification'],
  'limitations':[limits,'Constructed software checks do not certify measured physics, industrial devices, or AI model improvement'],
  'units':[units],
  'uncertainty':['Discretization and roundoff distinguished from material/measurement uncertainties','Original publisher files not authenticated']},
  'evidence':{'origin':'original_bounded_scientific_educational_synthesis',
  'review_status':'AI-assisted_original_not_independently_science_peer_reviewed',
  'locators':[{'source_id':source['record_id'],'locator':SOURCES[source_key],
       'inspected_scope':'Official source page orientation; no publisher primary files imported',
       'checked_at':DATE,'checker':'AI-assisted page orientation; no signed expert review'}],
  'gaps':['No authenticated publisher source transport','No calibrated laboratory experiment','No independent scientific review'],
  'upstream_labels':{}},
  'sources':[{'record_id':source['record_id'],'revision':source['revision']}],
  'rights':{'status':'local_reference','note':'Original v0.4 scientific explanation; linked external publishers are not locally mirrored'},
  'provenance':{'author':'James Paul Jackson ATLAS FORGE program, AI-assisted original explanatory manuscript',
       'created_at':DATE,'edition_added':VER,'independent_review':False,
       'source_chapter_file':f'docs/chapters/{num}_{slug}.md',
       'numeric_evidence':'Independent constructed NumPy dense/analytic checks, not physical instruments'},
  'extensions':{}}
 return seal(record)

def relation(i,kind,f,t):
 return seal({'schema':'atlas.relation/1','relation_id':f'{NODE}:v04-{i:04d}:{kind}',
    'type':kind,'from':{'record_id':f['record_id'],'revision':f['revision']},
    'to':{'record_id':t['record_id'],'revision':t['revision']},
    'provenance':{'origin':'authored_mathematical_prerequisite_and_source_link',
       'independent_review':False,'scope':'Typed navigation/evidence relation, not independent scientific proof'}})

def refresh_manifest(node):
 manifest_path=node/'atlas_manifest.json';prior=json.loads(manifest_path.read_text())
 collections={}
 for kind,entry in prior['collections'].items():
  content=(node/entry['path']).read_bytes()
  collections[kind]={'path':entry['path'],'records':sum(bool(s.strip()) for s in content.splitlines()),'sha256':sha(content)}
 prior.update(collections=collections,software_version=VER,corpus_revision=sha(canonical(collections)),
  evidence_maturity='52 original chapters, 38 constructed cases; v0.4 tested linear 2D electrostatics/PCG on synthetic grids; 0 experiments, authenticated publisher transport files or independent expert peer reviews')
 manifest_path.write_bytes(canonical(prior)+b'\n')

def refresh_registry(root):
 p=root/'registry.json';reg=json.loads(p.read_text())
 for entry in reg['nodes']:
  if entry['node_id']==NODE: entry['manifest_sha256']=sha((root/entry['manifest']).read_bytes())
 raw=canonical(reg)+b'\n';p.write_bytes(raw)
 (root/'registry.lock.json').write_bytes(canonical({'schema':'atlas.registry-lock/1','sha256':sha(raw)})+b'\n')

def main():
 old=R/'history/math_physics_v0.3.0_test_snapshot/MATHEMATICS-PHYSICS-ATLAS/data'
 for cat in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
  assert (M/'data'/f'{cat}.jsonl').read_bytes()==(old/f'{cat}.jsonl').read_bytes(),f'v03 baseline differs: {cat}'
 lookup={rec['record_id']:rec for cat in ('concepts','claims','equations','methods','datasets','reviews','sources') for rec in load(cat)}
 if f'{NODE}:chapter-49-concept' in lookup:raise SystemExit('Refuse duplicate v0.4 append')
 new_source=source_record();lookup[new_source['record_id']]=new_source;append('sources',[new_source])
 by_kind={k:[] for k in ('concept','claim','equation','method')};rels=[];count=0
 for ch in CHAPTERS:
  source=lookup[f'{NODE}:source:{ch[4]}']
  recs={k:chapter_record(ch,k,source) for k in by_kind}
  for kind,record in recs.items():by_kind[kind].append(record);lookup[record['record_id']]=record
  for kind,f,t in [('supports',source,recs['concept']),('depends_on',recs['equation'],recs['concept']),
                   ('depends_on',recs['method'],recs['equation']),('qualifies',recs['claim'],recs['method'])]:
   count+=1;rels.append(relation(count,kind,f,t))
 for kind,records in by_kind.items():append(kind+'s',records)
 append('relations',rels)
 for cat in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
  assert (M/'data'/f'{cat}.jsonl').read_bytes().startswith((old/f'{cat}.jsonl').read_bytes()),cat
 # Local resources EXACTLY match the updated standalone content.
 local=M/'math_physics_atlas/resources/common';L=local/'nodes'/NODE
 for cat in ('concepts','claims','equations','methods','datasets','reviews','sources','relations'):
  shutil.copy2(M/'data'/f'{cat}.jsonl',L/'data'/f'{cat}.jsonl')
 refresh_manifest(M);shutil.copy2(M/'atlas_manifest.json',L/'atlas_manifest.json');refresh_registry(local)
 # The old eight cross-node links remain untouched; append only new local edges.
 F=R/'common/nodes'/NODE
 for cat in ('concepts','claims','equations','methods','datasets','reviews','sources'):
  shutil.copy2(M/'data'/f'{cat}.jsonl',F/'data'/f'{cat}.jsonl')
 with (F/'data/relations.jsonl').open('ab') as f:
  for rel in rels:f.write(canonical(rel)+b'\n')
 refresh_manifest(F);refresh_registry(R/'common')
 index=M/'evidence/chapter_index.json';prev=json.loads(index.read_text())
 for idx,slug,title,domain,key,*_ in CHAPTERS:
  prev.append({'id':f'chapter-{idx}','title':title,'domain':domain,'file':f'{idx}_{slug}.md','sources':[key]})
 index.write_text(json.dumps(prev,ensure_ascii=False,indent=2)+'\n')
 loc=AtlasStore(local).discover();fed=AtlasStore(R/'common').discover()
 assert (loc['records'],loc['relations'])==(224,208)
 assert (fed['records'],fed['relations'],len(fed['nodes']))==(2581,1735,12)
 print(json.dumps({'result':'passed','local_records':loc['records'],'local_relations':loc['relations'],
  'full_records':fed['records'],'full_relations':fed['relations'],'source_cards_total':501,
  'added_records':17,'added_relations':16,'original_data_byte_prefix_preserved':True,
  'original_30_domain_queue_modified':False,'Bitwork_router_modified':False},indent=2))

if __name__=='__main__':main()
