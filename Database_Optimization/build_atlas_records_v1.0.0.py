"""Rebuild native canonical Database Optimization v1 scientific records.
Versions and exact predecessor revisions are immutable; the original staged
v0.1.0 source is separately archived and not replaced in the Library.
"""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NODE = 'database-optimization-atlas'

def canonical(x):
    return json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')

def with_revision(record):
    r=dict(record)
    r['revision']=hashlib.sha256(canonical(record)).hexdigest()
    return r

def mkrecord(rtype,original_id,title,text,links=None,chapter_path='',equation=''):
    base={
      'schema':'atlas.record/1', 'node_id':NODE, 'record_id':f'{NODE}:{original_id}',
      'original_id':original_id, 'title':title, 'type':rtype, 'status':'active',
      'content': {
        'text':text,'domain':'database-optimization',
        'tags':['database-optimization','original-30-priority-17','scoped-v1.0.0',rtype],
        'equation':equation,
        'assumptions':['Finite, bounded offline educational reference; no external service'],
        'applicability':['Offline reconstructible software/math demonstrations, not production database'],
        'limitations':['No physical performance measurements, storage durability or peer review',
                       'The exact canonical predecessor is Network Stacks v1.0.0; no physical evidence is implied'],
        'units':['rows','pages','bytes','abstract cost units','logical timestamps','dimensionless ratios'],
        'uncertainty':['Cost estimates are not calibrated to a DBMS or machine']},
      'evidence':{
        'origin':'original_atlas_database_optimization_canonical_scoped_v1',
        'review_status':'bibliographic_pointer_only' if rtype=='source' else 'finite_software_reference_only',
        'locators':[], 'gaps':['Original publisher bytes not authenticated','No independent scientific review',
                               'Current edition verification and restoration separately documented in release receipts'],'upstream_labels':{}},
      'rights':{'status':'local_reference','note':'Original AI-assisted ATLAS FORGE prose and code; linked documentation not reproduced.'},
      'sources': links or [],
      'provenance':{'author':'ATLAS FORGE scientific continuity (AI-assisted)',
                    'edition_added':'1.0.0','created_at':'2026-11-19',
                    'independent_expert_review':False,'chapter_path':chapter_path},
      'extensions':{}
    }
    return with_revision(base)


def relation(number, src, dst, rtype='related_to', scope='Exact-revision link; no authenticated publisher evidence'):
    return with_revision({'schema':'atlas.relation/1',
           'relation_id':f'{NODE}:rel-{number:04d}:{rtype}',
           'from':{'record_id':src['record_id'],'revision':src['revision']},
           'to':{'record_id':dst['record_id'],'revision':dst['revision']},
           'type':rtype,
           'provenance':{'origin':'atlas_database_optimization_scoped_v1_exact_revision',
                         'scope':scope,'external_expert_review':False}})


