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

def label(loc, m):
    for k in m.keys():
      for val in m[k]:
        if point_inside_polygon(loc[0], loc[1], val):
           return k


def main():
    nyc_boro = pd.read_csv('/users/ritali/desktop/ds1004/big-data-final-project/shapefile/zipcode_list.csv')
    del nyc_boro['zipcode']
    del nyc_boro['length']
    boro_info = {'Queens': [], 'Bronx': [], 'Staten Island': [], 'Manhattan': [], 'Brooklyn': []}

    for i in range(nyc_boro.shape[0]):
        boro_info[nyc_boro.borough[i]].append(parse_coord(nyc_boro.coordinates[i]))


    for line in sys.stdin:
        key, val = line.strip().split('\t', 1)
        loc = [float(val.split('\t')[1]), float(val.split('\t')[2])]
        boro = label(loc, boro_info)
        print key + '\t' + val + '\t' + boro



if __name__ == "__main__":
    main()
