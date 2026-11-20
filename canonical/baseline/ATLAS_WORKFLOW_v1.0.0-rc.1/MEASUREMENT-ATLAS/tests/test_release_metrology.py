import copy
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from measurement_atlas.units import parse_unit,convert_quantity
from measurement_atlas.certificates import review_certificate,reported_standard_uncertainty,specification_component
from measurement_atlas.decisions import normal_conformance,guard_band_decision

class UnitTests(unittest.TestCase):
    def cv(self,x,a,b,kind,**kw):return convert_quantity(x,a,b,quantity_kind=kind,**kw)
    def test_length(self):self.assertEqual(self.cv(2,'m','mm','length')['value'],2000)
    def test_mass(self):self.assertAlmostEqual(self.cv(3,'mg','kg','mass')['value'],3e-6)
    def test_force(self):self.assertEqual(self.cv(5,'kg*m/s^2','N','force')['value'],5)
    def test_pressure(self):self.assertEqual(self.cv(2,'kPa','N/m^2','pressure')['value'],2000)
    def test_volume(self):self.assertAlmostEqual(self.cv(2,'L','m^3','volume')['value'],0.002)
    def test_velocity(self):self.assertAlmostEqual(self.cv(36,'km/h','m/s','velocity')['value'],10)
    def test_viscosity(self):self.assertAlmostEqual(self.cv(1,'mm^2/s','m^2/s','kinematic_viscosity')['value'],1e-6)
    def test_temperature_value(self):self.assertAlmostEqual(self.cv(20,'degC','K','temperature')['value'],293.15)
    def test_temperature_difference(self):self.assertEqual(self.cv(-20,'degC','K','temperature',interval=True)['value'],-20)
    def test_temperature_uncertainty_no_offset(self):self.assertEqual(self.cv(20,'degC','K','temperature',uncertainty=0.2)['standard_uncertainty'],0.2)
    def test_temperature_absolute_zero(self):self.assertEqual(self.cv(-273.15,'degC','K','temperature')['value'],0)
    def test_below_absolute_zero(self):
        with self.assertRaises(ValueError):self.cv(-274,'degC','K','temperature')
    def test_affine_algebra_refused(self):
        with self.assertRaises(ValueError):parse_unit('degC/s')
    def test_dimensions_refused(self):
        with self.assertRaises(ValueError):self.cv(1,'m','s','length')
    def test_hz_not_bq(self):
        with self.assertRaises(ValueError):self.cv(1,'Hz','Bq','frequency')
    def test_hz_not_angular_velocity(self):
        with self.assertRaises(ValueError):self.cv(1,'Hz','rad/s','frequency')
    def test_explicit_angular_velocity(self):self.assertAlmostEqual(self.cv(60,'rad/min','rad/s','angular_velocity')['value'],1)
    def test_ratio_not_angle(self):
        with self.assertRaises(ValueError):self.cv(1,'rad','1','ratio')
    def test_ratio_percent(self):self.assertAlmostEqual(self.cv(30,'%','1','ratio')['value'],0.3)
    def test_no_implicit_product(self):
        with self.assertRaises(ValueError):parse_unit('kg m')
    def test_operator_whitespace(self):self.assertEqual(parse_unit('kg * m / s ^ 2').dimensions,parse_unit('N').dimensions)
    def test_unicode_micro(self):self.assertAlmostEqual(self.cv(1,'μm','m','length')['value'],1e-6)
    def test_bad_grammar(self):
        for text in ('','m//s','m/s/','__import__(os)','(kg*m)/s^2','m^99','m^1.5','dB','mph','m**2'):
            with self.subTest(text=text),self.assertRaises(ValueError):parse_unit(text)
    def test_bad_numerics(self):
        for x in (True,float('nan'),float('inf'),'3',None,10**1000):
            with self.subTest(value=str(x)[:20]),self.assertRaises(ValueError):self.cv(x,'m','mm','length')
    def test_negative_uncertainty(self):
        with self.assertRaises(ValueError):self.cv(1,'m','mm','length',uncertainty=-1)
    def test_round_trip(self):
        for a,b,k in [('mm','m','length'),('g','kg','mass'),('kPa','Pa','pressure'),('mV','V','voltage')]:
            for x in (-20,0,3.14,1e6):
                with self.subTest(a=a,x=x):self.assertAlmostEqual(self.cv(self.cv(x,a,b,k)['value'],b,a,k)['value'],x,places=8)

