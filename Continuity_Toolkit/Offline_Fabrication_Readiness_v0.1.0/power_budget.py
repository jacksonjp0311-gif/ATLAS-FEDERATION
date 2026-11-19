#!/usr/bin/env python3
"""Offline blackout energy worksheet; unknowns remain unknown, never guessed."""
from pathlib import Path
import argparse,json,math

INPUT_FIELDS=('printer_avg_watts_measured','printer_peak_watts_measured',
              'laptop_avg_watts_measured','other_avg_watts_measured',
              'expected_job_hours','usable_backup_battery_DC_watt_hours',
              'inverter_efficiency_estimate','total_simultaneous_AC_peak_watts_measured','inverter_continuous_AC_watts',
              'inverter_surge_AC_watts')


def compute(data):
    if not isinstance(data,dict):raise ValueError('JSON object required')
    unknown=[f for f in INPUT_FIELDS if data.get(f) is None]
    if unknown:
        return {'schema':'atlas.blackout-print-power-budget/1',
                'status':'BLOCKED_UNKNOWN_SITE_MEASUREMENTS',
                'missing_fields':unknown,
                'claim':'No backup-power runtime can be inferred without actual measurements and ratings'}
    for k in INPUT_FIELDS:
        x=data[k]
        if type(x) not in (int,float) or not math.isfinite(x) or x<0:
            raise ValueError('finite, nonnegative numeric field required: '+k)
    eff=data['inverter_efficiency_estimate']
    if not 0<eff<=1:raise ValueError('inverter efficiency must be within (0,1]')
    if data['expected_job_hours']<=0:raise ValueError('positive planned print time required')
    avg=data['printer_avg_watts_measured']+data['laptop_avg_watts_measured']+data['other_avg_watts_measured']
    peak=data['total_simultaneous_AC_peak_watts_measured']
    if peak<avg:raise ValueError('measured simultaneous peak cannot be less than total average')
    if avg<=0 or data['usable_backup_battery_DC_watt_hours']<=0:
        raise ValueError('nonzero measured average AC loads and usable backup required')
    load_Wh=avg*data['expected_job_hours']
    req_DC=load_Wh/eff
    available_AC=data['usable_backup_battery_DC_watt_hours']*eff
    good_energy=req_DC<=data['usable_backup_battery_DC_watt_hours']
    continuous_ok=peak<=data['inverter_continuous_AC_watts']
    surge_ok=peak<=data['inverter_surge_AC_watts']
    return {'schema':'atlas.blackout-print-power-budget/1',
        'status':'CALCULATED_FROM_USER_SUPPLIED_DATA_NOT_PHYSICAL_VALIDATION',
        'average_total_AC_watts':round(avg,2),'user_measured_simultaneous_peak_AC_watts':round(peak,2),
        'estimated_print_load_AC_watt_hours':round(load_Wh,2),
        'estimated_battery_draw_DC_watt_hours':round(req_DC,2),
        'estimated_AC_energy_available_watt_hours':round(available_AC,2),
        'energy_budget_within_supplied_backup':good_energy,
        'inverter_continuous_rating_within_supplied_estimated_peak':continuous_ok,
        'inverter_surge_rating_within_supplied_estimated_peak':surge_ok,
        'all_simple_thresholds_met':good_energy and continuous_ok and surge_ok,
        'cautions':['Manufacturer specifications and measured peak/startup loads may exceed these estimates',
          'Battery derating, cable losses, standby consumption, ventilation and safety not included',
          'Do not connect improvised mains wiring or indoor combustion generators',
          'A passing numerical budget is not a tested electrical power system']}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inventory',required=True,type=Path)
    p.add_argument('--out',type=Path)
    args=p.parse_args()
    obj=json.loads(args.inventory.read_text())
    result=compute(obj)
    raw=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.out:args.out.write_text(raw)
    print(raw)

if __name__=='__main__':main()
