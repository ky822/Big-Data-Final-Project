# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


def main():
    file = '/users/ritali/desktop/ds1004/hourly_tips'
    tips_hour = pd.read_table(file, sep = '\t')
    tips_hour.columns = ['hour', 'tips']
    tips_hour = tips_hour.sort(columns = 'hour') 

    g = sns.FacetGrid(tips_hour)
    g.map(sns.plt.plot, 'hour', 'tips')

    plt.xlabel('Hour')
    plt.title('Tips Average for Each Hour')
    plt.ylabel('Avg Tips')
    plt.grid(True)

    sns.plt.show()



if __name__ == '__main__':
    main()