SYNTHETIC_CERT={'certificate_id':'SYNTHETIC-NOT-A-CERTIFICATE-001','source_locator':'examples/synthetic_certificate.json',
    'instrument_id':'SIMULATED-GAUGE','calibration_date':'2026-01-01','quantity_kind':'length','unit':'mm',
    'value':10.0,'uncertainty_kind':'expanded','uncertainty':0.004,'coverage_factor':2,
    'conditions':['Synthetic 20 degC environment'], 'traceability_references':['Synthetic reference; no real traceability'],
    'data_origin':'synthetic_teaching_fixture'}
class CertificateTests(unittest.TestCase):
    def review(self,r):return review_certificate(r,as_of='2026-11-12')
    def test_expanded(self):self.assertEqual(reported_standard_uncertainty(0.4,'expanded',2)['standard_uncertainty'],0.2)
    def test_standard(self):self.assertEqual(reported_standard_uncertainty(0.4,'standard')['standard_uncertainty'],0.4)
    def test_k_not_inferred(self):
        with self.assertRaises(ValueError):reported_standard_uncertainty(0.4,'expanded')
    def test_inconsistent_standard_factor(self):
        with self.assertRaises(ValueError):reported_standard_uncertainty(0.4,'standard',2)
    def test_good_structure_not_verification(self):
        r=self.review(copy.deepcopy(SYNTHETIC_CERT));self.assertEqual(r['status'],'structured_for_review');self.assertFalse(r['authenticity_verified']);self.assertFalse(r['traceability_established']);self.assertIsNone(r['fit_for_intended_use'])
    def test_missing_conditions(self):
        r=dict(SYNTHETIC_CERT);r.pop('conditions');self.assertEqual(self.review(r)['status'],'incomplete')
    def test_missing_coverage_not_95_substitution(self):
        r=dict(SYNTHETIC_CERT);r.pop('coverage_factor');r['coverage_probability']=0.95;self.assertIsNone(self.review(r)['component'])
    def test_due_date(self):
        r=dict(SYNTHETIC_CERT,operator_due_date='2026-02-01');self.assertEqual(self.review(r)['status'],'incomplete')
    def test_no_automatic_expiry(self):self.assertEqual(self.review(SYNTHETIC_CERT)['status'],'structured_for_review')
    def test_future_calibration(self):self.assertEqual(self.review(dict(SYNTHETIC_CERT,calibration_date='2027-01-01'))['status'],'incomplete')
    def test_bad_range(self):self.assertEqual(self.review(dict(SYNTHETIC_CERT,valid_range=[20,30]))['status'],'incomplete')
    def test_unknown_field_refused(self):
        with self.assertRaises(ValueError):self.review(dict(SYNTHETIC_CERT,accept=True))
    def test_wrong_unit_kind(self):self.assertEqual(self.review(dict(SYNTHETIC_CERT,unit='V'))['status'],'incomplete')
    def test_bad_dates(self):
        with self.assertRaises(ValueError):review_certificate(SYNTHETIC_CERT,as_of='yesterday')
    def test_specification_additive(self):
        r=specification_component(5,unit='V',quantity_kind='voltage',percent_reading=0.1,counts=2,resolution=0.001,distribution='uniform',interpretation_basis='synthetic additive specification')
        self.assertAlmostEqual(r['half_width'],0.007);self.assertAlmostEqual(r['standard_uncertainty'],0.007/math.sqrt(3));self.assertFalse(r['complete_measurement_uncertainty'])
    def test_specification_range_requires_input(self):
        with self.assertRaises(ValueError):specification_component(5,unit='V',quantity_kind='voltage',percent_range=1,distribution='uniform',interpretation_basis='fixture')
    def test_specification_distribution_required(self):
        with self.assertRaises(ValueError):specification_component(5,unit='V',quantity_kind='voltage',distribution='normal',interpretation_basis='fixture')
    def test_specification_count_resolution(self):
        with self.assertRaises(ValueError):specification_component(5,unit='V',quantity_kind='voltage',counts=2,distribution='uniform',interpretation_basis='fixture')

