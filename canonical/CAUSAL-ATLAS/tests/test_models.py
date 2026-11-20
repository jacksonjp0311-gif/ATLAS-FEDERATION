import unittest
from fractions import Fraction
from causal_atlas.models import DAG,BinaryModel,ModelError,rational,standardize_binary
from causal_atlas.cases import process_model,casebook,ROWS

class GraphTests(unittest.TestCase):
    def test_chain_open(self):self.assertFalse(DAG(('A','M','Y'),(('A','M'),('M','Y'))).d_separated(['A'],['Y']))
    def test_chain_blocked(self):self.assertTrue(DAG(('A','M','Y'),(('A','M'),('M','Y'))).d_separated(['A'],['Y'],['M']))
    def test_fork_open(self):self.assertFalse(DAG(('Z','A','Y'),(('Z','A'),('Z','Y'))).d_separated(['A'],['Y']))
    def test_fork_blocked(self):self.assertTrue(DAG(('Z','A','Y'),(('Z','A'),('Z','Y'))).d_separated(['A'],['Y'],['Z']))
    def test_collider_closed(self):self.assertTrue(DAG(('A','B','C'),(('A','C'),('B','C'))).d_separated(['A'],['B']))
    def test_collider_conditioned(self):self.assertFalse(DAG(('A','B','C'),(('A','C'),('B','C'))).d_separated(['A'],['B'],['C']))
    def test_collider_descendant(self):self.assertFalse(DAG(('A','B','C','D'),(('A','C'),('B','C'),('C','D'))).d_separated(['A'],['B'],['D']))
    def test_irrelevant_collider_removed(self):self.assertTrue(DAG(('A','B','C','D'),(('A','C'),('B','C'))).d_separated(['A'],['B'],['D']))
    def test_disconnected(self):self.assertTrue(DAG(('A','B'),()).d_separated(['A'],['B']))
    def test_cycle(self):
        with self.assertRaises(ModelError):DAG(('A','B'),(('A','B'),('B','A')))
    def test_unknown_endpoint(self):
        with self.assertRaises(ModelError):DAG(('A','B'),(('A','Z'),))
    def test_self_loop(self):
        with self.assertRaises(ModelError):DAG(('A',),(('A','A'),))
    def test_duplicate_node(self):
        with self.assertRaises(ModelError):DAG(('A','A'),())
    def test_duplicate_edge(self):
        with self.assertRaises(ModelError):DAG(('A','B'),(('A','B'),('A','B')))
    def test_invalid_node(self):
        with self.assertRaises(ModelError):DAG(('A','B;exec'),())
    def test_overlap_sets(self):
        with self.assertRaises(ModelError):DAG(('A','B'),()).d_separated(['A'],['B'],['A'])
    def test_unknown_query(self):
        with self.assertRaises(ModelError):DAG(('A','B'),()).d_separated(['A'],['Z'])
    def test_empty_query(self):
        with self.assertRaises(ModelError):DAG(('A','B'),()).d_separated([],['B'])
    def test_bare_string(self):
        with self.assertRaises(ModelError):DAG(('A','B'),()).d_separated('A',['B'])
    def test_backdoor_valid(self):self.assertTrue(process_model().graph.backdoor('A','Y',['Z'])['valid_under_supplied_graph'])
    def test_backdoor_invalid(self):self.assertFalse(process_model().graph.backdoor('A','Y',[])['valid_under_supplied_graph'])
    def test_backdoor_descendant(self):self.assertFalse(DAG(('A','M','Y'),(('A','M'),('M','Y'))).backdoor('A','Y',['M'])['valid_under_supplied_graph'])
    def test_adjustment_empty(self):self.assertEqual(DAG(('A','Y'),(('A','Y'),)).minimal_backdoor_sets('A','Y',['A','Y']),[[]])
    def test_adjustment_confounder(self):self.assertEqual(process_model().graph.minimal_backdoor_sets('A','Y',['A','Y','Z']),[['Z']])
    def test_unobserved_confounder(self):self.assertEqual(process_model().graph.minimal_backdoor_sets('A','Y',['A','Y']),[])
    def test_max_nodes(self):
        with self.assertRaises(ModelError):DAG(tuple('N'+str(i) for i in range(21)),())
    def test_max_adjustment(self):
        g=DAG(tuple('N'+str(i) for i in range(16)),())
        with self.assertRaises(ModelError):g.minimal_backdoor_sets('N0','N1',g.nodes)
    def test_frozen(self):
        g=DAG(['A','B'],[['A','B']]);self.assertIsInstance(g.nodes,tuple);self.assertIsInstance(g.edges,tuple)
    def test_multiple_endpoints(self):self.assertTrue(DAG(('A','B','C','D'),(('A','C'),('B','D'))).d_separated(['A','C'],['B','D']))

