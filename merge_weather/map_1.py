#!/usr/bin/pyhon


"""Input file = merged_trip_fare
   Key = Date
   Value = tips, total_amount [subject to change]
"""

import sys


for line in sys.stdin:
    line = line.strip().split('\t', 1)
    date = line[0].strip().split(',')[-1][:10]
     
    tips = line[1].strip().split('\t')[14]
    tot_amount = line[1].strip().split('\t')[16]
    tips = float(tips)
    tot_amount = float(tot_amount)
    perc = tips/tot_amount


    print date + '\t' + str(perc)
