#!/usr/bin/python

import sys
import datetime

for line in sys.stdin:
    line = line.strip().split('\t', 1)
    key, pickup_datetime = line[0].strip().split(',')[:3], line[0].strip().split(',')[-1]
    new_time = datetime.datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S')
    trip_time_in_secs = line[1].strip().split('\t')[4]
    try:
        time_secs = int(trip_time_in_secs)
    except ValueError:
        continue
    new_time = new_time + datetime.timedelta(0, int(0.5 * time_secs))
    hour = str(new_time.hour)
    tip_amount = line[1].strip().split('\t')[14]
    print hour + '\t' + tip_amount
