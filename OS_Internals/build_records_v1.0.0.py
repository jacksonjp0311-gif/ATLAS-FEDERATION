"""Register original OS Internals authored chapters as a new canonical federation node.
Usage: python evidence/build_records.py /exact/working/atlas/root
"""
from __future__ import annotations
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('usage: build_records.py /original/atlas/federation/root')
F=Path(sys.argv[1]).resolve()
sys.path.insert(0,str(F/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import seal,write_node
from build_chapters import CHAPTERS,SOURCES,NODE,DATE

# Only explicitly verified, registered predecessor records qualify as dependencies.
DEPENDENCY_IDS={
 'measurement-atlas':'measurement-atlas:concept:calibration-not-precision-fix',
 'mathematics-physics-atlas':'mathematics-physics-atlas:chapter-01-concept',
 'computer-architecture-digital-hardware-atlas':'computer-architecture-digital-hardware-atlas:chapter-01-concept',
 'software-design-patterns-atlas':'software-design-patterns-atlas:chapter-01-concept',
 'cryptographic-protocols-atlas':'cryptographic-protocols-atlas:chapter-01-concept',
 'distributed-systems-atlas':'distributed-systems-atlas:chapter-01-concept',
 'manufacturing-atlas':'manufacturing-atlas:chapter-01-concept',
 'control-atlas':'control-atlas:actuation-knowledge-boundary',
 'materials-atlas':'materials-atlas:bonding-family',
 'electronics-semiconductors-atlas':'electronics-semiconductors-atlas:chapter-01-concept',
 'computation-atlas':'computation-atlas:chapter-01-concept',
}
# Unregistered future domain is an unresolved dependency, not an invented edge.
FUTURE_DEPENDENCIES={'formal-verification-atlas'}
exact={}
for node,rid in DEPENDENCY_IDS.items():
    p=F/'common/nodes'/node/'data/concepts.jsonl'
    hits=[obj for line in p.read_text().splitlines() if (obj:=json.loads(line))['record_id']==rid]
    if len(hits)!=1:raise ValueError('missing exact prior scientific record: '+rid)
    exact[node]={'record_id':rid,'revision':hits[0]['revision']}

rights={'status':'local_reference','note':'Original AI-assisted ATLAS FORGE research prose; authoritative source publisher originals not copied or authenticated.'}
gaps=['No independent expert OS review or scientific replication', 'Publisher original bytes not authenticated', 'No real kernel, device, firmware, power-loss or target machine testing']

def record(kind,ident,title,content,eq='',sources=(),chapter='',status='finite_software_reference_only'):
    return seal({'schema':'atlas.record/1','node_id':NODE,'record_id':NODE+':'+ident,'original_id':ident,'type':kind,'title':title,
        'content':{'text':content,'tags':['os-internals','priority-15','scoped-v1-reference',kind], 'domain':'os-internals','equation':eq,
           'assumptions':['All executable components are bounded, constructed pure-Python educational models','Platform ABI and hardware conformance untested'],
           'applicability':['Offline reconstruction and finite test reference, not a bootable OS'],
           'limitations':['No real kernel implementation, device behavior or security certification','No physical crash or scheduling measurements'],
           'units':['bytes','pages','ticks','dimensionless probabilities and logical counts'],
           'uncertainty':['Hardware timing, physical write persistence, supplier firmware, real CPU ABI and peer review unverified']},
        'evidence':{'origin':'original_atlas_os_internals_scoped_reference', 'review_status':status,'locators':[], 'gaps':gaps,'upstream_labels':{}},
        'sources':list(sources), 'status':'active','rights':rights,
        'provenance':{'author':'ATLAS FORGE scientific continuity (AI-assisted)', 'edition_added':'1.0.0','created_at':DATE,'chapter_path':chapter,'independent_expert_review':False},
        'extensions':{}})

sources_by_key={}
for key,(title,edition,url) in SOURCES.items():
    r=record('source','source:'+key,title,f'Bibliographic pointer: {title}; edition/date: {edition}; link: {url}. This identifies a research source but its original publisher bytes have not been authenticated. Its content is not redistributed.',status='bibliographic_pointer_only')
    r['provenance']['publisher_url']=url
    r['provenance']['publisher_original_authenticated']=False
    # Recalculate immutable revision once metadata is in place.
    r=seal({k:v for k,v in r.items() if k!='revision'})
    sources_by_key[key]=r

records=list(sources_by_key.values());relations=[]
def ref(r):return {'record_id':r['record_id'],'revision':r['revision']}
def edge(a,b,kind,why):
    relations.append(seal({'schema':'atlas.relation/1','relation_id':f'{NODE}:rel-{len(relations)+1:04d}:{kind}',
     'type':kind,'from':ref(a) if isinstance(a,dict) and 'node_id' in a else a,
     'to':ref(b) if isinstance(b,dict) and 'node_id' in b else b,
     'provenance':{'origin':'atlas_os_internals_exact_revision','scope':why,'external_expert_review':False}}))

for c in CHAPTERS:
    index=int(c['slug'][:2]);path='docs/chapters/'+c['slug']+'.md'
    source_refs=[ref(sources_by_key[k]) for k in c['sources']]
    body=(HERE/path).read_text()
    concept=record('concept',f'chapter-{index:02}-concept',c['title']+' — full technical concept',c['question']+'\n\n'+body,sources=source_refs,chapter=path)
    claim=record('claim',f'chapter-{index:02}-claim',c['title']+' — qualified claim',c['assumptions']+'\n\nNegative control: '+c['negative']+'\n\nScientific hold: '+c['limits'],sources=source_refs,chapter=path)
    equation=record('equation',f'chapter-{index:02}-equation',c['title']+' — governing invariant',c['derivation']+'\n\nConstructed numeric case: '+c['example'],eq=c['equation'],sources=source_refs,chapter=path)
    method=record('method',f'chapter-{index:02}-method',c['title']+' — offline reproducible procedure',c['procedure']+'\n\nRejection case: '+c['negative']+'\n\nLimits: '+c['limits'],sources=source_refs,chapter=path)
    dataset=record('dataset',f'chapter-{index:02}-constructed-case',c['title']+' — constructed test case',c['example']+'\n\nConstructed educational example, not a laboratory measurement or independently collected dataset.',sources=source_refs,chapter=path,status='constructed_example_not_experimental_data')
    records.extend([concept,claim,equation,method,dataset])
    edge(sources_by_key[c['sources'][0]],concept,'related_to','Bibliographic navigation only; not authenticated publisher evidence')
    edge(concept,claim,'related_to','Qualified claim about the bounded model')
    edge(claim,method,'qualifies','Claim assumptions and limitations accompany procedure')
    edge(equation,method,'related_to','Equation is interpreted only under method assumptions')
    edge(dataset,method,'related_to','Constructed numeric case is input to method, not measured data')
    for dep in c['deps']:
        if dep in FUTURE_DEPENDENCIES:continue
        if dep not in exact:raise ValueError('unregistered dependency: '+dep)
        edge(method,exact[dep],'depends_on','Exact immutable registered prerequisite; content support is scoped')

manifest=write_node(HERE,node_id=NODE,title='OS Internals Atlas — scoped offline technical reference v1.0.0',software_version='1.0.0',
    records=records,relations=relations,scope='Bounded OS models: virtual memory, schedulers, paging, allocation, deadlock, crash-prefix logging, handles and ELF parsing; NOT a bootable kernel',
    evidence_maturity='22 original technical chapters, independent finite software oracles, hardware and source authentication HOLD')
(HERE/'docs/RECORD_INDEX_v1.0.0.json').write_text(json.dumps([{'record_id':r['record_id'],'revision':r['revision'],'type':r['type'],'title':r['title']} for r in records],indent=2)+'\n')
print(json.dumps({'node_id':NODE,'records':len(records),'relations':len(relations),'source_cards':len(SOURCES),'corpus_revision':manifest['corpus_revision']},indent=2))
