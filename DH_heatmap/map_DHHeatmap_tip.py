#! /usr/bin/python
#groupby day and hour 

import sys
import string
import datetime

for line in sys.stdin:
	l = line.strip().split('\t')
        tips = l[0].strip()
        total = l[1].strip()
        p = float(tips)/float(total)
	time = l[2].strip()
	date = datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
	week_day = date.weekday() + 1
	hour = date.hour
	if hour == 0:
		hour = 24
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
	k = str(week_day) + hour
	print '%s\t%s' %(k,p)

	
