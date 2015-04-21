#!/usr/bin/python
import sys
last_key = None
NUM_FARE_VAL = 7
missing_fare_trip = ['2013000677,2013014407,CMT,2013-01-03 12:27:06','2013001028,2013001025,CMT,2013-01-02 22:44:20','2013006780,2013013640,CMT,2013-01-05 06:20:51','2013009537,2013003948,CMT,2013-01-04 23:28:06','2013009849,2013013116,CMT,2013-01-01 15:16:04']

for line in sys.stdin:
    key, value = line.strip().split("\t")[0], line.strip().split("\t")[1:]
    if key not in missing_fare_trip:
   	if key == last_key:
		if len(value) == NUM_FARE_VAL:
    			fare_value.append(value)
    		else:
    			trip_value.append(value)
    	else:
    		if last_key:
    			for trip in trip_value:
    				for fare in fare_value:
    					print last_key + "\t",
    					for i in trip:
						print i + "\t",
					for f in fare:
						print f + "\t",
					print

    		last_key = key
    		trip_value = []
		fare_value = []
		if len(value) == NUM_FARE_VAL:
    			fare_value.append(value)
   		else:
    			trip_value.append(value)

for trip in trip_value:
	for fare in fare_value:
		print last_key + "\t",
		for i in trip:
			print i + "\t",
		for f in fare:
			print f + "\t",
		print

