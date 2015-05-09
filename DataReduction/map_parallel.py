#!/usr/bin/python
import sys


for line in sys.stdin:
	value_list = []
	l = line.strip('\n').split("\t")
	
	key = l[0].split(',')[2]
	try:	
		for i in [4,15]:
			value_list.append(l[i])
		print key + '\t',
	
		for value in value_list[:-1]:
			print  value + '\t',
		print value_list[-1]
		
	except:
		pass
