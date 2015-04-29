#!/usr/bin/python
"""Input: TripFareMerged Dataset
   Ouput: (Key, value) = (four shared attributes, tips, dropoff_long, dropoff_lat)
"""

import sys


for line in sys.stdin:
    key, values = line.strip().split('\t', 1)
    tips = values.strip().split('\t')[14]
    location = values.strip().split('\t')[8: 10]
    location = '\t'.join(location)

    print key + '\t' + tips + '\t' + location

