# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:41:14 2019

@author: JH
"""

f=open('C:\\Users\\Princess\\Desktop\\Collabera Training\\Data\\Data\\car_prices.csv','r')
print(f.readlines(100))
import numpy as np
import pandas as pd
import csv
import os
os.getcwd()
os.chdir('C:\\Users\\Princess\\Desktop\\Collabera Training\\Data\\Data\\')
os.getcwd()
# WORKING WITH EXTERNAL FILES =======================================================================
#importing data from computer and other locations
newdata = pd.read_csv('Sample_csv_File_V1.csv')
newdata.dtypes
#checking the data
#What is the number of observations in the dataset?
newdata.shape[1]
100/newdata.shape[0] #will give you only the observations/rows number
newdata.shape
newdata.info()
newdata.dtypes
t = newdata.dtypes
#gives stats about numerical variables
checkingdata = newdata.describe()
checkingdata = newdata.describe().transpose()
#allows us to view first / last X observations
t=newdata.head(12)
t=newdata.tail()
#allows us to view a sample of observations
t=newdata.sample(n=370)
t=newdata.sample(frac = 0.2)
#getting frequency table of a single variable
t=newdata['TRFRID'].value_counts()
car = pd.read_csv('car_prices.csv')
t=car.car.value_counts(dropna=False)
t=newdata.TRFRID.value_counts(dropna=False)
t=newdata.TRFRID.value_counts(dropna=False)
print(newdata.columns) # prints the column names
# reading a csv file with options
newdata1 = pd.read_csv('Sample_csv_File_V2.csv')
newdata1 = pd.read_csv('Sample_csv_File_V2.csv',dtype=str, delimiter='|')
newdata1.dtypes
newdata1.info()
newdata1['DateofEvaluation']=(pd.to_datetime(newdata1['DateofEvaluation']))
#Changing the data type of a variable after reading a file
#var= '123.234'
newdata1['Revenue'] = newdata1['Revenue'].astype(float)
newdata1.Revenue = newdata1.Revenue.astype(float)
newdata1.Revenue = newdata1.float(['Revenue'])
newdata1.dtypes
t = newdata1.dtypes
newdata1.PROGRAMEID.unique() # calulating the unique rows
t = newdata1.describe()
#getting frequency table of a single variable
newdata['PROGRAMEID'].value_counts()
newdata.PROGRAMEID.value_counts()
t=newdata1.Revenue.value_counts()
#Group by
newdata1.agg({'Revenue':'mean'})
print(newdata1['Revenue'].mean())
print(newdata1.Revenue.min())
print(newdata1['Revenue'].median())
print(newdata1['PROGRAMEID'].mode())
print(newdata1['Revenue'].std())
print(newdata1['PROGRAMEID'].count())
abcd = np.percentile(newdata1['Revenue'], [10,20,30,40,80,90,95,99,99.5], axis =0)
#Part 2 =========================   DATA HANDLING ================================================
age = pd.read_csv('Sample_Age.csv',dtype=str, delimiter=',')
#Changing the data type of a variable after reading a file
age.Age = age.Age.astype(float)
#Merging files
newdata2 = pd.merge(newdata1,age[['PERSONID','Age']], how='left', on='PERSONID')
# An example where the names are not the same in both the files
# newdata2 = pd.merge(newdata1,age, how='left', left_on = 'PersonID' ,right_on = 'Person_id')
#Data Exploration
#Imputing Data
newdata2['Age'] = newdata2['Age'].fillna(newdata2['Age'].mean())
t = newdata2.describe()
#Selecting a few columns from a dataframe
t=newdata2[['PERSONID', 'Revenue', 'Age']]
#Creating a new variable
newdata2['rev2'] = newdata2['Revenue']*2
newdata2.rev2 = newdata2.Revenue*2
newdata2['rev3'] = newdata2['Revenue'] + newdata2['rev2']
newdata2.shape
#filtering data
t= newdata2[newdata2.Revenue < 110]
t= newdata2.Revenue < 110

newdata2['Revenue'] = newdata2['Revenue'].astype(float)

newdata2.Revenue.dtype

## PRACTICE====================================================================================
# Creating a flag variable
newdata2['Rev_flag'] = np.where(newdata2['Revenue'] > 120,'GT_120',np.where(newdata2['Revenue'] > 115, 'GT_115',np.where(newdata2['Revenue'] > 110, 'GT_110',np.where(newdata2['Revenue'] > 105, 'GT_105','<=105'))))

newdata2['Rev_flag'].unique()


flagFreq= newdata2['Rev_flag'].value_counts()


#LAMBDA===========================

newdata2['Age']= newdata2['Age'].astype(float)
newdata2.Age.dtype
newdata2['agegrp'] = newdata2['Age'].apply(lambda x : 'GRP_LE_35' if x <= 35 else 'GRP_LE_50' if x > 35 and x <= 50 else 'GRP_GT_50_70' if x > 50 and x <= 70 else 'GRP_GT_70' if x > 70 else 'MISS')


#t = newdata2.iloc(:[5,7])
list1=[1,2,3]

newdata2.tail(1000).to_csv("Jonny.csv")

pd.DataFrame(list1).to_csv("JPractice.csv")












## applying functions on dataframes

#1
def USD(x):
    return float(x/1.34)
newdata2['revenue_USD']= newdata2['Revenue'].apply(USD)







def rev_age(row):
    return row['Revenue']/row['Age']

newdata2['rev_age']=newdata2.apply(rev_age,axis =1)


def Multi_rev_age(row):
    return row['Revenue']*row['Age']

newdata2['rev_age']=newdata2.apply(Multi_rev_age,axis = 1)


## Easier method to multiply
newdata2['testing']=newdata2.Revenue* newdata2.Age



#renaming a column

newdata2.rename(columns={'CUSTID_yuiys': 'CUSTID'}, inplace= True)


#sorting a dataset

newdata2= newdata.sort_values(['Age', 'Revenue'],ascending= True)


#Missing value treatment
newdata2['Age'].fillna(47, inplace = True)



#groupby

Rev_summed = newdata2.groupby(['TRFRNAME']).Revenue.mean()

Age_mean = newdata2.groupby(['TRFRNAME','PROGRAMEID']).Age.mean().reset_index()


# PRACTICE
f=open('Practice_data.csv')
Practice_data= pd.read_csv('Practice_data.csv')

Practice_data.item_price.apply(lambda x: x.replace('$',''))

Practice_data['item_price'] = Practice_data['item_price'].astype(float)

Practice_data.item_price.dtype




Practice_data['item_price1']=Practice_data.item_price.str.replace("$",' ')

Practice_data['item_price1']=Practice_data['item_price1'].astype(float)

print(Practice_data.dtypes)

Practice_data.item_price1.dtype


Practice_data['ChickenData']= Practice_data.apply(lambda x: x.astype(str).str.contains('Chicken').any(),axis=1)
















