#!/usr/bin/python


import sys


for line in sys.stdin:
    key, values = line.strip().split('\t', 1)
    tips = values.strip().split('\t')[14]
    location = values.strip().split('\t')[6: 10]
    location = '\t'.join(location)

    print key + '\t' + tips + '\t' + location

