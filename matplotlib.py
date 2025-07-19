#!/usr/bin/env python
# coding: utf-8

# # PLOTTING SINGLE AND MULTIPLE PLOTS USIND SUBPLOTS, COLOUR AND HSAPCE WITH MATPLOTLIB
#importing required libries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')

#defining parameters for plots
temp_data = [24, 25,66,77,85,58,36,86,42,90]
wind_data = [45,86,87,56,4,6,7,23,9,20]
time_hrs = [1,2,3,4,5,6,7,8,9,10]
humidity_data = [73,68,77,87,91,65,98,35,46,78]
precipitation_data = [26,78,45,33,45,56,78,95,23,14]

#drawing plots against time_hrs
plt.figure(figsize=(8,4))
plt.subplots_adjust(hspace=.25)
plt.subplot(1,2,1)
plt.title('Temp')
plt.plot(time_hrs,temp_data, color = 'b', linestyle= '-', linewidth=1)
plt.subplot(1,2,2)
plt.title('Wind')
plt.plot(time_hrs,wind_data, color = 'r', linestyle= '-', linewidth=1)

plt.figure(figsize=(6,6))
plt.subplots_adjust(hspace=.30)
plt.subplot(2,1,1)
plt.title('Humidity')
plt.plot(time_hrs, humidity_data, color = 'g', linestyle= '-', linewidth=1)
#plt.subplot(2,1,2)
plt.title('Precipitate')
plt.plot(time_hrs, precipitation_data, color = 'b', linestyle= '-', linewidth=1)

plt.figure(figsize=(9,9))
plt.subplots_adjust(hspace=.3)
plt.subplot(2,2,1)
plt.title('Temp (F)')
plt.plot(time_hrs,temp_data, color = 'b', linestyle= '-', linewidth=1)
plt.subplot(2,2,2)
plt.title('Wind (MPH)')
plt.plot(time_hrs,wind_data, color = 'r', linestyle= '-', linewidth=1)
plt.subplot(2,2,3)
plt.title('Humidity (%)')
plt.plot(time_hrs, humidity_data, color = 'g', linestyle= '-', linewidth=1)
plt.subplot(2,2,4)
plt.title('Precipitate (%)')
plt.plot(time_hrs, precipitation_data, color = 'y', linestyle= '-', linewidth=1)


# # HISTOGRAM AND SCATTER PLOTS USING MATPLOT LIB


# import the boson data set from the sklearn library
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)

# import matplotlib
import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')
# This is too view the plot in jupyter notebook


# Load the data
print(housing.DESCR)


# DEFINING THE DATA SETS X
X = housing.data


# DEFINING THE DATA SETS Y
Y = housing.target

# PLOT HISTOGRAM
style.use('ggplot')
plt.figure(figsize=(7,7))
plt.hist(Y, bins=50)
plt.xlabel('price in 1000s USD')
plt.ylabel('number of houses')
plt.show()

# SCATTER PLOT
style.use('ggplot')
plt.figure(figsize=(9,9))
plt.scatter(housing.data[:,5], housing.target)
plt.ylabel('price in 1000s')
plt.xlabel('number of houses')
plt.show()


# # GENERATE A HEAT MAP USING MATPLOTLIB

# import matplot lib
import matplotlib.pyplot as plt
# import seaborn lib>
import seaborn as sns


# To ahow plot notebook
get_ipython().run_line_magic('matplotlib', 'inline')
sns.get_dataset_name()

# Load flights data from sns dataset (built in)
flight_data = sns.load_dataset('flights')

# view top 5 records
flight_data.head()