class ModelTests(unittest.TestCase):
    def test_joint_normalizes(self):self.assertEqual(sum(p for _,p in process_model().joint()),1)
    def test_do_normalizes(self):self.assertEqual(sum(p for _,p in process_model().joint({'A':1})),1)
    def test_observational_difference(self):
        m=process_model();self.assertEqual(m.probability({'Y':1},given={'A':1})-m.probability({'Y':1},given={'A':0}),Fraction(-13,50))
    def test_interventional_difference(self):
        m=process_model();self.assertEqual(m.probability({'Y':1},do={'A':1})-m.probability({'Y':1},do={'A':0}),Fraction(1,10))
    def test_ancestor_not_changed(self):self.assertEqual(process_model().probability({'Z':1},do={'A':1}),Fraction(1,2))
    def test_parent_order_declared(self):self.assertEqual(process_model().parents['Y'],('A','Z'))
    def test_two_interventions(self):self.assertEqual(process_model().probability({'Y':1},do={'A':1,'Z':0}),Fraction(9,10))
    def test_do_same_event(self):self.assertEqual(process_model().probability({'A':1},do={'A':1}),1)
    def test_do_contradict_event(self):self.assertEqual(process_model().probability({'A':0},do={'A':1}),0)
    def test_empty_event(self):self.assertEqual(process_model().probability({}),1)
    def test_impossible_condition(self):
        with self.assertRaises(ModelError):process_model().probability({'Y':1},given={'A':0},do={'A':1})
    def test_bad_assignment(self):
        with self.assertRaises(ModelError):process_model().probability({'Y':2})
    def test_bool_assignment(self):
        with self.assertRaises(ModelError):process_model().probability({'Y':True})
    def test_unknown_assignment(self):
        with self.assertRaises(ModelError):process_model().probability({'QQ':1})
    def test_missing_table(self):
        with self.assertRaises(ModelError):BinaryModel(DAG(('A',),()),{})
    def test_missing_parent_row(self):
        with self.assertRaises(ModelError):BinaryModel(DAG(('A','Y'),(('A','Y'),)),{'A':{'':'1/2'},'Y':{'0':'1/2'}})
    def test_bad_probability(self):
        with self.assertRaises(ModelError):BinaryModel(DAG(('A',),()),{'A':{'':'1.1'}})
    def test_nonfinite(self):
        with self.assertRaises(ModelError):rational(float('nan'))
    def test_bool_probability(self):
        with self.assertRaises(ModelError):rational(True)
    def test_huge_exponent(self):
        with self.assertRaises(ModelError):rational('1e999999999')
    def test_long_number(self):
        with self.assertRaises(ModelError):rational('1'*101)
    def test_decimal_exact(self):self.assertEqual(rational('0.1'),Fraction(1,10))
    def test_model_size(self):
        with self.assertRaises(ModelError):BinaryModel(DAG(tuple('N'+str(i) for i in range(13)),()),{})

class StandardizationTests(unittest.TestCase):
    def test_standardized_effect(self):self.assertEqual(standardize_binary(ROWS,{'easy':'1/2','hard':'1/2'})['standardized_difference'],'1/10')
    def test_causal_not_certified(self):self.assertFalse(standardize_binary(ROWS,{'easy':'1/2','hard':'1/2'})['causal_assumptions_verified'])
    def test_missing_cell(self):
        with self.assertRaises(ModelError):standardize_binary(ROWS[:-1],{'easy':'1/2','hard':'1/2'})
    def test_invalid_count(self):
        rs=[r.copy() for r in ROWS];rs[0]['successes']=81
        with self.assertRaises(ModelError):standardize_binary(rs,{'easy':'1/2','hard':'1/2'})
    def test_no_target(self):
        with self.assertRaises(ModelError):standardize_binary(ROWS,{})
    def test_unnormalized_target(self):
        with self.assertRaises(ModelError):standardize_binary(ROWS,{'easy':1,'hard':1})
    def test_negative_target(self):
        with self.assertRaises(ModelError):standardize_binary(ROWS,{'easy':2,'hard':-1})
    def test_duplicate_group(self):
        with self.assertRaises(ModelError):standardize_binary(ROWS+[ROWS[0]],{'easy':'1/2','hard':'1/2'})
    def test_zero_weight_needs_no_support(self):self.assertEqual(standardize_binary(ROWS[:2],{'easy':1,'hard':0})['standardized_difference'],'1/10')
    def test_no_automatic_interval(self):self.assertIsNone(standardize_binary(ROWS,{'easy':1,'hard':0})['uncertainty_interval'])
    def test_group_field_strict(self):
        rs=[r.copy() for r in ROWS];rs[0]['instruction']='run something'
        with self.assertRaises(ModelError):standardize_binary(rs,{'easy':1,'hard':0})
    def test_casebook(self):self.assertEqual(casebook()['result'],'passed')

if __name__=='__main__':unittest.main()
