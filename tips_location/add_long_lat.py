# -*- coding:utf-8 -*-

import sys

MANHATTAN_LONG = -73.9597
MANHATTAN_LAT = 40.7903

BRONX_LONG = -73.8860
BRONX_LAT = 40.8373

STATEN_LONG = -74.1448
STATEN_LAT = 40.5763

QUEENS_LONG = -73.8667
QUEENS_LAT = 40.7500

BROOKLYN_LONG = -73.9903
BROOKLYN_LAT = 40.6928



for line in sys.stdin:
    line = line.strip()
    l = line.split('\t')
    boro = l[-1]
    if boro == 'Manhattan':
        print l[1] + ',' + str(MANHATTAN_LONG) + ',' + str(MANHATTAN_LAT) + ',' + boro
    elif boro == 'Bronx':
        print l[1].strip() + ',' + str(BRONX_LONG) + ',' + str(BRONX_LAT) + ',' + boro
    elif boro == 'Staten Island':
        print l[1].strip() + ',' + str(STATEN_LONG) + ',' + str(STATEN_LAT) + ',' + boro
    elif boro == 'Queens':
        print l[1].strip() + ',' + str(QUEENS_LONG) + ',' + str(QUEENS_LAT) + ',' +  boro
    elif boro == 'Brooklyn':
        print l[1].strip() + ',' + str(BROOKLYN_LONG) + ',' + str(BROOKLYN_LAT) + ',' +  boro
    else:
        continue
