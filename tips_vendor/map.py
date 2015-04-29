#!/usr/bi/python

"""Input: TripFareMerged Dataset
   Output: (Key, Value) = (Vendor ID, tips)
"""

import sys


for line in sys.stdin:
    key, val = line.strip().split('\t', 1)
    vendor = key.strip().split(',')[-2]
    tips = val.strip().split('\t')[14]

    print vendor + '\t' + tips
    
