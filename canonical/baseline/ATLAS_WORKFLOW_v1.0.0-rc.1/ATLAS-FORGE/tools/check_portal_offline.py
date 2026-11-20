#!/usr/bin/env python3
"""Offline browser-render check using fixtures captured from the real loopback API.

This is not direct browser-to-HTTP end-to-end validation. It runs the shipped JS
with captured response data so layout and event handlers can be inspected even
where browser policy blocks loopback navigation. Requires optional Playwright.
"""
from pathlib import Path
import argparse,json,shutil,sys,threading,urllib.request
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from atlas_forge.server import make_server
from playwright.sync_api import sync_playwright
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'output/portal-check');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
s=make_server(port=0);t=threading.Thread(target=s.serve_forever,daemon=True);t.start();base=f'http://127.0.0.1:{s.server_port}'
paths=['/api/common/nodes','/api/common/context?q=expanded+uncertainty&max_bytes=32768&limit=5&node=measurement-atlas',
'/api/common/context?q=expanded+uncertainty&max_bytes=512&limit=5&node=measurement-atlas',
'/api/common/context?q=zxqv7788&max_bytes=512&limit=5&node=measurement-atlas']
fixtures={}
try:
 for path in paths:
  with urllib.request.urlopen(base+path,timeout=10) as res:fixtures[path]=json.load(res)
finally:s.shutdown();s.server_close()
resources=ROOT/'src/atlas_forge/resources';html=(resources/'common_portal.html').read_text()
html=html.replace('<link rel="stylesheet" href="/common_portal.css">','<style>'+(resources/'common_portal.css').read_text()+'</style>')
html=html.replace('<script src="/common_portal.js" defer></script>','').replace('src="/hero.png"','src="data:image/png;base64,'+__import__('base64').b64encode((resources/'hero.png').read_bytes()).decode()+'"')
bootstrap='const CAPTURED='+json.dumps(fixtures).replace('</','<\\/')+';window.fetch=async url=>{if(!(url in CAPTURED))throw new Error("Uncaptured request: "+url);return {ok:true,json:async()=>structuredClone(CAPTURED[url])};};'
r={'execution_kind':'local_actual','scope':'offline_browser_js_with_captured_real_http_responses','direct_browser_network_test':False,'views':[],'errors':[]}
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path=shutil.which('chromium'),headless=True,args=['--no-sandbox']);r['browser_version']=browser.version
 for name,size in [('desktop',{'width':1440,'height':1000}),('mobile',{'width':390,'height':844})]:
  page=browser.new_page(viewport=size);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(html,wait_until='load');page.add_script_tag(content=bootstrap);page.add_script_tag(content=(resources/'common_portal.js').read_text())
  page.wait_for_function("document.getElementById('inventory').textContent.includes('399')");assert page.locator('.card').count()==3
  assert page.locator('.hero').evaluate('(e)=>e.naturalWidth>0')
  page.locator('button[type=submit]').click();page.wait_for_function("document.getElementById('status').textContent.includes('context_available')")
  assert page.locator('#results .result').count()>0
  page.screenshot(path=str(a.out/f'portal_{name}.png'),full_page=True)
  overflow=page.evaluate('document.documentElement.scrollWidth>window.innerWidth')
  if overflow:errors.append('horizontal page overflow')
  page.locator('#budget').fill('512');page.locator('button[type=submit]').click();page.wait_for_function("document.getElementById('status').textContent.includes('budget_exhausted')")
  page.locator('#question').fill('zxqv7788');page.locator('button[type=submit]').click();page.wait_for_function("document.getElementById('status').textContent.includes('no_match')")
  page.locator('#packet summary').click()
  with page.expect_download() as di:page.locator('#download').click()
  assert di.value.suggested_filename=='atlas-context.json'
  r['views'].append({'name':name,'viewport':size,'node_count':3,'artwork_loaded':True,'context_assembled':True,'budget_exhaustion':True,'no_match':True,'download':True,'horizontal_overflow':overflow,'errors':errors});r['errors']+=errors;page.close()
 browser.close()
r['result']='failed' if r['errors'] else 'passed';(a.out/'offline_browser.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
