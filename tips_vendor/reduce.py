#!/usr/bin/python
"""Input: key, val = vendor, tips
   output: vendor, tips amount
"""

import sys
import operator


current_vendor = None

for line in sys.stdin:
    vendor, tips = line.strip().split('\t')

    try:
        tips = float(tips)
    except ValueError:
        continue

    if vendor == current_vendor:
       current_tips += tips

    else:
        if current_vendor:
            print current_vendor + '\t' + str(current_tips)
        current_vendor = vendor
        current_tips = tips


print current_vendor + '\t' + str(current_tips)
