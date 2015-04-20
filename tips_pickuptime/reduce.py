#!/usr/bin/python
import sys


current_hour = None
current_sum = 0

for line in sys.stdin:
    line = line.strip().split('\t')
    hour = line[0]
    try:
        tips = float(line[1])
    except ValueError:
        continue

    if hour == current_hour:
        current_sum += tips
        count += 1
    else:
        if current_hour:
            current_avg = current_sum / count
            print "%s\t%.2f" % (current_hour, current_avg)
        current_hour = hour
        current_sum = tips
        count = 1


current_avg = current_sum / count
print "%s\t%.2f" % (current_hour, current_avg)
