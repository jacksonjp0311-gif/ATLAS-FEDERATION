"""Finite evidence fixtures, no imports of manufacturing/real hardware tooling."""
import json,hashlib,unittest
from pathlib import Path
from computer_atlas.spec import SpecMachine
from computer_atlas.microcoded import MicrocodedMachine
from computer_atlas.isa import assemble,disassemble

E=Path(__file__).resolve().parents[1]

class TestEvidence(unittest.TestCase):
    def test_casebook_count(self):
        d=json.loads((E/'evidence/CASE_INDEX_v0.1.0.json').read_text())
        self.assertEqual(d['count'],18)
    def test_all_chapters_present(self):
        d=json.loads((E/'evidence/chapter_index.json').read_text())
        self.assertEqual(d['chapter_count'],24)
        self.assertEqual(len(list((E/'docs/chapters').glob('*.md'))),24)
        for c in d['chapters']:self.assertTrue((E/c['file']).is_file())
    def test_machine_contract_json(self):
        d=json.loads((E/'evidence/AT8_ISA_SPEC_v0.1.0.json').read_text())
        self.assertEqual((d['register_count'],d['instruction_bytes'],len(d['operations'])),(4,2,16))
        self.assertTrue(d['not_risc_v_beta_hack'])
    def test_golden_programs(self):
        d=json.loads((E/'evidence/GOLDEN_PROGRAMS_v0.1.0.json').read_text())
        self.assertEqual(d['count'],3)
        for p in d['programs']:
            code=bytes.fromhex(p['rom_hex'])
            self.assertEqual(hashlib.sha256(code).hexdigest(),p['rom_sha256'])
            inputs={int(k):v for k,v in p['input_tapes'].items()}
            s=SpecMachine(code,inputs).run(100)
            m=MicrocodedMachine(code,inputs).run(100)
            self.assertEqual(s['snapshot'],m['snapshot'])
            self.assertEqual(s['snapshot']['regs'],tuple(p['expected_registers']))
            self.assertEqual(s['snapshot']['output'],tuple(tuple(x) for x in p['output_tape']))
            self.assertEqual(assemble(disassemble(code)),code)
    def test_science_gates_explicit(self):
        text=(E/'docs/SCOPED_V1_GATES.md').read_text().lower()
        self.assertIn('hold',text)
        self.assertIn('fabricated/transistor',text)

if __name__=='__main__':unittest.main()
