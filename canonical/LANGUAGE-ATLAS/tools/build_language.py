"""Build first Language Atlas content edition from original chapter source.

Source cards have verified-scoped description status (or bibliography-only),
not authenticated original publication bytes or community recordings.
"""
from __future__ import annotations
import sys,json,re,hashlib,shutil,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
NODE=ROOT/'LANGUAGE-ATLAS';PACK=NODE/'language_atlas';D=NODE/'docs'
sys.path[:0]=[str(Path(__file__).resolve().parent),str(ROOT/'baseline/ATLAS_WORKFLOW_v1.0.0-rc.1/ATLAS-FORGE/src'),str(NODE)]
from atlas_forge.common import seal,write_node,write_registry,sha,canonical,AtlasStore
from chapter_content import CHAPTERS
from language_atlas.cases import casebook

SOURCES={
 'UNICODE-UAX15':('Unicode Standard Annex #15 — Normalization Forms','Unicode Consortium','https://www.unicode.org/reports/tr15/','Unicode 18.0, published 2026-08-12; inspected summary, definitions of NFC/NFD/NFKC/NFKD','selected_official_page','Unicode published normative standard; original content terms/rights must be checked; no full text mirrored'),
 'UNICODE-UAX29':('Unicode Standard Annex #29 — Text Segmentation','Unicode Consortium','https://www.unicode.org/reports/tr29/','Unicode 18.0, published 2026-09-01; inspected abstract and grapheme/word/sentence boundaries','selected_official_page','Unicode normative content and related data rights must be checked; no original bytes retained'),
 'UNICODE-CORE':('The Unicode Standard and character model','Unicode Consortium','https://www.unicode.org/standard/standard.html','Bibliographic pointer to Unicode standard character properties; full specification not audited','bibliographic_only','Rights retained by Unicode Consortium; no full source mirrored'),
 'IPA-CHART':('International Phonetic Alphabet, current IPA Chart','International Phonetic Association','https://www.internationalphoneticassociation.org/content/chart','Official IPA chart notation, Council revisions and reproduction terms; current chart rights CC BY-SA 4.0','selected_official_page','IPA chart CC BY-SA 4.0 with attribution/share alike where applicable; chart not copied'),
 'WALS':('World Atlas of Language Structures Online','Dryer and Haspelmath (editors)','https://wals.info/','WALS v2020.6 typology database and per-chapter citation guidance; CC BY 4.0 site terms','selected_official_page','WALS site CC BY 4.0; specific linked original chapter and edition must be credited'),
 'PHOIBLE':('PHOIBLE phonological inventories','Moran and McCloy (editors)','https://phoible.org/inventories','Database description and inventories index; PHOIBLE 2.0 CC BY-SA 3.0','selected_official_page','CC BY-SA 3.0 for PHOIBLE 2.0; no inventories copied here'),
 'UD-GUIDE':('Universal Dependencies annotation framework, version 2','UD contributors','https://universaldependencies.org/','UD v2 official overview: cross-linguistic POS, morphology, dependency syntax, public 2026 releases','selected_official_page','Different treebanks have their own licenses; no original treebank mirrored'),
 'UD-CONLLU':('Universal Dependencies CoNLL-U Format','UD contributors','https://universaldependencies.org/format.html','Official 10-column UTF-8 tab-separated sentence format, fields and multiword/empty-node distinctions','selected_official_page','Specification linked; rights and treebank license distinct'),
 'LEIPZIG':('Leipzig Glossing Rules','Max Planck Institute for Evolutionary Anthropology and University of Leipzig','https://www.eva.mpg.de/lingua/resources/glossing-rules.php','Official ten rules and interlinear gloss conventions page, last stated change 2015','selected_official_page','Rules are external publisher material, not reproduced in full'),
 'GLOTTOLOG':('Glottolog language and family bibliographic identifiers','Glottolog contributors','https://glottolog.org/','Bibliographic navigation for reference language names and genealogical classifications; no dataset version pinned','bibliographic_only','Check version and dataset-specific license before archival use'),
 'CLDF':('Cross-Linguistic Data Formats (CLDF)','CLDF/Glottobank consortium','https://cldf.clld.org/','CLDF 1.3 official overview: UTF-8 CSV, linked identifiers, metadata and interoperability','selected_official_page','CLDF specification and individual datasets have separately scoped licenses'),
 'BCP47':('RFC 5646 — Tags for Identifying Languages','IETF / RFC Editor','https://www.rfc-editor.org/rfc/rfc5646','BCP47 official abstract: syntax, structure, semantics and registered subtags','selected_official_page','IETF RFC Trust copyright and code-component terms apply; not mirrored'),
 'RFC4647':('RFC 4647 — Matching of Language Tags','IETF / RFC Editor','https://www.rfc-editor.org/rfc/rfc4647','BCP47 official abstract about filtering and lookup matching','selected_official_page','IETF Trust rights retained'),
 'SLP3':('Speech and Language Processing, Third Edition online draft','Daniel Jurafsky and James H. Martin','https://web.stanford.edu/~jurafsky/slp3/','Authors August 19, 2026 manuscript release; inspected site contents and edition details','selected_official_page','© 2026 authors all rights reserved; only link and original brief educational synthesis'),
 'SEP-COMPOS':('Compositionality','Stanford Encyclopedia of Philosophy','https://plato.stanford.edu/entries/compositionality/','Stanford Encyclopedia 2025 revision: structure, constituent meaning, theories and counterarguments','selected_scholarly_page','Stanford authors/publisher copyright; original article not mirrored'),
 'SEP-PRAG':('Pragmatics','Stanford Encyclopedia of Philosophy','https://plato.stanford.edu/entries/pragmatics/','Bibliographic pointer for context dependence and language-use theory; no full-page review','bibliographic_only','Stanford source copyright and terms retained'),
 'SEP-IMPLICATURE':('Implicature','Stanford Encyclopedia of Philosophy','https://plato.stanford.edu/entries/implicature/','Bibliographic pointer for conversational implicature and cancellability','bibliographic_only','Stanford source copyright, no article mirrored'),
 'LSA-SIGN':('Sign Languages as Natural Languages','Linguistic Society of America','https://www.linguisticsociety.org/resource/sign-languages','Bibliographic pointer about signed linguistic systems, no original primary video inspected','bibliographic_only','No sign-language community recordings or third-party material archived'),
 'TALKBANK':('TalkBank linguistic interaction and transcript resources','TalkBank Project','https://talkbank.org/','Bibliographic overview of corpus, transcription and speaker data; no corpora inspected','bibliographic_only','Corpus-level access, consent and data restrictions apply'),
 'CHILDES':('CHILDES Child Language Data Exchange System','TalkBank CHILDES','https://talkbank.org/childes/','Official CHILDES overview and registration/access conditions, no child-level source data used','selected_official_page','Child language data are sensitive; no child corpus uploaded or mirrored'),
 'ELAR':('Endangered Languages Archive (ELAR)','SOAS University of London','https://blogs.soas.ac.uk/elar/about-elar/','Publisher overview of endangered language multimedia repository and registration','selected_official_page','Community and deposit-specific access conditions govern material, no recording mirrored'),
 'CHOMSKY1956':('Three Models for the Description of Language (1956)','Noam Chomsky','https://doi.org/10.1109/TIT.1956.1056813','Bibliographic historical paper pointer for formal grammar classification; no paper body inspected','bibliographic_only','Publisher copyright remains external'),
 'SHANNON1948':('A Mathematical Theory of Communication (1948)','Claude E. Shannon','https://doi.org/10.1002/j.1538-7305.1948.tb01338.x','Bibliographic historical pointer for communication and entropy, not a paper reproduction','bibliographic_only','Original journal publisher rights may apply'),
 'PRAAT':('Praat phonetic analysis software','Paul Boersma and David Weenink','https://www.fon.hum.uva.nl/praat/','Bibliographic software reference for acoustic analysis and measurements; no instrument data acquired','bibliographic_only','Software and documentation rights checked separately before redistribution'),
 'W3C-LANG':('W3C Internationalization: Language Tags','W3C Internationalization','https://www.w3.org/International/articles/language-tags/','Bibliographic educational overview of language tag choices; no full text reviewed','bibliographic_only','W3C material rights retained'),
}
assert len(SOURCES)==25
DATE='2026-11-14';NID='language-atlas'
RIGHTS={'status':'local_reference','note':'Original educational text and methods; third-party source works remain separately licensed and are not mirrored.'}
records=[];relations=[];by={};rel_ids=set();area_counts=collections.Counter()

