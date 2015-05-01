

import pandas as pd


boro_info = dict()


nyc_boro = pd.read_csv('/Users/ritali/desktop/ds1004/big-data-final-project/shapefile/zipcode_list.csv')
del nyc_boro['zipcode']



for i in range(nyc_boro.shape[0]):
    boro_info[nyc_boro[borough[i]]] = 








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
                        xintes = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside
