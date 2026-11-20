#!/usr/bin/env python3
"""Synthetic coverage teaching cases. Standard library only, no measured data."""
from pathlib import Path
import sys,json,math
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from measurement_atlas.coverage import coverage_factor,effective_df,expanded_interval,student_t_survival

def run():
    c=lambda n,u,df:dict(name=n,standard_uncertainty=u,sensitivity=1,df=df)
    ws=effective_df([c('repeatability',.02,9),c('bounded contribution',.01,'Infinity')],independent=True)
    interval=expanded_interval(10,ws['combined_standard_uncertainty'],probability=.95,df=ws['effective_df'],unit='mm',model='welch_satterthwaite_approximation')
    results=[{'id':'equal_components','value':float(effective_df([c('a',1,10),c('b',1,10)],independent=True)['effective_df']),'expected':20,'tolerance':1e-12},
      {'id':'eight_df_95','value':coverage_factor(.95,8),'expected':2.306004135204166,'tolerance':1e-10},
      {'id':'normal_95_not_two','value':coverage_factor(.95,'inf'),'expected':1.959963984540054,'tolerance':1e-10},
      {'id':'two_at_four_df','value':1-2*student_t_survival(2,4),'expected':0.8838834764831844,'tolerance':1e-10},
      {'id':'mixed_budget_df','value':float(ws['effective_df']),'expected':14.0625,'tolerance':1e-10}]
    for r in results:r['passed']=abs(r['value']-r['expected'])<=r['tolerance'];r['data_origin']='synthetic_teaching_example'
    return {'result':'passed' if all(r['passed'] for r in results) else 'failed','cases':results,'mixed_budget_interval':interval,
       'actual_measurements':False,'coverage_guarantee':False,'description':'Declared distributions and independent components; physical applicability remains caller responsibility.'}
if __name__=='__main__':
    r=run();print(json.dumps(r,indent=2));sys.exit(0 if r['result']=='passed' else 2)