def record(key,title,kind,body,sources=(),*,area='language-science',tags=None,equation='',assumptions=None,applicability=None,limitations=None,uncertainty=None,units=None,origin='original_educational_synthesis',review_status='author_method_not_independently_reviewed',gaps=None,extra=None):
    rid=NID+':'+key
    if rid in by:raise AssertionError('duplicate record ID '+rid)
    srcrefs=[by['source:'+source] for source in sources]
    locators=[{'source_id':s['record_id'],'locator':s['provenance']['url'],
        'inspected_scope':s['provenance']['inspected_scope'],'checked_at':DATE,'checker':'AI-assisted selected public source scope; not independent review'} for s in srcrefs]
    r=seal({'schema':'atlas.record/1','node_id':NID,'record_id':rid,'original_id':key,'type':kind,'title':title,'status':'active',
      'content':{'text':body,'tags':tags or [area,kind,'language-0.1.0'],'domain':'linguistic-structure-meaning-communication','equation':equation,
         'assumptions':assumptions or ['Language and analysis context is explicitly declared','Inputs and source scope are bounded'],
         'applicability':applicability or ['Offline linguistic science and methods reference, not a language identification or translation deployment'],
         'limitations':limitations or ['No corpus-wide or independent human linguist validation','No full primary-source document archived'],
         'units':units or ['Declared codepoint, token, probability or timeline unit only where applicable'],
         'uncertainty':uncertainty or ['Alternative linguistic analyses and speaker variation may exist']},
      'evidence':{'origin':origin,'review_status':review_status,'locators':locators,'gaps':gaps or ['No primary original source bytes or independently reviewed language study'],
        'upstream_labels':{}},
      'sources':[{'record_id':x['record_id'],'revision':x['revision']} for x in srcrefs], 'rights':dict(RIGHTS),
      'provenance':{'author':'James Paul Jackson research program; AI-assisted original instructional drafting',
          'created_at':DATE,'edition_added':'0.1.0','independent_scientific_review':False,**(extra or {})},'extensions':{}})
    by[key]=r;records.append(r);return r

