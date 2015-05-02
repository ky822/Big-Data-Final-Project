#! /usr/bin/python

import sys

current_key = None
current_sum = 0

print '\t'.join(['day','hour','value'])
for line in sys.stdin:
	key,value = line.rsplit('\t',1)
	try:
		value = int(value)
	except:
		continue

	if key == current_key:
		current_sum += 1
	else:
		if current_key:
		    if int(current_key[1:])<10:
                        print '%s\t%s\t%s' %(current_key[0],current_key[-1],current_sum)
                    else:
                        print '%s\t%s\t%s' %(current_key[0],current_key[1:],current_sum)	

		current_key = key
		current_sum = value

if int(current_key[1:])<10:
    print '%s\t%s\t%s' %(current_key[0],current_key[-1],current_sum)
else:
    print '%s\t%s\t%s' %(current_key[0],current_key[1:],current_sum)	
