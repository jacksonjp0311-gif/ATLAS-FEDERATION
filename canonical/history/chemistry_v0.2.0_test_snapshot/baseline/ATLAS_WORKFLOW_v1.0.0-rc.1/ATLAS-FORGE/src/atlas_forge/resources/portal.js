'use strict';
const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
const link=(label,url)=>{const a=el('a',label);a.href=url;a.target='_blank';a.rel='noopener noreferrer';return a;};
async function loadNodes(){
 try{const res=await fetch('/api/nodes');const data=await res.json();const box=document.getElementById('nodes');box.replaceChildren();
 for(const node of data.nodes){const c=el('article',undefined,'card');const okay=node.integrity==='passed';c.append(el('span',okay?(node.enabled_by_default?'REFERENCE NODE':'STARTER NODE'):'UNAVAILABLE','pill '+(node.enabled_by_default?'':'starter')),el('h2',node.title||node.id));
 c.append(el('p',node.description||node.error),el('p',String(node.record_count??0),'number'),el('span','searchable reference records','small'));
 if(okay){c.append(el('p','Version '+node.version+' · snapshot integrity passed','small'));const up=node.upstream;if(up.url)c.append(link('Independent repository ↗',up.url));c.append(el('p',up.commit?'Pinned commit '+up.commit.slice(0,12):'Local starter · excluded from default search','small'));const opt=el('option',node.title);opt.value=node.id;document.getElementById('node').append(opt);}
 box.append(c);}
 if(!data.valid)document.getElementById('status').textContent='Some nodes are unavailable. Review /api/verify.';
 }catch(e){document.getElementById('nodes').textContent='Unable to load nodes: '+e.message;}
}
document.getElementById('search').addEventListener('submit',async event=>{event.preventDefault();const status=document.getElementById('status'),results=document.getElementById('results');status.textContent='Searching pinned snapshots…';results.replaceChildren();
 const params=new URLSearchParams({q:document.getElementById('question').value,per_node:'4',include_starters:String(document.getElementById('starter').checked)});const node=document.getElementById('node').value;if(node)params.append('node',node);
 try{const response=await fetch('/api/search?'+params);const data=await response.json();if(data.error)throw new Error(data.error);status.textContent=(data.results.length?data.results.length+' context records. ':'No matching reference records. ')+(data.degraded?'Some nodes failed validation. ':'')+'No answer has been independently verified.';
 for(const group of data.groups){if(!group.results.length)continue;results.append(el('h2',group.node_id+' · '+group.node_version));for(const r of group.results){const card=el('article',undefined,'result');card.append(el('span',r.kind,'pill'),el('h3',r.title),el('p',r.text),el('p','Upstream label: '+r.upstream_status,'small'),el('p',r.limitations||'See upstream record for scope.','boundary'));for(const s of r.sources){const p=el('p',undefined,'small');p.append(link(s.title,s.url));card.append(p);}const d=el('details');d.append(el('summary','Inspect full provenance and original record'),el('pre',JSON.stringify(r,null,2)));card.append(d);results.append(card);}}
 if(data.excluded_nodes.length)results.append(el('p','Measurement starter is excluded unless explicitly enabled.','muted'));
 }catch(e){status.textContent='Search failed: '+e.message;}
});loadNodes();