def relate(a,b,kind='qualifies',origin='author_qualified_dependency'):
    x,y=by[a],by[b];rid=f'{NID}:{len(relations):04d}:{kind}'
    rel=seal({'schema':'atlas.relation/1','relation_id':rid,'type':kind,
        'from':{'record_id':x['record_id'],'revision':x['revision']},
        'to':{'record_id':y['record_id'],'revision':y['revision']},
        'provenance':{'origin':origin,'scope':'Bounded conceptual dependency; does not demonstrate scientific causal effect',
                      'independent_scientific_review':False}})
    if rid in rel_ids:raise AssertionError('duplicate relation ID')
    rel_ids.add(rid);relations.append(rel)

for sid,(title,author,url,scope,level,license_note) in SOURCES.items():
    r=record('source:'+sid,title,'source',f'{author}. Bibliographic pointer: {url}. Inspected extent: {scope}. Original source bytes are NOT stored in this Atlas.',
       area='source',tags=['bibliography','source',sid],origin='bibliographic_navigation',
       review_status='selected_source_abstract_or_page_checked_by_assistant' if level=='selected_official_page' or level=='selected_scholarly_page' else 'bibliographic_reference_not_inspected',
       assumptions=['Source page may be versioned or revised'],
       applicability=['Source navigation and limited scholarly context, not an unlicensed copy'],
       limitations=['No original publisher text/audio/video retained','No expert claim review'],
       uncertainty=['Publisher source contents may change after the inspected date'],
       gaps=['Original transport bytes not acquired','Licensing and reuse rights are not universal across corpora or editions'],
       extra={'url':url,'source_author':author,'inspected_scope':scope,'access_level':level,'rights_note':license_note,'original_source_bytes_archived':False})

