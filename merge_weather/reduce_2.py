#/usr/bin/python

import sys

current_key = None
current_value = 0
val = []

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)[0], line.strip().split('\t', 1)[1]
    if key == current_key:
        val.append(value)
    else:
        if current_key:
           assert(len(val) == 2)
           print key + '\t' + val[0] +'\t'+ val[1]
        current_key = key
        val = []
        val.append(value)


<<<<<<< HEAD
if len(val) > 1:
   print key + '\t' + val[0] + '\t'+ val[1]
=======
if len(val) <  1:
   print key + '\t' + val[0] + val[1]
>>>>>>> b1bf1ff8d7f6093a600733ef0d4c5eafbd768575
else:
    print key + '\t' +  val[0]
