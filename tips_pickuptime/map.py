#!/usr/bin/python

import sys
import datetime

for line in sys.stdin:
    pickup_datetime, val = line.strip().split('\t')[0].strip(), line.strip().split('\t')[1: ]
    new_time = datetime.datetime.strptime(pickup_datetime.strip(), '%Y-%m-%d %H:%M:%S')
    trip_time_in_secs = val[0]
    try:
        time_secs = int(trip_time_in_secs)
    except ValueError:
        continue
    new_time = new_time + datetime.timedelta(0, int(0.5 * time_secs))
    hour = str(new_time.hour)
    tip_amount = val[-2] 
    print hour + '\t' + tip_amount