print('sources built',len(records))
MANUAL=['# Language Atlas v0.1.0 — Reconstructing human language and communication',
  'A comprehensive foundational **reference edition**, not a complete science of every language or a trained universal language model.',
  'James Paul Jackson research program · 14 November 2026 · ATLAS Common Contract v1.0',
  'Source notes are link-only unless explicitly proven otherwise. No copyrighted publications, recordings, treebanks, sign-language video or community material are mirrored.',
  '## How to read',
  'Start with form and representation (speech, sign, phonology, scripts), then morphology, syntax, meaning, use, acquisition, corpus science and preservation. Each chapter teaches a scoped hypothesis and a reconstruction experiment; it does not certify real-world cultural or linguistic judgments.',
  ]
GUIDE=['# Language Atlas — Scientific Reading Directory v0.1.0',
  '**Observed form → Feature/word analysis → Structural hypothesis → Semantic interpretation → Pragmatic context → Qualified evidence.**',
  'All reconstructions and casebooks are original constructed fixtures, not human-subject experiments or source language corpora.',
  '## Chapters']
D.mkdir(exist_ok=True,parents=True)
for i,ch in enumerate(CHAPTERS,1):
    n=f'{i:02d}';slug=re.sub(r'[^a-z0-9]+','_',ch['title'].lower()).strip('_')[:72]
    name=n+'_'+slug+'.md';area=ch['area'];area_counts[area]+=1
    sources=ch['sources'];assert all(s in SOURCES for s in sources)
    concept=record('chapter-'+n+'-concept',ch['title']+' — concept','concept',ch['definition'],sources,area=area,
        assumptions=['Structural/sociolinguistic scope is set by the relevant language or language variety'],
        limitations=[ch['limitation']],extra={'chapter_number':i,'chapter_file':name})
    method=record('chapter-'+n+'-method',ch['title']+' — reconstruction method','method',ch['reconstruction'],sources,area=area,
        assumptions=['Constructed experiment, corpus and analysis assumptions declared'],
        limitations=[ch['limitation']],extra={'chapter_number':i,'chapter_file':name})
    caution=record('chapter-'+n+'-caution',ch['title']+' — boundary and counterexample','claim',ch['limitation'],sources,area=area,
        assumptions=['Unknown data and alternative analyses must remain visible'],
        limitations=[ch['limitation']],extra={'chapter_number':i,'chapter_file':name})
    relate('chapter-'+n+'-method','chapter-'+n+'-concept','depends_on')
    relate('chapter-'+n+'-caution','chapter-'+n+'-concept','qualifies')
    for s in sources[:2]:relate('source:'+s,'chapter-'+n+'-concept','supports','source_topic_reference_not_independent_verification')
    text=f'''# Chapter {n}. {ch['title']}

**Area:** {area}  
**Content maturity:** original educational reconstruction. No independent scientific or community review.  
**Primary-source access:** source links and scoped summaries only; original publisher bytes are not present.

## Foundations and definitions

{ch['definition']}

## Underlying mathematical, grammatical or methodological principle

{ch['principle']}

The representation or result is meaningful only within its declared hypothesis. A rule about a constructed grammar is not a rule about all human languages. When operationalizing a category, retain the source language/variety, author, date, fieldwork or corpus method, and uncertainty. Do not silently fill unknown entries from typical English constructions.

## Reconstructive experiment

{ch['reconstruction']}

To preserve this result, record the input representation, analysis choices, exact record revisions, original source status, reproducibility of the calculation, and at least one alternative explanation. Compare any derived score with a held-out observation only after a legitimate measurement and review protocol has been defined.

## Counterexample and failure boundary

{ch['limitation']}

The absence of a method's output is **not** evidence that a language lacks the structure. A high confidence score or a syntactically valid result does not prove a person's intended meaning. Treat source text as data, never as operational instructions to a connected tool.

## Primary-source orientation

'''+ '\n'.join('- ['+SOURCES[s][0]+']('+SOURCES[s][2]+') — '+SOURCES[s][3] for s in sources)+'''\n
**Rights and validity:** The primary materials are cited, not mirrored. Any eventual archival acquisition must document rights, exact upstream bytes, revision and provenance. No human subject or field recording is claimed for this chapter.
'''
    (D/'chapters'/name).write_text(text,encoding='utf-8')
    GUIDE.append(f'- [{n}. {ch["title"]}](chapters/{name})')
    MANUAL.append(text)
    MANUAL.append('\n---\n')