class DecisionTests(unittest.TestCase):
    def prob(self,x,u,**kw):return normal_conformance(x,u,unit='mm',quantity_kind='length',model_basis='synthetic declared normal knowledge distribution',**kw)
    def test_center(self):self.assertAlmostEqual(self.prob(0,1,lower=-1,upper=1)['conditional_probability'],0.6826894921370859)
    def test_one_sided_boundary(self):self.assertEqual(self.prob(0,1,upper=0)['conditional_probability'],0.5)
    def test_one_sided_95(self):self.assertAlmostEqual(self.prob(0,1,upper=1.6448536269514722)['conditional_probability'],0.95)
    def test_negative_values(self):
        r=normal_conformance(-5.47,0.05,upper=-5.40,unit='V',quantity_kind='voltage',model_basis='JCGM published illustrative normal model')
        self.assertAlmostEqual(r['conditional_probability'],0.9192433407662,places=12)
    def test_positive_tail(self):self.assertGreater(self.prob(0,1,lower=9,upper=10)['conditional_probability'],0)
    def test_negative_tail_symmetry(self):self.assertEqual(self.prob(0,1,lower=9,upper=10)['conditional_probability'],self.prob(0,1,lower=-10,upper=-9)['conditional_probability'])
    def test_not_a_decision(self):
        r=self.prob(0,1,upper=2);self.assertIsNone(r['decision']);self.assertIsNone(r['global_consumer_risk'])
    def test_model_basis_required(self):
        with self.assertRaises(ValueError):normal_conformance(0,1,upper=2,unit='mm',quantity_kind='length',model_basis='')
    def test_zero_u_refused(self):
        with self.assertRaises(ValueError):self.prob(0,0,upper=2)
    def test_invalid_limits(self):
        for kw in ({},{'lower':1,'upper':1},{'lower':2,'upper':1},{'upper':float('nan')}):
            with self.subTest(kw=kw),self.assertRaises(ValueError):self.prob(0,1,**kw)
    def test_guard_accept(self):
        r=guard_band_decision(0.5,lower=0,upper=1,guard_width=0.1,rule_id='fixture',unit='mm',quantity_kind='length')
        self.assertEqual(r['decision'],'accepted_under_declared_rule');self.assertFalse(r['conformity_certified'])
    def test_guard_not_accepted_is_not_nonconformance(self):
        r=guard_band_decision(0.95,lower=0,upper=1,guard_width=0.1,rule_id='fixture',unit='mm',quantity_kind='length')
        self.assertEqual(r['decision'],'not_accepted_under_declared_rule');self.assertFalse(r['risk_bound_established'])
    def test_guard_inclusive_boundary(self):self.assertEqual(guard_band_decision(0.1,lower=0,upper=1,guard_width=0.1,rule_id='fixture',unit='mm',quantity_kind='length')['decision'],'accepted_under_declared_rule')
    def test_empty_guard_interval(self):
        with self.assertRaises(ValueError):guard_band_decision(0,lower=0,upper=1,guard_width=0.6,rule_id='fixture',unit='mm',quantity_kind='length')
    def test_missing_rule(self):
        with self.assertRaises(ValueError):guard_band_decision(0,upper=1,guard_width=0.1,rule_id='',unit='mm',quantity_kind='length')
    def test_invalid_guard(self):
        with self.assertRaises(ValueError):guard_band_decision(0,upper=1,guard_width=-1,rule_id='fixture',unit='mm',quantity_kind='length')

class CliTests(unittest.TestCase):
    def call(self,*args):
        env=dict(os.environ);env['PYTHONPATH']=str(Path(__file__).resolve().parents[1])
        return subprocess.run([sys.executable,'-m','measurement_atlas',*args],env=env,capture_output=True,text=True,timeout=20)
    def test_convert_cli(self):
        p=self.call('convert',json.dumps({'value':2,'from_unit':'m','to_unit':'mm','quantity_kind':'length'}));self.assertEqual(p.returncode,0);self.assertEqual(json.loads(p.stdout)['value'],2000)
    def test_bad_input_exit2(self):self.assertEqual(self.call('guard-band','{}').returncode,2)
    def test_nan_input_exit2(self):self.assertEqual(self.call('convert','{"value":NaN,"from_unit":"m","to_unit":"mm","quantity_kind":"length"}').returncode,2)
    def test_file_input(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'c.json';p.write_text(json.dumps({'record':SYNTHETIC_CERT,'as_of':'2026-11-12'}))
            r=self.call('certificate-review','--input',str(p));self.assertEqual(r.returncode,0);self.assertFalse(json.loads(r.stdout)['authenticity_verified'])

if __name__=='__main__':unittest.main()