def make():
    data=ROOT/'data';data.mkdir(exist_ok=True)
    sources=json.loads((ROOT/'sources.json').read_text())['sources']
    ref_sources=[]
    for s in sources:
        rec=mkrecord('source',f"source:{s['id']}",s['title'],
            f"Official bibliography pointer: {s['organization']}; URL {s['url']}; role {s['role']}. Original bytes and rights not authenticated.")
        rec_no_rev={k:v for k,v in rec.items() if k!='revision'}
        rec_no_rev['provenance']['publisher_url']=s['url']
        rec_no_rev['provenance']['publisher_original_authenticated']=False
        ref_sources.append(with_revision(rec_no_rev))
    sourcemap={s['id']:r for s,r in zip(sources,ref_sources)}
    chapfiles=sorted((ROOT/'docs/chapters').glob('*.md'))
    assert len(chapfiles)==22, 'canonical v1 requires twenty-two scientific chapters'
    per_chapter_source=['SQLITE_PLANNER','SQLITE_WAL','SQLITE_PLANNER','SQLITE_PLANNER',
      'PG_PLANNER','PG_PLANNER','PG_EXPLAIN','PG_PLANNER','PG_EXPLAIN',
      'SQLITE_WAL','PG_ISOLATION','SQLITE_WAL','SQLITE_ANALYZE','SQLITE_ISOLATION',
      'PG_INDEX_ONLY','PG_STATS_DETAILS','PG_PLANNER','SQLITE_PLANNER',
      'SQLITE_WAL','PG_ISOLATION','SQLITE_EQP','SQLITE_PLANNER']
    equation_by_chapter={
       1:'TRUE, FALSE, UNKNOWN; SQL NULL comparison yields UNKNOWN',
       2:'R=floor((page_bytes-header_bytes)/row_bytes); P=ceil(rows/R)',
       3:'immutable fence lookup O(log(leaf_count)+matches)',
       4:'index lexicographic sort keys (a,b, row_id)',
       5:'P(A and B) ≈ P(A)P(B) only under independence',
       6:'Cscan=P*cseq+N*ccpu; Cindex=ceil(log2(P+1))*crand+seek_pages*crand+M*ccpu',
       7:'hash join expected O(N+M+output), excluding spills',
       8:'DP[S]=min(DP[A]+DP[S\\A]+Cjoin(A,S\\A)) over valid A',
       9:'first_run_count=ceil(N/M); merge_passes=ceil(log_fan_in(first_run_count))',
       10:'hit_ratio=sum(hits)/requests',
       11:'visible(k,s)=argmax_commit_ts<=s(version(k))',
       12:'commit durability requires ordered persisted log writes under stated assumptions',
       13:'estimated_plan!=measured_latency; compare output bags',
       14:'sha256(source_bytes) must match exact recorded immutable revision',
       15:'H=sum_i 1[heap_page(i) not in visibility_map]; index_only=m-H',
       16:'P(A and B) != P(A)*P(B) under correlated predicates',
       17:'DP[S]=min_j(DP[S\{j}]+r(S\{j})*N_j) for a left-deep bounded cost model',
       18:'runs_0=ceil(N/B), runs_(k+1)=ceil(runs_k/(B-1)), IO=2*N*(1+passes)',
       19:'replay applies changes only after matching COMMIT records in a well-formed WAL',
       20:'RW1->2 and RW2->1 is a two-transaction anti-dependency cycle',
       21:'regret=t(argmin_i c_i)-min_i t_i, for separate observed t and estimate c',
       22:'SHA256(full_restored_zip)==SHA256(expected_canonical_zip)' 
    }
    concepts=[];claims=[];equations=[];methods=[]
    for i,chap in enumerate(chapfiles,1):
        title=re.search(r'^## \d{2} — (.+)',chap.read_text(),flags=re.M).group(1)
        content=chap.read_text(encoding='utf-8')
        src=sourcemap[per_chapter_source[i-1]]
        src_link={'record_id':src['record_id'],'revision':src['revision']}
        concepts.append(mkrecord('concept',f'chapter-{i:02d}-concept',title,content,[src_link],
                                 chapter_path=f'docs/chapters/{chap.name}'))
        claim_text=f"Bounded educational claim for {title}. The complete procedure, assumptions and counterexamples are in chapters/{chap.name}. The finite reference code is not a production implementation."
        claims.append(mkrecord('claim',f'chapter-{i:02d}-claim',title+' — scoped claim',claim_text,[src_link],chapter_path=f'docs/chapters/{chap.name}'))
        equations.append(mkrecord('equation',f'chapter-{i:02d}-equation',title+' — symbolic model',
                                  'Educational model; applicability and units are specified in the chapter, not empirically calibrated.',
                                  [src_link],chapter_path=f'docs/chapters/{chap.name}',equation=equation_by_chapter[i]))
        methods.append(mkrecord('method',f'chapter-{i:02d}-method',title+' — offline reconstruction procedure',
                                f'See docs/chapters/{chap.name}; execute both test_db_reference.py, test_db_extended.py and both independent oracle scripts; compare independent results and negative cases. Do not infer real storage durability.',
                                [src_link],chapter_path=f'docs/chapters/{chap.name}'))
    receipt=json.loads((ROOT/'CUMULATIVE_ORACLE_RECEIPT_v1.0.0.json').read_text())
    dataset=[mkrecord('dataset','dataset:finite-oracle','Constructed finite oracle corpus and receipt',
                      f"Constructed seeded independent oracles: {receipt['comparisons']} finite checks, {receipt['failures']} failures. No physical workload benchmark or independent expert review.")]
    groups={'concept':concepts,'claim':claims,'equation':equations,'method':methods,
            'source':ref_sources,'dataset':dataset,'review':[]}
    # Exact dependency anchors are read from the complete verified predecessor
    # common corpus, never from a guessed summary or a versionless latest ID.
    FEDERATION_ROOT=ROOT.parent
    required_ids={
       'os-internals-atlas':{7,14},
       'software-design-patterns-atlas':{13,14,21},
       'network-stacks-atlas':{10,20,22},
    }
    old_records=[]
    for node, numbers in required_ids.items():
        path=FEDERATION_ROOT/'common/nodes'/node/'data/concepts.jsonl'
        for line in path.read_text().splitlines():
            obj=json.loads(line)
            if obj['record_id'] in {f'{node}:chapter-{n:02d}-concept' for n in numbers}:
                assert with_revision({k:v for k,v in obj.items() if k!='revision'})['revision']==obj['revision']
                old_records.append({'record_id':obj['record_id'],'revision':obj['revision'],'title':obj['title']})
    assert len(old_records)==8
    (ROOT/'EXACT_PREDECESSOR_LINKS.json').write_text(json.dumps({
        'schema':'atlas.original-federation-exact-dependency/1',
        'current_authoritative_predecessor_release':'Network_Stacks_v1.0.0',
        'previous_full_archive_sha256':'41d88dac074563965872feae86545cc76748b0cb47811a006e5b3659e3cd6e1e',
        'predecessor_records':old_records,
        'scientific_acceptance':'source record revision presence only; physical evidence not implied',
        'reconstruction':'new full archive must be restored and tested from exact predecessor'
    },sort_keys=True,indent=2)+'\n')
    oldmap={r['record_id']:r for r in old_records}
    deps={
       2:['os-internals-atlas:chapter-07-concept'],
       10:['os-internals-atlas:chapter-07-concept','software-design-patterns-atlas:chapter-21-concept'],
       11:['software-design-patterns-atlas:chapter-14-concept'],
       12:['os-internals-atlas:chapter-14-concept','software-design-patterns-atlas:chapter-13-concept'],
       14:['os-internals-atlas:chapter-14-concept'],
       20:['software-design-patterns-atlas:chapter-14-concept'],
       22:['network-stacks-atlas:chapter-20-concept','network-stacks-atlas:chapter-22-concept'],
    }
    relations=[];counter=0
    for i,(concept,claim,equation,method) in enumerate(zip(concepts,claims,equations,methods),1):
        for from_record,to_record,rtype in [(concept,claim,'related_to'),
                                            (concept,equation,'related_to'),
                                            (concept,method,'related_to'),
                                            (sourcemap[per_chapter_source[i-1]],concept,'related_to')]:
            counter+=1;relations.append(relation(counter,from_record,to_record,rtype))
        for target_id in deps.get(i,[]):
            target=oldmap[target_id]
            counter+=1;relations.append(relation(counter,concept,target,'depends_on',
                'Prior federation source record exact revision; dependency not a proof of engineering acceptance'))
    assert len(relations)>=90, len(relations)
    records={r['record_id']:r for kind,rr in groups.items() for r in rr}
    for r in relations:
        for key in ('from','to'):
            link=r[key]
            x=records.get(link['record_id']) or oldmap.get(link['record_id'])
            assert x and x['revision']==link['revision'],link
    paths={'concept':'concepts.jsonl','claim':'claims.jsonl','equation':'equations.jsonl',
           'method':'methods.jsonl','source':'sources.jsonl','dataset':'datasets.jsonl',
           'review':'reviews.jsonl','relations':'relations.jsonl'}
    collections={}
    for kind,path in paths.items():
        seq=relations if kind=='relations' else groups[kind]
        outfile=data/path
        payload=''.join(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n' for x in seq).encode()
        outfile.write_bytes(payload)
        collections[kind]={'path':'data/'+path,'records':len(seq),'sha256':hashlib.sha256(payload).hexdigest()}
    corpus_rev=hashlib.sha256(canonical(collections)).hexdigest()
    manifest={'schema':'atlas.common/1','node_id':NODE,'title':'Database Optimization Atlas — original canonical scoped offline content v1.0.0',
              'software_version':'1.0.0','contract_version':'1.0','index_revision':'bm25-fields-1',
              'scope':'Finite query-planning, index, join, buffer, MVCC, WAL and offline SQLite reference; no production assurances',
              'evidence_maturity':'22 original technical chapters, independent finite software oracles, full federation restoration and regression receipts; hardware and authenticated originals HOLD',
              'schema_conformance_does_not_validate_science':True,
              'capabilities':['discover','search','fetch','neighbors','assemble_context','validate_context','changes_since'],
              'required_extensions':[],'collections':collections,'corpus_revision':corpus_rev}
    (ROOT/'atlas_manifest.json').write_bytes(canonical(manifest)+b'\n')
    return {'records':sum(len(v) for v in groups.values()),'relations':len(relations),'source_cards':len(ref_sources),
            'chapters':len(concepts),'corpus_revision':corpus_rev,'record_groups':{k:len(v) for k,v in groups.items()}}

if __name__=='__main__':print(json.dumps(make(),indent=2))