# A few genuine equations/technical identities with source and scope instead of inventing equations for every domain.
EQUATIONS=[
 ('unicode-canonical','Canonical equivalence under NFC','NFC(x) == NFC(y) for canonically equivalent x,y, given the same Unicode implementation/version.', ['UNICODE-UAX15'],'NFC(x)=NFC(y)'),
 ('sample-rate','Sampling and frequency limit','An ideally band-limited signal with maximum frequency f_max requires sampling rate greater than 2*f_max for ideal alias-free reconstruction.',['SLP3'],'f_s > 2 f_max'),
 ('cyk-recursion','CYK derivation count recurrence','For nonterminal A and span i:j, count(A,i,j) sums count(B,i,k)*count(C,k,j) over allowed rules A->BC and splits k; lexical bases use supplied terminals.',['CHOMSKY1956','SLP3'],'C[A,i,j]=sum_(A->BC,k) C[B,i,k]*C[C,k,j]'),
 ('universal-quantification','Finite universal quantifier','In classical finite truth, forall x P(x) requires P(d) for every d in D; in the supplied three-valued open-world model unknown instances remain unknown unless a false counterexample exists.',['SEP-COMPOS'],'forall x in D P(x) = AND_(d in D) P(d)'),
 ('existential-quantification','Finite existential quantifier','Exists is satisfied by a known witness; missing observations cannot always prove failure under three-valued interpretation.',['SEP-COMPOS'],'exists x in D P(x) = OR_(d in D) P(d)'),
 ('bigram-probability','Smoothed bigram conditional probability','Add-alpha smoothing under a declared prediction vocabulary and caller-supplied tokenization; different tokenizers produce incomparable scores.',['SLP3'],'P(w|h)=(count(h,w)+alpha)/(count(h)+alpha*|V|)'),
 ('perplexity','Perplexity under a fixed tokenization','The token-level geometric inverse probability; low values indicate predictive fit, not semantic understanding.',['SLP3','SHANNON1948'],'PP=2^(-sum_i log2(P(w_i|history_i))/N)'),
 ('shannon-entropy','Entropy of a language-symbol distribution','Average self-information under a stated distribution, not the truth or human meaningfulness of a message.',['SHANNON1948'],'H(X)=-sum_x p(x) log2 p(x)'),
 ('minimal-contrast','Distinctive feature contrast','Toy categorical feature Hamming distance under a supplied dimension set, not a continuous acoustic or perceptual metric.',['IPA-CHART','PHOIBLE'],'d_f(a,b)=sum_k [feature_k(a)!=feature_k(b)]'),
 ('leakage-id','Exact split exclusion','A valid train/eval ID split needs empty intersection; passing this check cannot exclude semantic duplicates or data contamination.',['SLP3'],'TrainIds ∩ EvalIds = ∅')]
for slug,title,body,source,eq in EQUATIONS:
    r=record('equation-'+slug,title,'equation',body,source,area='formal-method',equation=eq,
      assumptions=['Finite source-defined objects, fixed representations and explicit error conventions'],
      limitations=['A formal identity within a model does not establish the correctness of source annotations or application to all languages'])
    # Link to closest chapter by source intersection, without modifying old records.
    for i,ch in enumerate(CHAPTERS,1):
        if source[0] in ch['sources']:
            relate('equation-'+slug,f'chapter-{i:02d}-concept','qualifies')
            break

# Area-level coverage cards, plus a machine-checkable synthetic-only casebook.
for area,ct in sorted(area_counts.items()):
    items=[ch for ch in CHAPTERS if ch['area']==area]
    ids=list(dict.fromkeys(s for c in items for s in c['sources']))[:3]
    record('coverage-'+re.sub('[^a-z0-9]+','-',area.lower()).strip('-'),area+' — coverage and research debt','review',
        f'{ct} original language-science chapters in the {area} area. All content is model-limited original synthesis; no source texts or human-language corpora were independently acquired. Community annotation, contextual interpretation and scholarly validation remain open.',ids,area='review',
        limitations=['Not a complete or independently reviewed account of any language or community','Primary-source bytes are not retained'],
        gaps=['Community and primary data rights','Independent linguistic validation and cross-linguistic empirical replication'])

