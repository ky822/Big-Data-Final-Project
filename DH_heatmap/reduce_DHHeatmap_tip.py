#! /usr/bin/python

import sys

current_key = None
current_sum = 0
count = 0

print '\t'.join(['day','hour','value'])
for line in sys.stdin:
	key,value = line.rsplit('\t',1)
	try:
		value = float(value)
	except:
		continue

	if key == current_key:
		current_sum += value
	        count += 1
        else:
		if current_key:
                    mean = float(current_sum)/count
		    if int(current_key[1:])<10:
                        print '%s\t%s\t%s' %(current_key[0],current_key[-1],mean)
                    else:
                        print '%s\t%s\t%s' %(current_key[0],current_key[1:],mean)	

		current_key = key
                current_sum = 0
                count = 1
		current_sum += value

mean = float(current_sum)/count
if int(current_key[1:])<10:
    print '%s\t%s\t%s' %(current_key[0],current_key[-1],mean)
else:
    print '%s\t%s\t%s' %(current_key[0],current_key[1:],mean)	
