import pandas as pd
import matplotlib.pyplot as plt
import numpy
import seaborn as sns

data = pd.read_csv('week.txt','\t')
data = data.ix[:,0:18]

data.columns = ['Key', 'rate_code', 'store_and_fwd_flag', 'dropoff_datetime','passenger_count', 'trip_time_in_secs','trip_distance', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount', 'surcharge', 'mta_tax','tip_amount', 'tolls_amount', 'total_amount']

dat = data[['Key','trip_time_in_secs','trip_distance','tip_amount','total_amount']]

dat['tip_perc'] = map(float,dat.tip_amount/dat.total_amount)

def distance_classification(distance):
	if distance <= 1.18:
		return 'Short'
	elif 1.18 < distance <= 1.97:
		return "Medium Short"
	elif 1.97 < distance <= 3.5:
		return "Medium"
	else:
		return 'Long'

dat['distance_label']= map(distance_classification,dat.trip_distance)

def hist_distance():
	dat.groupby('distance_label').tip_perc.mean().plot(kind='bar')
	plt.title('Tip Percentage v.s Trip Distance')
	plt.savefig('hist')

hist_distance()

def time_classification(time):
	if time <=360:
		return "Short_Time"
	elif 360 < time <=592:
		return "Medium_Short_Time"
	elif 592 < time <= 900:
		return "Medium_Time"
	else:
		return "Long_Time"

dat['Time_Label']=map(time_classification,dat.trip_time_in_secs)

def hist_timeLabel():
	dat.groupby('Time_Label').tip_perc.mean().plot(kind='bar')
	plt.title('Tip Percentage v.s Trip Time')
	plt.savefig('hist_time')

hist_timeLabel()


#print dat.tip_perc.describe()


def tip_label(percentage):
	if percentage <= 0.1:
		return 'Low_Level_Tipping'
	elif 0.1 < percentage <= 0.2:
		return 'Medium_Level_Tipping'
	else:
		return "High_Level_Tipping"
					        
dat['tip_Label'] = map(tip_label,dat.tip_perc)
#print dat.tip_Label.describe()

def pie_chart():
	dat.groupby('tip_Label').tip_perc.count().plot(kind='pie',autopct = '%.2f',fontsize =20, figsize=(6,6))
	plt.title("Tipping Level Compostion")
	plt.savefig('pie_chart')

pie_chart()

tclass = dat.groupby(['Time_Label','tip_Label']).size().unstack()


tclass['Total'] = tclass.High_Level_Tipping+tclass.Low_Level_Tipping+tclass.Medium_Level_Tipping
tclass['MS'] = tclass.Low_Level_Tipping+tclass.Medium_Level_Tipping
tclass_nor = (1. * tclass.T / tclass.T.sum()).T
tclass_nor.Time_Label = tclass.index
tclass.Time_Label = tclass.index
tclass.reset_index(level=0, inplace=True)
tclass_nor.reset_index(level=0, inplace=True)

#print tclass
tclass.to_csv('tclass')
tclass_nor.to_csv('tclass_nor')
