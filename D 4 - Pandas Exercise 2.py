# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import csv

# Ex 1 Set your home directory
#import the two vehicle data sets name them as veh1 and veh2
f=open('C:\\Users\\Princess\\Desktop\\Collabera Training\\Data\\Data\\vehicles1.csv')

Veh1= pd.read_csv('vehicles1.csv')
Veh2= pd.read_csv('vehicles2.csv')






# EX 2

#check the data using dtypes, describe, sample, head and tail options

##CHECKING VEH1
Veh1.dtypes
Veh1.describe()
Veh1.sample(20)
Veh1.head()
Veh1.tail()

# CHECKING VEH2
Veh2.dtypes
Veh2.describe()
Veh2.sample(15)
Veh2.head()
Veh2.tail()


# Ex 3
# What is the number of observations in each dataset?

Veh1.count(axis =0)
Veh2.count(axis =0)


# Ex 4
#Join veh1 and veh2 into a single DataFrame called cars

cars= pd.concat([Veh1,Veh2],axis = 0)


#Ex 5
# delete the duplicates in item_name and quantity

#cars['quantity'] = np.where(car[' '] == True, '1','false'

#---TESTTING....cars['quantity']= cars['car'].count()

CarDROP= cars.drop_duplicates('car')



# EX 6

#Merge veh1 and veh2 with car prices
car_prices= pd.read_csv('car_prices.csv')

BIGmerge = pd.merge(cars,car_prices)


# Ex 7

#Give the top 10 and the bottom 10 cars with the best price_to_Value_ratio defined as 
#price_to_Value_ratio = price/(horsepwer/mpg)

BIGmerge['horsepower']=BIGmerge.horsepower.str.replace(' ','0')
    
BIGmerge['horsepower']=BIGmerge['horsepower'].astype(float)


BIGmerge['P2VR'] = BIGmerge['Price'] /(BIGmerge['horsepower']/BIGmerge['mpg'])


BIGmerge

descendingBM= BIGmerge.sort_values(by = "P2VR", ascending = False)
#TOP 10
descendingBM.head(10)
#BOTTOM10
descendingBM.tail(10)

#Ex 8
# select only the vehicle from both the datasets  with mpg >= 25
#print the no of such vehicles and their avg prices
BIGmerge['MPG >= 25']= np.where(BIGmerge['mpg'] >= 25) ##### DIDNT WORK FOR ME
print(BIGmerge['MPG >= 25'].count())
print(BIGmerge['MPG >= 25'].mean())

# EX 9
# print the percentile distribution of prices of all cars with horsepower <= 100 with 20,40,50,70,90,95,99 and 99.9 percentile values of prices
Ptile = np.percentile(BIGmerge['horsepower']<=100, [20,40,50,70,90,95,99,99.9], axis =0)

#Ex 10
#calculate the avg price of all the car models
print(BIGmerge['Price'].mean())

from matplotlib import pyplot as plt
# Ex 11

#Plot bar graph of the top 10 cars by price and plot their total no of variants available

plt.bar(BIGmerge['car'].head(10),BIGmerge['Price'].head(10))
plt.xlabel("CAR")
plt.ylabel("PRICE")


# Ex 12
#
#calculate the horse power to weight ratio of all the cars by combining the two datasets and selecting only the unique records.
BIGmerge['HPWT']= (BIGmerge['horsepower']/BIGmerge['mpg'])
BIGmerge['HPWT'].unique()
#Ex 13
#
#PLot the top 20 percentile cars by power to weight ratio  - X axis (car name) Y axis - power to weight ratio in % terms
plt.plot(np.percentile(BIGmerge['HPWT'],[20],np.percentile(BIGmerge['HPWT'],[20])))
plt.xlabel("CAR")
plt.ylabel("P2W Ratio")

#Ex 14

#calcuate the avg age of a car model from 2019 ( using their model ) and plot

## Ex 15
#create  4 horse power bands such that 25% of the total no of cars are in each band in increasing order of horse power and create a pie chart

BIGmerge['HP1']=BIGmerge['Horsepower'].head(94)

BIGmerge['HP4']=BIGmerge['Horsepower'].tail(94)
