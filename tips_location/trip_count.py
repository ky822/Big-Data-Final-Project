# -*- utf-08 -*-




import pandas as pd
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import numpy as np


def main():

    file_path = '/users/ritali/desktop/ds1004/label_data'
    dat = pd.read_table(file_path, sep = '\t', header = None)
    dat.columns = ['key', 'tips', 'long', 'lat', 'boro']
    count_man = dat[dat.boro == 'Manhattan'].shape[0]
    count_bronx = dat[dat.boro == 'Bronx'].shape[0]
    count_queens = dat[dat.boro == 'Queens'].shape[0]
    count_staten = dat[dat.boro == 'Staten Island'].shape[0]
    count_brooklyn = dat[dat.boro == 'Brooklyn'].shape[0]


    
    count = [count_man, count_bronx, count_queens, count_staten, count_brooklyn]
    label = ['Manhattan', 'Bronx', 'Queens', 'Staten Island', 'Brooklyn']
    fig, ax = plt.subplots(1)
    ppl.bar(ax, np.arange(5), count, annotate = True, grid = 'y', xticklabels = label)
    plt.title('Trip Count for Each Borough')
    plt.ylabel('Trip Count')
    plt.xlabel('Borough')
    fig.savefig('trip_count.pdf')    



if __name__ == '__main__':
    main()
