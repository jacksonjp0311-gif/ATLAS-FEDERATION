"""Explicit one-time legacy-to-common import. No source-specific runtime branches.

Reads pinned packaged data only. Preserves upstream fields and labels without
scientific status promotion. This script may rewrite only the generated common
view; it never changes the frozen federation snapshots.
"""
from pathlib import Path
import argparse
import json
import sys
from copy import deepcopy
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from atlas_forge.federation import Federation
from atlas_forge.common import seal,canonical,sha,write_node,write_registry,AtlasStore


def strings(v):
    if v is None:return []
    if isinstance(v,str):return [v] if v else []
    if isinstance(v,list):return [x if isinstance(x,str) else json.dumps(x,ensure_ascii=False,sort_keys=True) for x in v]
    return [json.dumps(v,ensure_ascii=False,sort_keys=True)]


def make_record(nid,rid,kind,title,text, *, sources=None,evidence=None,qualifiers=None,provenance=None,tags=None):
    q=qualifiers or {}
    return seal({'schema':'atlas.record/1','node_id':nid,'record_id':rid,'original_id':rid.split(':')[-1], 'type':kind,'title':title,
      'content':{'text':text or '', 'tags':tags or [], 'domain':q.get('domain',''), 'equation':q.get('equation') or '',
                 **{k:strings(q.get(k)) for k in ('assumptions','applicability','limitations','units','uncertainty')}},
      'evidence':evidence or {'origin':'editorial','review_status':'imported_unreviewed','locators':[],'gaps':['No primary-source check performed by this migration.'],'upstream_labels':{}},
      'sources':sources or [],'status':'active','rights':{'status':'local_reference','note':'Project-owned reference metadata/paraphrase. Third-party source rights remain separate; no full text mirrored.'},
      'provenance':provenance or {},'extensions':{}})


