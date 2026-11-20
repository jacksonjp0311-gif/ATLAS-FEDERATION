import unittest
from measurement_atlas.budget import uncertainty_budget, type_b
from measurement_atlas.traceability import audit_chain

class BudgetTests(unittest.TestCase):
    def setUp(self):self.c=[{'name':'a','standard_uncertainty':3,'sensitivity':1,'output_unit':'mm'},
                            {'name':'b','standard_uncertainty':4,'sensitivity':1,'output_unit':'mm'}]
    def test_independent(self):self.assertAlmostEqual(uncertainty_budget(self.c,output_unit='mm')['combined_standard_uncertainty'],5)
    def test_anticorrelation(self):self.assertAlmostEqual(uncertainty_budget(self.c,[[1,-1],[-1,1]],output_unit='mm')['combined_standard_uncertainty'],1)
    def test_nonpsd(self):
        with self.assertRaises(ValueError):uncertainty_budget(self.c,[[1,2],[2,1]],output_unit='mm')
    def test_asymmetric(self):
        with self.assertRaises(ValueError):uncertainty_budget(self.c,[[1,0.2],[0.1,1]],output_unit='mm')
    def test_no_units(self):
        with self.assertRaises(ValueError):uncertainty_budget(self.c)
    def test_bad_units(self):
        c=[dict(x) for x in self.c];c[0]['output_unit']='m'
        with self.assertRaises(ValueError):uncertainty_budget(c,output_unit='mm')
    def test_duplicate(self):
        c=[dict(x) for x in self.c];c[1]['name']='a'
        with self.assertRaises(ValueError):uncertainty_budget(c,output_unit='mm')
    def test_typeb(self):
        self.assertAlmostEqual(type_b(3,'uniform')['standard_uncertainty'],3/(3**0.5))
    def test_typeb_bad(self):
        with self.assertRaises(ValueError):type_b(-3,'uniform')
        with self.assertRaises(ValueError):type_b(3,'normal')
    def test_negative_uncertainty(self):
        c=[dict(x) for x in self.c];c[0]['standard_uncertainty']=-1
        with self.assertRaises(ValueError):uncertainty_budget(c,output_unit='mm')

class TraceabilityTests(unittest.TestCase):
    def setUp(self):
        self.nodes=[{'id':'m','kind':'measurement','description':'meter reading','source_url':'local:record'},
                    {'id':'s','kind':'reference_standard','description':'calibration reference','source_url':'local:certificate'}]
        self.edges=[{'child':'m','parent':'s'}]
    def test_path(self):self.assertTrue(audit_chain(self.nodes,self.edges,measurement_id='m')['documented_chain_complete'])
    def test_cycle(self):
        e=self.edges+[{'child':'s','parent':'m'}]
        self.assertFalse(audit_chain(self.nodes,e,measurement_id='m')['documented_chain_complete'])
    def test_missing(self):
        n=[dict(x) for x in self.nodes];n[1].pop('source_url')
        self.assertFalse(audit_chain(n,self.edges,measurement_id='m')['documented_chain_complete'])
    def test_no_reference(self):
        n=[dict(x) for x in self.nodes];n[1]['kind']='workpiece'
        self.assertFalse(audit_chain(n,self.edges,measurement_id='m')['documented_chain_complete'])
    def test_dangling(self):
        with self.assertRaises(ValueError):audit_chain(self.nodes,[{'child':'m','parent':'missing'}],measurement_id='m')
    def test_expired(self):
        n=[dict(x) for x in self.nodes];n[1]['valid_through']='2001-01-01'
        self.assertFalse(audit_chain(n,self.edges,measurement_id='m')['documented_chain_complete'])
