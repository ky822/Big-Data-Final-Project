# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import pandas as pd
import operator
import seaborn as sns
import numpy as np


def tips_amount(data):
    tips = dict()
    types = set(data.loc[:, 4])
    for t in types:
        tip = data[data.loc[:, 4] == t].loc[:, 1]
        avg = sum(tip)/ tip.shape[0]
        tips[t] = avg

    return tips



def main():
    boro = '/users/ritali/desktop/ds1004/label_data'
    boro_dat = pd.read_table(boro, sep = '\t', header = None)

    boro_tips = tips_amount(boro_dat)
    #del boro_tips['None']
    sorted_boro = sorted(boro_tips.items(), key = operator.itemgetter(1))
    values = np.array([sorted_boro[i][1] for i in range(6)])
    label = np.array([sorted_boro[i][0] for i in range(6)])

    current_color = sns.color_palette()
    sns.barplot(label, values, palette = current_color)

    #pos = [i + 0.5 for i in range(5)]
    #plt.barh(pos, values, align = 'center')
    #plt.yticks(pos, label)
    plt.xlabel('tips average')
    plt.title('Tips Average for Each Borough')
    plt.grid(True)

    sns.plt.show()


if __name__ == "__main__":
   main()
