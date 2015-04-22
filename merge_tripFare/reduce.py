#!/usr/bin/python
import sys
last_key = None
NUM_FARE_VAL = 7

for line in sys.stdin:
    key, value = line.strip().split("\t")[0], line.strip().split("\t")[1:]
    if value[-2] == '' or value[-1] == '':
      print "True"
    else:
      continue
    """
    if len(value[-1]) < 1:
        print "=========++++++++++++=============="
        continue
    else:
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
"""