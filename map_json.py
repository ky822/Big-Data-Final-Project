import json
import os
import csv

zipcode_list = []
path  = os.getcwd()
map_json = open(path+'/NYCZIP.json','r')

map = json.load(map_json)['features']
for zip in xrange(len(map)):
	map_dict = {} 
	map_dict['zipcode'] = map[zip]['properties']['postalCode'].encode('ascii')
	map_dict['coordinates'] = map[zip]['geometry']['coordinates'][0]
	map_dict['borough'] = map[zip]['properties']['borough'].encode('ascii')
	zipcode_list.append(map_dict)
keys = zipcode_list[0].keys()
with open('zipcode_list.csv','wb') as output_file:
	dict_writer = csv.DictWriter(output_file,keys)
	dict_writer.writeheader()
	dict_writer.writerows(zipcode_list)

#print len(map)
#print map[0]['properties']['borough']
#print map[0]['properties']['postalCode']
#print map[0]['geometry']['coordinates'][0]
#print len(map[0]['geometry']['coordinates'][0])
#print map[1]
print 'job done!'
