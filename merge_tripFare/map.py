#!/usr/bin/python
import sys

FARE_COL = 11

for line in sys.stdin:
    l = line.split(",")
    if l[0] == 'medallion':
       continue
    elif l[0] != "medallion":
	    if len(l) == FARE_COL:
             if l[4] == 'CRD' or l[4] == 'UNK':
                 key = str(l[0]+','+l[1]+','+l[2]+','+l[3])
                 l[-1] = l[-1].rstrip("\n")
                 value = "\t".join(l[4:])
                 value.rstrip("\n")
             else:
                continue
	    else:
		     key = str(l[0]+','+l[1]+','+l[2]+','+l[5])
		     l[-1] = l[-1].rstrip('\n')
		     value = "\t".join(l[3:5]+l[6:])
		     value.rstrip("\n")
    print "%s\t%s" %(key, value)
