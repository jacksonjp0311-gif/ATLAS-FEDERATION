"""Offline OpenMCT parser and held-out ARX tests, no publisher raw logs bundled."""
import unittest,random, math, json
from control_atlas.empirical import parse_openmct,validate_openmct_identification,COLUMNS
from control_atlas.methods import ControlInputError


def fake_raw(count=180,constant_pwm=False,jitter=False, duplicate_dmm=True):
    rng=random.Random(110113)
    x=0.;rows=[]
    for k in range(count):
        cmd=100 if constant_pwm else (80 if k//9%2 else 220)
        dt=(20 if not jitter else (3 if k%3 else 100))
        # Prior commanded/applied PWM drives next sample, not the REF column.
        row=[0,x,dt,500,510,cmd,
             0.5, k*.02, 2, k//4 if duplicate_dmm else k]
        rows.append(row)
        x=.6*x+.35*cmd+3+rng.gauss(0,1.)
    return '\n'.join(['Mode, System Identification','Date, 2026-10-12',','.join(COLUMNS)] + [','.join(map(str,row)) for row in rows])

class ParseOpenMCT(unittest.TestCase):
    def test_full(self):
        d=parse_openmct(fake_raw())
        self.assertEqual(d['count'],180)
        self.assertEqual(d['median_dt_ms'],20)
        self.assertEqual(d['dmm_unique_fresh'],45)
        self.assertEqual(d['dmm_duplicate_ids'],135)
        self.assertAlmostEqual(d['times_s'][12],.24)
        self.assertEqual(d['samples'][0]['PWM'],220)
    def test_partial_dmm_missing(self):
        s=fake_raw(50)
        s=s.replace('0.5,0.0,2,0','nan,nan,nan,nan',1)
        self.assertEqual(parse_openmct(s)['dmm_rows_absent'],1)
    def test_malformed_header_reject(self):
        with self.assertRaises(ControlInputError):parse_openmct(fake_raw().replace('PWM','PWM_COMMAND',1))
    def test_blank_dmm_partial_reject(self):
        s=fake_raw(50).replace(',0.5,0.0,2,0',',,,2,0',1)
        with self.assertRaises(ControlInputError):parse_openmct(s)
    def test_bad_loop_interval(self):
        s=fake_raw(50).replace(',20,500,',',0,500,',1)
        with self.assertRaises(ControlInputError):parse_openmct(s)
    def test_bad_pwm_input(self):
        s=fake_raw(50).replace(',220,0.5,',',600,0.5,',1)
        with self.assertRaises(ControlInputError):parse_openmct(s)
    def test_no_clock_invention(self):
        parsed=parse_openmct(fake_raw())
        self.assertIn('not verified clock sync',parsed['limits'][-1])

class HeldoutIdentification(unittest.TestCase):
    def test_model_fit_synthetic_known(self):
        p=parse_openmct(fake_raw())
        r=validate_openmct_identification(p)
        self.assertAlmostEqual(r['model']['a'],.6,delta=.03)
        self.assertAlmostEqual(r['model']['b'],.35,delta=.02)
        self.assertAlmostEqual(r['model']['c'],3,delta=1)
        self.assertEqual(r['validation_transitions'],54)
        self.assertLess(r['performance']['heldout_one_step_rmse_rpm'],r['performance']['heldout_persistence_rmse_rpm'])
        self.assertEqual(r['status'],'descriptive_prediction_evaluated_not_causal_or_safety_identification')
    def test_no_excitation_refusal(self):
        p=parse_openmct(fake_raw(constant_pwm=True))
        with self.assertRaisesRegex(ControlInputError,'PWM excitation'):validate_openmct_identification(p)
    def test_jitter_refusal(self):
        p=parse_openmct(fake_raw(jitter=True))
        with self.assertRaisesRegex(ControlInputError,'sample period'):validate_openmct_identification(p)
    def test_insufficient_samples(self):
        p=parse_openmct(fake_raw(35))
        with self.assertRaises(ControlInputError):validate_openmct_identification(p)
    def test_train_fraction_validation(self):
        p=parse_openmct(fake_raw())
        for frac in [.1,.9,float('nan')]:
            with self.subTest(frac=frac),self.assertRaises(ControlInputError):validate_openmct_identification(p,train_fraction=frac)
    def test_heldout_is_chronological(self):
        p=parse_openmct(fake_raw())
        r=validate_openmct_identification(p)
        self.assertEqual(r['training_transitions']+r['validation_transitions'],179)
        self.assertIn('one-step', 'one-step')

if __name__=='__main__':unittest.main()
