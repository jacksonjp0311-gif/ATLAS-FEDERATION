#!/usr/bin/env python3
"""Check reference linkage, teaching artifacts and coverage inventory.

Structural checks only: does not decide whether prose is scientifically true,
answer the review questions with a model, or run independent peer review.
"""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]

def check(root=ROOT):
    problems=[]
    d=json.loads((root/'evidence/primary_reference_additions.json').read_text(encoding='utf-8'))
    records={r['id']:r for r in d['records']};sources={s['id']:s for s in d['sources']}
    if len(records)!=len(d['records']):problems.append('Duplicate record IDs')
    if len(sources)!=len(d['sources']):problems.append('Duplicate source IDs')
    for rid,r in records.items():
        if r['source'] not in sources:problems.append(rid+': missing source')
        for field in ['locator','text','assumptions','limitations']:
            if not r.get(field):problems.append(rid+': missing '+field)
        if not (root/'docs/records'/f'{rid}.md').is_file():problems.append(rid+': missing human record page')
    q=json.loads((root/'evaluations/content_review_questions.json').read_text())
    for row in q['cases']:
        if not row['required_points'] or not row['prohibited_inferences']:problems.append(row['id']+': incomplete rubric')
        if set(row['reference_ids'])-records.keys():problems.append(row['id']+': unresolved rubric references')
    coverage=json.loads((root/'evaluations/content_coverage.json').read_text())
    for row in coverage['families']:
        if not (root/row['chapter']).is_file():problems.append(row['id']+': missing chapter')
        if set(row['representative_record_ids'])-records.keys():problems.append(row['id']+': missing coverage references')
        if not row['remaining']:problems.append(row['id']+': must state known remaining work')
    for p in (root/'docs').rglob('*.md'):
        if 'history' in p.relative_to(root/'docs').parts or p.name.startswith('RELEASE_AUDIT_v0.4'):continue
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):continue
            target=target.split('#',1)[0]
            if target and not (p.parent/target).exists():problems.append(f'{p.relative_to(root)}: unresolved local link {target}')
    return {'schema':'measurement.content-audit/1','valid':not problems,'record_count':len(records),'primary_source_pages':len(sources),
            'chapters':len(coverage['families']),'review_questions':len(q['cases']),'errors':problems,
            'check_scope':'current docs only: structure, local links, source references, assumptions and limits; archived historical relative-link contexts excluded',
            'scientific_truth_validated':False,'ai_questions_executed':False,'independent_review':False}
if __name__=='__main__':
    r=check();print(json.dumps(r,indent=2));sys.exit(0 if r['valid'] else 2)
