

import pandas as pd


boro_info = dict()


nyc_boro = pd.read_csv('/Users/ritali/desktop/ds1004/big-data-final-project/shapefile/zipcode_list.csv')
del nyc_boro['zipcode']



print nyc_boro.shape
print nyc_boro.head(n = 3)


for i in range(nyc_boro.shape[0]):
    boro_info[nyc_boro[borough[i]]] = 
    
