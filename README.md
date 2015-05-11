# Big-Data-Final-Project

# Introduction

- This project focuses on analyzing the tipping behavior using NYC cab data together 
  with weather and borough boundary data.

- The three main datasets we worked with are:
  TripFareJoin for 2012
  Weather in 2012
  Borough Boundary 


- We have 9 folders that each serves different purposes.
  DH_headmap
  DataReduction
  GRAPH
  merge_tripfare
  merge_weather
  shapefile
  tips_location
  tips_pickuptime
  tips_vendor



# Instruction

- tips_pickuptime:
  This folder perform analysis on average tipping amount v.s. hour of the day.
  
  MapReduce: input > reduced data with pickuptime, tips, total_amount, trip_in_secs, trip_distance
             output >  hour with corresponding tips average. 

  plot.py: input > MapReduce output
           output > produce the linear plot.

- tips_locaiton:
  data_proc.py: input > TripFareJoin 
                output > tips, total, dropofftime, location
  data_print.py: input == output == output of data_proc.py
  coordinates_label.py: Label each trip with corresponding borough name
                input > origianl values with additional columns for borough
  plot.py: input > labeled data
           output > bar plot


- merge_weather:
  map_1.py: input > TripFareJoin
            output > Modified date format, tips
  reduce_1.py: input > date, tips
               output > date, avg_tips
  map_2.py: input > weather data, reduce_2.py output
            output > date, values
  reduce_2.py: input > date, values
               output > date, combined values


- tips_vendor:
  map.py: input >  TripFareJoin
          output >  VendorID, tips
  reduce.py: input > map.py output
             output > vendor, tips total

- Data Dimension Reduction:
  map_select.py > pickup_dates, trip in secs, trip distance, tip amout, total amount
  reduce_select.py > pickup_dates, trip in secs, trip distance, tip amout, total amount

- Folder Graph:
  updated_graph.py:
  Inputs: selected_data
  Output: pie chart, bar plots, and stacked bar plots

  weathergraph.ipynb:
  inputs:weather merged data
  outputs: 1) Time-Series plot of tip amount v.s Temperature 2) plot of precipitation v.s tip amount 3) wind speed v.s tip amount
 
- DH_heatmap:
  map_DHHeatmap.py:
  Input > TripFareJoin
  Output > weekday + hour, count
  reduce_DHHeatmap.py:
  Input > map_DHHeatmap.py output
  Output > weekday,hour, sum of count

  DHHeat_count.html:
  Input > reduce_DHHeatmap.py output (a .tsv table)
  Output > Day/Hour Heat Map (Open in browsers)

- R_map:
  density_map.R:
  Input > TripFareJoin labeled with boroughs
  OUtput > Density maps of different areas in NYC in different weekdays and weekends

- shapefile:
  map_json.py:
  Input > NYCZIP.json and zipcode_list.csv
  Output > the shape file in tabel containing each zipcode shape
