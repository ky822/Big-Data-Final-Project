#!/usr/bin/python
import sys
last_key = None
NUM_FARE_VAL = 7


for line in sys.stdin:
    key, value = line.strip().split("\t")[0], line.strip().split("\t")[1:]
    if key == last_key:
		if len(value) == NUM_FARE_VAL:
    			fare_value.append(value)
    		else:
    			trip_value.append(value)
    else:
   		if last_key:
    			for trip in trip_value:
    				for fare in fare_value:
					TRIP = []
					FARE = []
					for i in trip:
						TRIP.append(i)
					for f in fare:
						FARE.append(f)
					test = '\t'.join([last_key]+TRIP+FARE).split('\t')
    					if len(test) == 18:
						print last_key,
    						for i in trip:
							print "\t" + i,
						for f in fare:
							print '\t' + f,
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
		TRIP = []
		FARE = []
		for i in trip:
			TRIP.append(i)
		for f in fare:
			FARE.append(f)
		test = '\t'.join([last_key]+TRIP+FARE).split('\t')
		if len(test) == 18:
			print last_key,
			for i in trip:
				print "\t" + i,
			for f in fare:
				print '\t' + f,
			print
