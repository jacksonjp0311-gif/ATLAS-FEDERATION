from pathlib import Path
import importlib.util,tempfile,unittest
from atlas_forge.common import AtlasStore,ContractError
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('new_node',ROOT/'tools/new_node.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class ScaffoldTests(unittest.TestCase):
 def test_active_scaffold_uses_shared_kernel(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'node';module.scaffold(p,'measurement-atlas','Measurement Atlas');s=AtlasStore(p);self.assertEqual(s.discover()['records'],0);self.assertTrue((p/'data/sources.jsonl').is_file())
 def test_other_domain_blocked(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'node'
   with self.assertRaises(ContractError):module.scaffold(p,'causal-atlas','Causal Atlas')
   self.assertFalse(p.exists())
 def test_no_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(ContractError):module.scaffold(Path(d),'measurement-atlas','Measurement Atlas')
 def test_path_injection(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(ContractError):module.scaffold(Path(d)/'node','../bad','Bad')