cases=casebook()
record('dataset-author-built-casebook','Language Atlas — nineteen constructed reconstruction cases','dataset',
   f"The {cases['case_count']} author-generated deterministic examples demonstrate Unicode, ambiguity, finite semantics, CoNLL-U subset syntax, corpus leakage and toy bigram probabilities; there are no real subject or language data in this dataset.",['SLP3','UNICODE-UAX29','UD-GUIDE'],area='dataset',
   limitations=['Synthetic examples are not a representative sample of human languages or a test of AI comprehension'],
   gaps=['Real rights-cleared source corpus and independent annotation missing'],origin='original_synthetic_cases',
   extra={'case_count':cases['case_count'],'corpus_real_language_rows_read':0,'independent_review':False})

# Full federation only: cross-node qualified links. Standalone keeps only local edges.
prev=AtlasStore(ROOT/'common');prev_records=prev.export();cross=[]
requests=[('computation-atlas','string',14),('agent-atlas','language',1),('causal-atlas','confounding',32),('measurement-atlas','calibration',3),('control-atlas','state',23)]
for dest,needle,n in requests:
    hits=[x for x in prev_records if x['node_id']==dest and x['type']!='source' and needle in (x['title']+' '+x['content']['text'][:160]).casefold()]
    if not hits:
        print('cross link not found',dest,needle);continue
    target=hits[0];origin=by[f'chapter-{n:02d}-concept'];rel_id=f'{NID}:{len(relations):04d}:related_to'
    edge=seal({'schema':'atlas.relation/1','relation_id':rel_id,'type':'related_to',
      'from':{'record_id':origin['record_id'],'revision':origin['revision']},
      'to':{'record_id':target['record_id'],'revision':target['revision']},
      'provenance':{'origin':'author_curated_cross_domain_topic_link','scope':'Conceptual caveat/affinity only; no deployed cross-domain router or empirical integration','independent_review':False}})
    relations.append(edge)
    cross.append({'from':origin['record_id'],'to':target['record_id'],'relation_id':rel_id,'target_revision':target['revision']})

NODE_ROOT=ROOT/'common/nodes/language-atlas'
args=dict(node_id=NID,title='Language Atlas — Speech, Sign, Writing, Grammar, Meaning and Communication',software_version='0.1.0',records=records,relations=relations,
 scope='Human-readable language-science research and bounded offline algorithms; not full linguistic corpora, multilingual translation, universal grammar, Unicode conformance or language-model inference.',
 evidence_maturity='Original author-designed computational cases and educational synthesis from scoped bibliography; primary documents and community recordings not locally retained; no independent scientific/cultural review.')
write_node(NODE_ROOT,**args)
old_entries=json.loads((ROOT/'common/registry.json').read_text())['nodes'];add_entry={'node_id':NID,'manifest':'nodes/language-atlas/atlas_manifest.json','manifest_sha256':sha((NODE_ROOT/'atlas_manifest.json').read_bytes())}
write_registry(ROOT/'common',old_entries+[add_entry])
# Standalone projection only local references, preserving all full relations in the full collection.
local=[x for x in relations if x['to']['record_id'].startswith(NID+':')]
resource=PACK/'resources/common';root=resource/'nodes/language-atlas'
write_node(root,**dict(args,relations=local))
entry=dict(add_entry,manifest_sha256=sha((root/'atlas_manifest.json').read_bytes()))
write_registry(resource,[entry]);shutil.copy2(root/'atlas_manifest.json',NODE/'atlas_manifest.json');shutil.copytree(root/'data',NODE/'data',dirs_exist_ok=True)
# Package registry and full federation source-closure verification.
full=AtlasStore(ROOT/'common').discover();standalone=AtlasStore(resource).discover()
assert len(full['nodes'])==9 and full['records']==1475+len(records)
assert len(standalone['nodes'])==1 and standalone['records']==len(records)

# Manual and reading guide.
GUIDE+=['','## Working offline','',
 '```sh','python -m language_atlas','python -m unittest discover -s tests -q','python tools/check_manifest.py verify .','```',
 'Read `SOURCE_REGISTER.md`, `COVERAGE_MATRIX.md` and `VALIDATION_v0.1.0.md` before using any examples outside a constructed setting.',
 'The exact and complete Unicode UAX 29, BCP 47, full UD parser, natural-language reasoning, real audio analysis and translation are **not** implemented.',
 'All thirty domain content libraries precede Bitwork routing, integrated evaluation and desktop transfer.']
