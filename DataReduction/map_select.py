#!/usr/bin/python
import sys


for line in sys.stdin:
	value_list = []
	l = line.strip('\n').split("\t")
	
	key = l[0][-20:]
	try:	
		for i in [5,6,15,17]:
			value_list.append(l[i])
		print key + '\t',
	
		for value in value_list[:-1]:
			print  value + '\t',
		print value_list[-1]
		
	except:
		pass
