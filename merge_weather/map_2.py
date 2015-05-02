#!/usr/bin/python


import sys
import datetime

for line in sys.stdin:
    line = line.strip().split(',')

    if line[0] == "YEARMODA":
        continue
    elif len(line) == 1:
       time = line[0][:10]
       year, month, day = time.strip().split('-')
       perc = line[0][11:]
       print year + month + day + '\t' + perc
    else:
        time = line[0]
        values = [w.strip() for w in line[1: ]]
        values = '\t'.join(values)
        print time + '\t' + values
