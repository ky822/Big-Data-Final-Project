#!/usr/bin/python


"""Input file = merged_trip_fare
   Key = Date
   Value = tips, total_amount [subject to change]
"""

import sys


for line in sys.stdin:
    line = line.strip().split('\t', 1)
    try:
       #tot_amount = float(line[1].strip().split('\t')[16])
       date = line[0].strip().split(',')[-1][:10]
       tips = float(line[1].strip().split('\t')[14])
       #perc = tips/tot_amount
       print date + '\t' + str(tips)
    except IndexError:
        continue

