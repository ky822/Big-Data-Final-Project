#!/usr/bin/python

"""Aggregate percentage tgt and avg
"""


import sys

current_date = None
current_perc = 0


for line in sys.stdin:
    line = line.strip().split('\t')
    date = line[0]
    perc = line[1]

    try:
        perc = float(perc)
    except ValueError:
        continue

    if date  == current_date:
        current_perc += perc
        count += 1
    else:
        if current_date:
            current_avg = current_perc / count
	    print "%s\t%.3f" % (current_date, current_avg)
        current_date = date
        current_perc = perc
        count = 1

current_avg = current_perc / count
print "%s\t%.2f" % (current_date, current_avg)