(D/'REFERENCE_GUIDE.md').write_text('\n'.join(GUIDE)+'\n')
MANUAL+=['','## External sources, known rights and missing bytes','',(D/'REFERENCE_GUIDE.md').read_text()]
(D/'DEPTH_MANUAL_v0.1.0.md').write_text('\n'.join(MANUAL)+'\n')
source_lines=['# Language Atlas — Source Register v0.1.0','',
 '**Access class:** only selected publisher pages/abstracts and bibliographic metadata. None of these 25 original publisher documents, sign/video recordings or natural-language corpora was downloaded into this package.','',
 '| Card | Link | Inspected scope | Rights and missing evidence |','|---|---|---|---|']
for sid,(title,author,url,scope,level,rights) in SOURCES.items():
    source_lines.append(f'| {sid} | [{title}]({url}) | {level}: {scope} | {rights}; original bytes not locally authenticated |')
(D/'SOURCE_REGISTER.md').write_text('\n'.join(source_lines)+'\n')
area_matrix=['# Language Atlas v0.1.0 — Scientific Coverage and Readiness','',
 '| Area | Chapters | Research maturity | Remaining work |','|---|---:|---|---|']
for area,ct in sorted(area_counts.items()):
    area_matrix.append(f'| {area} | {ct} | Original teaching chapters and bounded model examples | Primary linguistic corpus acquisition, cross-language validation, human/community review |')
area_matrix+=['',
'### What is missing','',
'- Comprehensive original sound/video recordings and associated consent or archival rights','- Normative Unicode 18.0 segmentation and comprehensive language-tag registry validation',
'- Full typological/fieldwork databases and corpus-level statistical generalization',
'- Independent speaker and community linguistic review, and authentic child-language privacy protections',
'- Live ASR, sign recognition, multilingual translation or LLM capability evaluation',
'- Scoped v1 content maturity; Language Atlas 0.1 is an initial substantive reference, not the final domain or an exhaustive record of every language.',
'- Bitwork routing and full-dataset integration; deferred until all 30 content domains exist.']
(D/'COVERAGE_MATRIX.md').write_text('\n'.join(area_matrix)+'\n')

# Casebook and source preservation.
(D/'CASEBOOK.md').write_text('# Language Atlas — Constructed Executable Investigations\n\nAll 19 cases are author-created input fixtures; no real language corpus, audio, video, speaker interview, model performance or independent translation quality was measured.\n\n'+ '\n\n'.join(f"## Investigation {i:02d} — {x['id']}\n\n**Observed structure:** `{json.dumps(x['result'],ensure_ascii=False,default=str)[:1150]}`\n\n**Limitation:** {'; '.join(x['limitations'])}.\n\n**Reproduce:** `python -m language_atlas` in the standalone package." for i,x in enumerate(cases['cases'],1))+'\n')

( NODE/'evidence/build_receipt_v0.1.0.json').write_text(json.dumps({'schema':'atlas.language-build/1','version':'0.1.0','date':DATE,'chapters':len(CHAPTERS),
  'source_cards':len(SOURCES),'records':len(records),'relations_full':len(relations),'relations_standalone':len(local),
  'cross_domain_links_full_only':cross,'eight_node_prior_records_preserved':1475,
  'full_nodes':len(full['nodes']),'full_records':full['records'],'full_relations':full['relations'],
  'casebook_cases':cases['case_count'],'natural_corpus_rows_loaded':0,'human_experiment_rows_loaded':0,
  'authentic_primary_sources_archived':0,'independent_expert_review':False,'router_changed':False},indent=2)+'\n')

print(json.dumps({'result':'built','chapters':len(CHAPTERS),'manual_words':len((D/'DEPTH_MANUAL_v0.1.0.md').read_text().split()),
 'source_cards':len(SOURCES),'records':len(records),'full_relations':len(relations),'standalone_relations':len(local),
 'cross_links':len(cross),'collection_records':full['records'],'collection_relations':full['relations'],'nodes':len(full['nodes'])},indent=2))
