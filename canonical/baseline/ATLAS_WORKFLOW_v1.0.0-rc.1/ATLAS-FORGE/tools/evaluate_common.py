#!/usr/bin/env python3
"""Authored diagnostic, not a blind test or model-answer evaluation."""
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from atlas_forge.common import AtlasStore,tokens,sha,canonical

def run():
    spec=json.loads((ROOT/'evaluations/queries.json').read_text(encoding='utf-8'));s=AtlasStore()
    rows=[];stats={name:{'answerable':0,'hit5':0,'rr_total':0.0,'unsupported':0,'no_match':0} for name in ('bm25','lexical_overlap')}
    for case in spec['cases']:
        node_ids=case.get('node_ids');q=case['question'];expected=set(case['expected_ids']);qt=set(tokens(q))
        baseline=[]
        for r in s.export():
            if r['type']=='source' or r['status'] not in ('active','disputed') or r['rights']['status']!='local_reference':continue
            if node_ids and r['node_id'] not in node_ids:continue
            bag=set(tokens(' '.join([r['title'],r['content']['text'],' '.join(r['content']['tags']),r['content']['domain']])));score=len(qt&bag)
            if score:baseline.append((score,r['record_id']))
        baseline.sort(key=lambda x:(-x[0],x[1]))
        ranked={'bm25':[h['record_id'] for h in s.search(q,node_ids=node_ids,limit=5)['results']],
                'lexical_overlap':[uid for _,uid in baseline[:5]]}
        row={'id':case['id'],'question':q,'expected_ids':sorted(expected),'ranked':ranked}
        for name,ids in ranked.items():
            st=stats[name]
            if expected:
                st['answerable']+=1;positions=[i+1 for i,x in enumerate(ids) if x in expected]
                if positions:st['hit5']+=1;st['rr_total']+=1/min(positions)
            else:st['unsupported']+=1;st['no_match']+=not ids
        packet=s.assemble_context(q,node_ids=node_ids,max_context_bytes=32768)
        valid=s.validate_context(packet)['valid'];row['context_valid']=valid;row['context_status']=packet['status'];row['context_bytes']=packet['context_bytes'];rows.append(row)
    for st in stats.values():
        st['hit5_fraction']=st['hit5']/max(1,st['answerable']);st['mrr5']=st.pop('rr_total')/max(1,st['answerable'])
        st['no_match_fraction']=st['no_match']/max(1,st['unsupported'])
    return {'schema':'atlas.authored-diagnostic/1','test_set_sha256':sha(canonical(spec)),'registry_revision':s.registry_revision,
       'evaluation_kind':'author_curated_seen_regression','independently_blinded':False,'actual_ai_run':False,'live_bitwork_run':False,
       'metrics':stats,'context_integrity_passed':sum(r['context_valid'] for r in rows),'cases':len(rows),'rows':rows,
       'limitations':['Small authored test set; used during development.','No neural semantic or actual Bitwork comparison.','Lexical baseline shares corpus and excludes the same inadmissible record types.','No-match is lexical behavior, not semantic out-of-domain detection.','No answer quality, energy saving or model improvement established.']}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path);a=p.parse_args();r=run()
    text=json.dumps(r,indent=2,ensure_ascii=False)+'\n'
    if a.out:a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(text,encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
    sys.exit(0 if r['context_integrity_passed']==r['cases'] else 2)
