
# coding: utf-8

# In[100]:

import pandas as pd
import matplotlib.pyplot as plt 
import numpy 
import seaborn as sns


# In[18]:

test = pd.read_csv('trip_fare.txt','\t')


# In[237]:

data = pd.read_csv('1_month_merged.txt','\t')


# In[240]:

data = data.ix[:, 0:18]


# In[241]:


data.columns = ['Key', 'rate_code', 'store_and_fwd_flag', 'dropoff_datetime', 
               'passenger_count', 'trip_time_in_secs', 'trip_distance', 'pickup_longitude', 'pickup_latitude',
                'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount', 'surcharge', 'mta_tax', 
                'tip_amount', 'tolls_amount', 'total_amount']



# In[243]:

data_interest = data[['Key','trip_time_in_secs','trip_distance','tip_amount','total_amount']]


# In[245]:

data_interest['tip_percentage'] = map(float, data_interest.tip_amount/data_interest.total_amount)


# In[248]:

def distance_classification(distance):
    if distance <= 1.18:
        return 'Short'
    elif 1.18 < distance <= 1.97:
        return 'medium short'
    elif 1.97 < distance <= 3.5:
        return 'medium'
    else:
        return "Long"
    
data_interest['Distance_Label'] = map(distance_classification, data_interest.trip_distance)
    


# In[301]:

def hist_distance():
    data_interest.groupby('Distance_Label').tip_percentage.mean().plot(kind='bar')


# In[250]:

def time_classification(time):
    if time <= 360:
        return 'Short'
    elif 360 < time <= 592:
        return 'medium short'
    elif 592 < time <= 900:
        return 'medium'
    elif 900 < time <= 10000:
        return "long"
    
data_interest['Time_Label'] = map(time_classification, data_interest.trip_time_in_secs)


# In[303]:

def hist_timeLabel():
    data_interest.groupby('Time_Label').tip_percentage.mean().plot(kind='bar')


# In[252]:

def tip_label(percentage):
    if percentage <= 0.1:
        return 'Low'
    elif 0.1 < percentage <= 0.2:
        return 'Medium'
    else:
        return "High"
    
data_interest['tip_Label'] = map(tip_label, data_interest.tip_percentage)


# In[304]:

def pie_chart():
    data_interest.groupby('tip_Label').tip_percentage.count().plot(kind='pie',autopct = '%.2f',fontsize =20, figsize=(6,6))
    plt.title("Tipping Level")


# In[ ]:




# In[256]:

tclass = data_interest.groupby(['Time_Label','tip_Label']).size().unstack()
tclass['Total'] = tclass.High+tclass.Low+tclass.Medium
tclass['MS'] = tclass.Low+tclass.Medium
tclass_nor = (1. * tclass.T / tclass.T.sum()).T
tclass_nor.Time_Label = tclass.index
tclass.Time_Label = tclass.index
tclass.reset_index(level=0, inplace=True)
tclass_nor.reset_index(level=0, inplace=True)


# In[305]:

def stacked_timeLabel():
    #Set general plot properties
    plt.subplot(121)
    sns.set_style("white")
    sns.set_context({"figure.figsize": (24, 10)})

    #Plot 1 - background - "total" (top) series
    sns.barplot(x = tclass.Time_Label, y = tclass.Total, color = "#4168B7")

    #Plot 3 - overlay - "medium" series
    bottom_plot2 = sns.barplot(x = tclass.Time_Label, y = tclass.MS, color = "#0000A3")

    #Plot 2 - overlay - "bottom" series
    bottom_plot1 = sns.barplot(x = tclass.Time_Label, y = tclass.Medium, color = "mediumseagreen")

    topbar = plt.Rectangle((0,0),1,1,fc="#4168B7", edgecolor = 'none')
    bottombar = plt.Rectangle((0,0),1,1,fc='#0000A3',  edgecolor = 'none')
    mediumbar = plt.Rectangle((0,0),1,1,fc='mediumseagreen',  edgecolor = 'none')
    l = plt.legend([bottombar, mediumbar, topbar], ['Low', 'Medium','High'], loc='best', ncol = 3, prop={'size':14})
    l.draw_frame(True)


    #Optional code - Make plot look nicer
    sns.despine(left=True)
    bottom_plot1.set_ylabel("Tipping Level Count")
    bottom_plot1.set_xlabel("Trip Duration Level")

    #Set fonts to consistent 16pt size
    for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
                 bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
        item.set_fontsize(10)
    plt.title('Tipping Level Against Trip Time')

    plt.subplot(122)
    sns.set_style("white")
    sns.set_context({"figure.figsize": (24, 10)})

    #Plot 1 - background - "total" (top) series
    sns.barplot(x = tclass_nor.Time_Label, y = tclass_nor.Total, color = "#4168B7")

    #Plot 3 - overlay - "medium" series
    bottom_plot2 = sns.barplot(x = tclass_nor.Time_Label, y = tclass_nor.MS, color = "#0000A3")

    #Plot 2 - overlay - "bottom" series
    bottom_plot1 = sns.barplot(x = tclass_nor.Time_Label, y = tclass_nor.Medium, color = "mediumseagreen")

    topbar = plt.Rectangle((0,0),1,1,fc="#4168B7", edgecolor = 'none')
    bottombar = plt.Rectangle((0,0),1,1,fc='#0000A3',  edgecolor = 'none')
    mediumbar = plt.Rectangle((0,0),1,1,fc='mediumseagreen',  edgecolor = 'none')


    #Optional code - Make plot look nicer
    sns.despine(left=True)
    bottom_plot1.set_ylabel("Fraction")
    bottom_plot1.set_xlabel("Trip Duration Level")

    #Set fonts to consistent 16pt size
    for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
                 bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
        item.set_fontsize(10)
    plt.title('Normalized Tipping Level Against Trip Time')
    plt.show()


