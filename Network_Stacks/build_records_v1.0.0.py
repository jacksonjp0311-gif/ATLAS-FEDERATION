"""Build one complete, scoped canonical Network Stacks Atlas #16 node.

Run in the original full federation, not as a second Atlas.
Versioned records use atlas.common/1 and exact immutable predecessor revision.
"""
from __future__ import annotations
import json,hashlib,sys
from pathlib import Path
from chapter_spec import CHAPTERS,SOURCES,NODE,DATE
ROOT=Path(__file__).resolve().parents[1]
F=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT.parent
sys.path.insert(0,str(F/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'))
from atlas_forge.common import seal,write_node
ANCHOR={
 'os-internals-atlas':'os-internals-atlas:chapter-17-concept',
 'software-design-patterns-atlas':'software-design-patterns-atlas:chapter-01-concept',
 'computer-architecture-digital-hardware-atlas':'computer-architecture-digital-hardware-atlas:chapter-01-concept',
 'distributed-systems-atlas':'distributed-systems-atlas:chapter-01-concept',
 'cryptographic-protocols-atlas':'cryptographic-protocols-atlas:chapter-01-concept',
 'measurement-atlas':'measurement-atlas:concept:calibration-not-precision-fix',
 'manufacturing-atlas':'manufacturing-atlas:chapter-01-concept',
 'control-atlas':'control-atlas:actuation-knowledge-boundary',
 'materials-atlas':'materials-atlas:bonding-family'
}
exact={}
for node,rid in ANCHOR.items():
    entries=(F/'common/nodes'/node/'data/concepts.jsonl').read_text().splitlines()
    hits=[x for line in entries if (x:=json.loads(line))['record_id']==rid]
    if len(hits)!=1:raise ValueError('Required exact predecessor anchor not found: '+rid)
    exact[node]={'record_id':rid,'revision':hits[0]['revision']}

def rec(kind,id,title,body,eq='',source_refs=(),chapter='',review='finite_software_reference_only'):
    return seal({'schema':'atlas.record/1','node_id':NODE,'record_id':NODE+':'+id,'original_id':id,'type':kind,'title':title,
      'content':{'text':body,'tags':['network-stacks','priority-16','scoped-v1-reference',kind], 'domain':'network-stacks', 'equation':eq,
       'assumptions':['Python 3 standard-library finite models; no physical wire tests','Subset parsers intentionally abstain on unsupported framing and protocol states'],
       'applicability':['Offline technical explanation and finite reference calculation'],
       'limitations':['Not an interoperable TCP/IP stack or a TLS implementation','No real NIC/PHY captures or authenticated publisher originals'],
       'units':['bytes','bits','seconds','packets','dimensionless logical counts'],
       'uncertainty':['Network timing, offload behavior, clock accuracy and security not independently tested']},
      'evidence':{'origin':'original_atlas_network_stacks_scoped_v1_reference',
       'review_status':review,'locators':[],
       'gaps':['No independent external protocol expert review','No authenticated local publisher original files','No physical network interoperability or security acceptance'],
       'upstream_labels':{}},
      'sources':list(source_refs),'status':'active',
      'rights':{'status':'local_reference','note':'Original research prose and code; official RFC bibliographic links only, source publisher bytes not copied/authenticated.'},
      'provenance':{'author':'ATLAS FORGE AI-assisted scientific continuity','edition_added':'1.0.0','created_at':DATE,'chapter_path':chapter,
       'independent_expert_review':False,'unsealed_prior_source':'Network Stacks v0.1.0 working reference','source_material_reuse':'qualified original technical content'},'extensions':{}})

def ref(r):return {'record_id':r['record_id'],'revision':r['revision']}
sources={}
for id,(title,edition,url) in SOURCES.items():
    s=rec('source','source:'+id,title,f'Bibliographic source pointer for offline provenance: {title}; edition {edition}; official locator {url}. Publisher original binary/text content is not locally authenticated. Check RFC obsoletions, updates and errata.',review='bibliographic_locator_not_authenticated')
    s['provenance']['publisher_url']=url
    s['provenance']['publisher_original_authenticated']=False
    sources[id]=seal({k:v for k,v in s.items() if k!='revision'})
records=list(sources.values());relationships=[];index=[]
def edge(a,b,kind,why):
    relationships.append(seal({'schema':'atlas.relation/1','relation_id':f'{NODE}:rel-{len(relationships)+1:04d}:{kind}',
       'type':kind,'from':ref(a) if isinstance(a,dict) and 'node_id' in a else a,
       'to':ref(b) if isinstance(b,dict) and 'node_id' in b else b,
       'provenance':{'origin':'atlas_network_stacks_exact_revision','scope':why,'expert_review':False}}))

chapterdir=ROOT/'docs/chapters';chapterdir.mkdir(parents=True,exist_ok=True)
manual=['# ATLAS FORGE — Network Stacks Atlas · scoped scientific reference v1.0.0','',
 'Original canonical domain #16. This is ONE federation and extends OS Internals v1.0.0.','',
 'This manual documents reconstructible algorithms, assumptions, negative controls, sources and limits.','',
 '**Scope boundary:** validated local numerical software models, not a production TCP/IP stack, authenticated network service, TLS library, or physical engineering acceptance.','']
for idx,(slug,title,q,assumptions,derivation,eq,example,procedure,negative,limits,keys,deps) in enumerate(CHAPTERS,1):
    path=f'docs/chapters/{idx:02d}_{slug}.md'
    chapter=(f'# {idx:02d} — {title}\n\n'
      f'**Scientific question.** {q}\n\n'
      f'## Definitions, physical assumptions and scope\n\n{assumptions}\n\n'
      f'## Governing principle and derivation\n\n{derivation}\n\n'
      f'**Equation / invariant:** `{eq}`. Do not apply outside the stated assumptions.\n\n'
      f'## Worked construction (not experimental data)\n\n{example}\n\n'
      f'## Reconstructible offline procedure\n\n{procedure}\n\n'
      f'## Independent test or negative control\n\n{negative}\n\n'
      f'## Known failures, uncertainty and acceptance gates\n\n{limits}\n\n'
      f'## Source pointers (not authenticated publisher files)\n\n')
    for key in keys: chapter+=f'- {key}: {SOURCES[key][0]} ({SOURCES[key][1]}), {SOURCES[key][2]}\n'
    chapter+='\n**Exact predecessor dependencies:** '+', '.join(deps)+'. See immutable relation revisions in `data/relations.jsonl`.\n\n'
    (ROOT/path).write_text(chapter,encoding='utf8')
    manual.append(chapter)
    ss=[ref(sources[k]) for k in keys]
    concept=rec('concept',f'chapter-{idx:02d}-concept',title+' — definitions and full technical chapter',q+'\n\n'+chapter,source_refs=ss,chapter=path)
    claim=rec('claim',f'chapter-{idx:02d}-claim',title+' — bounded claim and explicit negative case',assumptions+'\n\nRequired negative: '+negative+'\n\nLimits: '+limits,source_refs=ss,chapter=path)
    equation=rec('equation',f'chapter-{idx:02d}-equation',title+' — equation and assumptions',derivation+'\n\nConstructed worked case: '+example,eq=eq,source_refs=ss,chapter=path)
    method=rec('method',f'chapter-{idx:02d}-method',title+' — offline reproduction and refusal conditions',procedure+'\n\nNegative control: '+negative+'\n\nLimits: '+limits,source_refs=ss,chapter=path)
    case=rec('dataset',f'chapter-{idx:02d}-constructed-case',title+' — reproducible constructed input',example+'\n\nThis is a synthetic worked construction, not field measurement or empirical observation.',source_refs=ss,chapter=path,review='constructed_case_not_measured')
    records.extend((concept,claim,equation,method,case));index.append({'chapter':idx,'title':title,'path':path,'equation':eq,'sources':keys,'dependencies':deps})
    edge(sources[keys[0]],concept,'related_to','Bibliographic navigation only; published original content not authenticated')
    edge(concept,claim,'related_to','Qualified claim under bounded assumptions')
    edge(claim,method,'qualifies','Attach limitations and negative control to method')
    edge(equation,method,'related_to','Equation is scoped to procedure and preconditions')
    edge(case,method,'related_to','Constructed example, not an observed measurement')
    for dep in deps:
        edge(method,exact[dep],'depends_on','Exact immutable predecessor scientific dependency')
(ROOT/'docs/DEPTH_MANUAL_v1.0.0.md').write_text('\n'.join(manual),encoding='utf8')
(ROOT/'docs/CHAPTER_INDEX_v1.0.0.json').write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
(ROOT/'docs/SOURCE_REGISTER_v1.0.0.md').write_text('# Network Stacks #16 — official bibliographic locators (no authenticated publisher originals)\n\n'+'\n'.join(f'- **{id}:** {title}, {edition}, {url}' for id,(title,edition,url) in SOURCES.items())+'\n',encoding='utf8')
(ROOT/'docs/SCOPED_V1_GATES_v1.0.0.md').write_text('''# Scoped Network Stacks v1.0.0 acceptance gates

| Gate | Scoped offline reference | Real-world acceptance |
|---|---|---|
| Full original chapters | Authored and indexed | Independent engineering review HOLD |
| IPv4/IPv6/UDP/DNS/QUIC subset | Finite Python tests | Full protocol conformance HOLD |
| TCP sequence window/RTO | Independent finite oracles | Complete TCP state/congestion engine HOLD |
| Checksum/pseudoheader and framing | Deterministic arithmetic/oracle | Wire captures and NIC checksum offload HOLD |
| Neighbor, routing, DNSSEC, QUIC/TLS | Research-only explanatory chapters | Interoperability, security and hardware HOLD |
| Original 30-domain queue | Byte-preserved | Unchanged historical release |
| Historical federation archive | Exact predecessor and patch | Source/fresh regression and restore receipt required |
| Publisher original authentication | Bibliographic links only | Original publisher bytes HOLD |

**Scoped software-content v1.0 readiness does not equal production network, physical, scientific-expert or security acceptance.**
''',encoding='utf8')
(ROOT/'README.md').write_text('''# ATLAS FORGE / Network Stacks Atlas — Original Domain #16

This is a **native node inside the ONE canonical ATLAS FORGE federation**; never use it as a separate Atlas or standalone substitute. Current release candidate: scoped offline scientific/software reference **v1.0.0**. Complete historical predecessor, exact revisions and original 30-domain roadmap are preserved.

- `docs/DEPTH_MANUAL_v1.0.0.md`: 22 original technical chapters, worked cases, equations and negative controls.
- `data/`: eight explicit atlas.common/1 collections, all records sealed with canonical immutable revisions.
- `net_atlas/`: dependency-minimal Python 3 reference models, deliberately bounded to supported protocol subsets.
- `tests/`, `evidence/`: unit suites, independent oracle, previous unsealed working-model comparison and build instructions.
- `docs/SCOPED_V1_GATES_v1.0.0.md`: independent scientific/wire/security HOLD register.

Run from this node folder:

```sh
PYTHONPATH=. python -m unittest discover -s tests -q
PYTHONPATH=. python evidence/independent_oracle_v1.py
PYTHONPATH=. python evidence/independent_oracle_prior.py
```

The final release only becomes canonical after full historical federation and exact fresh-restore verification and Library readback. RFC links are bibliographic pointers; they are **not** authenticated original publisher bytes. No Bitwork router or desktop transfer was changed.
''',encoding='utf8')
m=write_node(ROOT,node_id=NODE,title='Network Stacks Atlas — scoped offline scientific reference v1.0.0',software_version='1.0.0',records=records,relations=relationships,
  scope='Offline IPv4/IPv6, Ethernet/ARP, UDP checksums, TCP sequence/RTT, DNS, CIDR, QUIC numeric models; no live stack or TLS engine',
  evidence_maturity='22 source-linked original chapters; finite cross-checked Python models; wire/hardware/primary publisher/expert acceptance HOLD')
(ROOT/'docs/RECORD_INDEX_v1.0.0.json').write_text(json.dumps([{'record_id':r['record_id'],'revision':r['revision'],'type':r['type'],'title':r['title']} for r in records],indent=2)+'\n')
print(json.dumps({'node':NODE,'records':len(records),'relations':len(relationships),'sources':len(sources),'chapters':len(CHAPTERS),'manifest_corpus_revision':m['corpus_revision']},indent=2))