def migrate(destination: Path, additions: Path) -> dict:
    fed=Federation();legacy=fed.export();disc=fed.discover();nodes={x['id']:x for x in disc['nodes']}; groups={nid:[] for nid in nodes}; source_map={}
    for old in legacy:
        if old['kind']!='source_card':continue
        r=make_record(old['node_id'],old['record_uid'],'source',old['title'],old['text'],provenance={'legacy_envelope':old},
                      qualifiers={'limitations':old['limitations'],'domain':old['domain']},tags=strings(old['tags']))
        r['evidence']['origin']='bibliographic_metadata';r['evidence']['upstream_labels']={'status':old['upstream_status']};r=seal(r)
        groups[old['node_id']].append(r);source_map[(old['node_id'],old['original_id'])]=r
    typemap={'claim':'claim','concept':'concept','source_audit':'review','publisher_portion':'review','external_dataset_catalog':'dataset','starter_packet':'concept'}
    for old in legacy:
        if old['kind']=='source_card':continue
        raw=old['upstream_record'];srcs=[source_map[(old['node_id'],s['source_id'])] for s in old['sources']]
        q={k:raw.get(k,old.get(k)) for k in ('assumptions','applicability','limitations','units','uncertainty','domain','equation')}
        ev={'origin':raw.get('evidence_kind','source_reported' if old['kind'] in {'source_audit','publisher_portion'} else 'editorial'),
            'review_status':'imported_unreviewed','locators':[],'gaps':['Preserved upstream labels are not independently reviewed by the common-contract migration.'],
            'upstream_labels':{'upstream_status':old['upstream_status'],'federation_status':old['federation_status']}}
        r=make_record(old['node_id'],old['record_uid'],typemap[old['kind']],old['title'],old['text'],
                      sources=[{'record_id':s['record_id'],'revision':s['revision']} for s in srcs],evidence=ev,qualifiers=q,provenance={'legacy_envelope':old},tags=strings(old['tags']))
        groups[old['node_id']].append(r)
    added=json.loads(additions.read_text(encoding='utf-8'));nid='measurement-atlas';new_sources={};new_records={}
    for s in added['sources']:
        rid=f'{nid}:source:{s["id"]}'
        r=make_record(nid,rid,'source',s['title'],'Primary source navigation: '+s['inspected_scope'],provenance={'source_url':s['url'],'publication':s['publication'],'source_record':s},
                      evidence={'origin':'bibliographic_metadata','review_status':'source_navigation','locators':[],'gaps':['Source identity is not a claim-level independent review.'],'upstream_labels':{}},
                      qualifiers={'domain':'measurement-science','limitations':s['rights']})
        groups[nid].append(r);new_sources[s['id']]=r
    for c in added['records']:
        source=new_sources[c['source']];rid=f'{nid}:{c["kind"]}:{c["id"]}'
        evidence={'origin':c['origin'],'review_status':'primary_portion_checked_by_assistant','locators':[{'source_id':source['record_id'],'locator':c['locator'],
                  'inspected_scope':c.get('inspected_scope','The cited primary HTML portion and displayed formulas; bounded paraphrase or declared substitution.'),
                  'checked_at':added['checked_at'],'checker':'OpenAI assistant, not independent scientific reviewer'}],
                  'gaps':['No independent reviewer or physical replication.'],'upstream_labels':{}}
        r=make_record(nid,rid,c['kind'],c['title'],c['text'],sources=[{'record_id':source['record_id'],'revision':source['revision']}],evidence=evidence,
                      qualifiers={'assumptions':c['assumptions'],'limitations':c['limitations'],'equation':c['equation'],'domain':'measurement-science',
                                  'applicability':['Declared scope only; caller must establish applicability.'],'units':['Use compatible units in the stated model.']},
                      provenance={'source_url':source['provenance']['source_url'],'curation_receipt':'evidence/primary_reference_additions.json','curation_receipt_sha256':sha(additions.read_bytes()),'method':'assistant primary portion inspection; no lab claim'},tags=c['tags'])
        groups[nid].append(r);new_records[c['id']]=r
    edges=[]
    for i,e in enumerate(added['relations']):
        a,b=new_records[e['from']],new_records[e['to']]
        edges.append(seal({'schema':'atlas.relation/1','relation_id':f'{nid}:relation:{i+1:03d}','type':e['type'],
                          'from':{'record_id':a['record_id'],'revision':a['revision']},'to':{'record_id':b['record_id'],'revision':b['revision']},
                          'provenance':{'basis':'editorial method-navigation relation','note':e['note'],'not_independent_scientific_evidence':True}}))
    entries=[];counts={}
    for nid,recs in sorted(groups.items()):
        directory=destination/'nodes'/nid
        write_node(directory,node_id=nid,title=nodes[nid]['title'],software_version=added['revision'] if nid=='measurement-atlas' else nodes[nid]['version'],
                   records=recs,relations=edges if nid=='measurement-atlas' else [],scope=nodes[nid].get('scope','Imported reference subset; see preserved upstream fields.'),
                   evidence_maturity='mixed; imported historical references and bounded assistant primary-portion checks' if nid=='measurement-atlas' else 'legacy imported; upstream labels preserved without new scientific review')
        mp=directory/'atlas_manifest.json';entries.append({'node_id':nid,'manifest':mp.relative_to(destination).as_posix(),'manifest_sha256':sha(mp.read_bytes())});counts[nid]=len(recs)
    write_registry(destination,entries);new=AtlasStore(destination)
    return {'schema':'atlas.migration-receipt/1','legacy_records_preserved':len(legacy),'common_records':new.discover()['records'],'counts':counts,
            'added_measurement_records':len(added['records']),'added_source_pages':len(added['sources']), 'domain_specific_runtime_branches':0,
            'legacy_federation_unchanged':True,'scientific_status_promotion':False,'registry_revision':new.registry_revision}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--measurement-additions',type=Path,required=True);p.add_argument('--out',type=Path,default=ROOT/'src/atlas_forge/resources/common')
    a=p.parse_args();r=migrate(a.out,a.measurement_additions);print(json.dumps(r,indent=2))