# In[300]:

dclass = data_interest.groupby(['Distance_Label','tip_Label']).size().unstack()
dclass['Total'] = dclass.High+dclass.Low+dclass.Medium
dclass['MS'] = dclass.Low+dclass.Medium
dclass_nor = (1. * dclass.T / dclass.T.sum()).T
dclass.Time_Label = dclass.index
dclass.reset_index(level=0, inplace=True)
dclass_nor.reset_index(level=0, inplace=True)


# In[306]:

def stacked_DistanceLabel():
    #Set general plot properties
    plt.subplot(121)
    sns.set_style("white")
    sns.set_context({"figure.figsize": (24, 10)})

    #Plot 1 - background - "total" (top) series
    sns.barplot(x = dclass.Distance_Label, y = dclass.Total, color = "#8C1515")

    #Plot 3 - overlay - "medium" series
    bottom_plot2 = sns.barplot(x = dclass.Distance_Label, y = dclass.MS, color = "#D2C295")

    #Plot 2 - overlay - "bottom" series
    bottom_plot1 = sns.barplot(x = dclass.Distance_Label, y = dclass.Medium, color = "#6495ED")

    topbar = plt.Rectangle((0,0),1,1,fc="#8C1515", edgecolor = 'none')
    bottombar = plt.Rectangle((0,0),1,1,fc='#D2C295',  edgecolor = 'none')
    mediumbar = plt.Rectangle((0,0),1,1,fc='#6495ED',  edgecolor = 'none')
    l = plt.legend([bottombar, mediumbar, topbar], ['Low', 'Medium','High'], loc='best', ncol = 3, prop={'size':14})
    l.draw_frame(True)


    #Optional code - Make plot look nicer
    sns.despine(left=True)
    bottom_plot1.set_ylabel("Tipping Level Count")
    bottom_plot1.set_xlabel("Trip Distance Level")

    #Set fonts to consistent 16pt size
    for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
                 bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
        item.set_fontsize(10)
    plt.title('Tipping Level Against Distance')

    plt.subplot(122)
    sns.set_style("white")
    sns.set_context({"figure.figsize": (24, 10)})

    #Plot 1 - background - "total" (top) series
    sns.barplot(x = dclass_nor.Distance_Label, y = dclass_nor.Total, color = "#8C1515")

    #Plot 3 - overlay - "medium" series
    bottom_plot2 = sns.barplot(x = dclass_nor.Distance_Label, y = dclass_nor.MS, color = "#D2C295")

    #Plot 2 - overlay - "bottom" series
    bottom_plot1 = sns.barplot(x = dclass_nor.Distance_Label, y = dclass_nor.Medium, color = "#6495ED")

    topbar = plt.Rectangle((0,0),1,1,fc="#8C1515", edgecolor = 'none')
    bottombar = plt.Rectangle((0,0),1,1,fc='#D2C295',  edgecolor = 'none')
    mediumbar = plt.Rectangle((0,0),1,1,fc='#6495ED',  edgecolor = 'none')


    #Optional code - Make plot look nicer
    sns.despine(left=True)
    bottom_plot1.set_ylabel("Fraction")
    bottom_plot1.set_xlabel("Trip Distance Level")

    #Set fonts to consistent 16pt size
    for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
                 bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
        item.set_fontsize(10)
    plt.title('Normalized Tipping Level Against Distance')
    plt.show()


# In[ ]:



