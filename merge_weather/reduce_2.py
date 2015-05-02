#/usr/bin/python

import sys

current_key = None
current_value = 0
val = []

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    if key == current_key:
        val.append(value)
    else:
        if current_key:
           assert(len(val) == 2)
           print key + '\t' + val[0] +'\t'+ val[1]
        current_key = key
        val = []
        val.append(value)

print key + '\t' + val[0] + '\t'+ val[1]
