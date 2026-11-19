"""Construct versioned Atlas records from original chapters; preserves old nodes.

Run with: python evidence/build_records.py /path/to/extracted/federation
"""
import sys, json, hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('usage: build_records.py /full/federation/root')
F=Path(sys.argv[1]).resolve()
sys.path.insert(0,str(F/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import seal,write_node,canonical,sha,validate_relation
from build_chapters import CHAPTERS,SOURCES,NODE,DATE

# These are exact prior record identities, not new copies or guessed latest revisions.
DEPENDENCY_IDS={
 'agent-atlas':'agent-atlas:action-observation',
 'software-design-patterns-atlas':'software-design-patterns-atlas:chapter-02-concept',
 'distributed-systems-atlas':'distributed-systems-atlas:chapter-01-concept',
 'computation-atlas':'computation-atlas:chapter-05-concept',
 'mathematics-physics-atlas':'mathematics-physics-atlas:chapter-01-concept',
 'measurement-atlas':'measurement-atlas:concept:certificate-structure-not-authenticity',
 'computer-architecture-digital-hardware-atlas':'computer-architecture-digital-hardware-atlas:chapter-04-concept',
 'electronics-semiconductors-atlas':'electronics-semiconductors-atlas:chapter-01-concept',
 'language-atlas':'language-atlas:chapter-01-concept',
 'neural-architectures-atlas':'neural-architectures-atlas:chapter-01-concept',
}
external={}
for nid,rid in DEPENDENCY_IDS.items():
    p=F/'common/nodes'/nid/'data/concepts.jsonl'
    candidate=[json.loads(line) for line in p.read_text().splitlines() if json.loads(line)['record_id']==rid]
    if len(candidate)!=1:raise ValueError('missing exact dependency '+rid)
    external[nid]={'record_id':rid,'revision':candidate[0]['revision']}

rights={'status':'local_reference','note':'Original Atlas research text only. Published source files are not redistributed or authenticated.'}
evidence_gaps=['No independent expert cryptography review','Original publisher files not byte-authenticated','No deployed-key or side-channel validation']


def make_record(kind,ident,title,text,equation,source_refs,chapter_path,scope='Reference educational software only'):
    return seal({
      'schema':'atlas.record/1','node_id':NODE,'record_id':NODE+':'+ident,'original_id':ident,
      'type':kind,'title':title,
      'content':{'text':text,'tags':['cryptographic-protocols','original-priority-14','scoped-content-v1',kind],
        'domain':'cryptographic-protocols','equation':equation,'assumptions':['Public standards as bibliographic locators','Tests use fixed inputs, not real production secrets'],
        'applicability':[scope], 'limitations':['No security certification or implementation interoperability','No real operational entropy or hardware testing'],
        'units':['bits','bytes','dimensionless probabilities and logical counts'],
        'uncertainty':['Computational assumptions, side channels, user trust-anchor acquisition and production deployment unverified']},
      'evidence':{'origin':'original_atlas_crypto_reference',
        'review_status':'finite_software_and_published_vector_check_only','locators':[],
        'gaps':evidence_gaps,'upstream_labels':{}},
      'sources':source_refs,'status':'active','rights':rights,
      'provenance':{'author':'ATLAS FORGE scientific-continuity research (AI-assisted authoring)',
        'edition_added':'1.0.0','created_at':DATE,'chapter_path':chapter_path,'external_review':False},
      'extensions':{}
    })


def make_source(key):
    title,edition,url=SOURCES[key]
    return seal({
      'schema':'atlas.record/1','node_id':NODE,'record_id':NODE+':source:'+key,'original_id':'source:'+key,
      'type':'source','title':title,
      'content':{'text':f'{title}. Edition: {edition}. Bibliographic locator: {url}. This official standards-page link is navigation only, not proof of authenticated local publisher bytes or a licensed full-text copy.',
        'tags':['cryptographic-protocols','bibliographic','official-standards-pointer'],
        'domain':'cryptographic-protocols','equation':'',
        'assumptions':['Publisher-standard bibliographic pointer only'],
        'applicability':['Locating official specifications and test vectors'],
        'limitations':['Original publisher files not independently authenticated or stored'],
        'units':['bibliographic edition identifier'],
        'uncertainty':['Standards may have errata, successors or differing implementation conformance']},
      'evidence':{'origin':'issuing_organization_bibliographic_pointer','review_status':'bibliographic_pointer_only','locators':[],
        'gaps':['Exact publisher original bytes not authenticated','Publication rights and authoritative errata not independently preserved'],'upstream_labels':{}},
      'sources':[],'status':'active','rights':rights,
      'provenance':{'author':'ATLAS FORGE scientific-continuity research (AI-assisted authoring)',
        'created_at':DATE,'edition_added':'1.0.0','publisher_url':url,'publisher_original_authenticated':False,
        'external_review':False},'extensions':{}
    })

records=[make_source(k) for k in SOURCES]
by_id={r['record_id']:r for r in records}
relations=[]

def add_relation(a,b,kind,explanation):
    rid=f'{NODE}:link-{len(relations)+1:04}:{kind}'
    relations.append(seal({'schema':'atlas.relation/1','relation_id':rid,'type':kind,
      'from':{'record_id':a['record_id'],'revision':a['revision']} if isinstance(a,dict) and 'type' in a else a,
      'to':{'record_id':b['record_id'],'revision':b['revision']} if isinstance(b,dict) and 'type' in b else b,
      'provenance':{'origin':'original_atlas_crypto_reference','scope':explanation,'independent_expert_review':False}}))

for slug,title,question,assumptions,eq,derivation,example,procedure,negative,limits,refids,deps in CHAPTERS:
    no=int(slug[:2]);pth='docs/chapters/'+slug+'.md'
    source_refs=[{'record_id':by_id[NODE+':source:'+key]['record_id'],'revision':by_id[NODE+':source:'+key]['revision']} for key in refids]
    fulltext=(HERE/pth).read_text()
    conce=make_record('concept',f'chapter-{no:02d}-concept',title+' — concept',question+'\n\n'+fulltext,'',source_refs,pth)
    claim=make_record('claim',f'chapter-{no:02d}-claim',title+' — bounded claim',assumptions+'\n\nNegative control: '+negative+'\n\nLimitations: '+limits,'',source_refs,pth)
    equat=make_record('equation',f'chapter-{no:02d}-equation',title+' — formal relation',derivation+'\n\nConstructed investigation: '+example,eq,source_refs,pth)
    meth=make_record('method',f'chapter-{no:02d}-method',title+' — offline procedure',procedure+'\n\nFailure to avoid: '+negative,'',source_refs,pth)
    records.extend([conce,claim,equat,meth])
    src=by_id[NODE+':source:'+refids[0]]
    add_relation(src,conce,'related_to','Source card is a bibliographic pointer; no publisher original authenticated')
    add_relation(conce,claim,'related_to','Concept navigation to bounded claim')
    add_relation(equat,meth,'related_to','Formal relation accompanies specified reconstruction procedure')
    add_relation(claim,meth,'qualifies','Method limits scope of claim; do not inflate to full security certification')
    for dep in deps:
        add_relation(meth,external[dep],'depends_on','Exact immutable prerequisite from previously verified Atlas node')

manifest=write_node(HERE,node_id=NODE,title='Cryptographic Protocols Atlas — scoped offline technical v1.0.0',software_version='1.0.0',
    records=records,relations=relations,scope='Offline scientific methods, standards, protocol-state reasoning and bounded authentication/integrity tests; NOT encrypted transport or vetted cryptography',
    evidence_maturity='18 original chapters, 75+ standard-library unit tests, two independent oracles and published SHA-256 HMAC/HKDF vectors; security assurance, publisher authentication and hardware tests HOLD')
(HERE/'docs/RECORD_INDEX_v1.0.0.json').write_text(json.dumps([{'record_id':r['record_id'],'revision':r['revision'],'type':r['type'],'title':r['title']} for r in records],indent=2)+'\n')
print(json.dumps({'manifest':manifest,'records':len(records),'relations':len(relations),'sources':len(SOURCES)},indent=2))
