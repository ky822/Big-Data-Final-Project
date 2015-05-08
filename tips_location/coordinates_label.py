# -*- coding: utf-8 -*-
import pandas as pd
import sys

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y<= max(p1y, p2y):
                if x<= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def parse_coord(c):
    coord = []
    c = c.translate(None, '[],')
    c = c.split(' ')
    for i in range(0, len(c), 2):
        coord.append([float(c[i]), float(c[i + 1])])
    return coord

def label(location, m):
    for k in m.keys():
      for val in m[k]:
        if point_inside_polygon(location[0], location[1], val):
           print val
           return k

def main():
    nyc_boro = pd.read_csv('/users/ritali/desktop/ds1004/big-data-final-project/shapefile/zipcode_list.csv')
    del nyc_boro['zipcode']
    del nyc_boro['length']
    boro_info = {'Queens': [], 'Bronx': [], 'Staten Island': [], 'Manhattan': [], 'Brooklyn': []}

    for i in range(nyc_boro.shape[0]):
        boro_info[nyc_boro.borough[i]].append(parse_coord(nyc_boro.coordinates[i]))


    for line in sys.stdin:
        val = line.strip().split('\t')
        location = [float(val[-2]), float(val[-1])]
        if 0 not in location:
           boro = label(location, boro_info)
           if str(boro) != None:
              print key + '\t' + val + '\t' + str(boro)



if __name__ == "__main__":
    main()
