# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:30:16 2019

@author: Princess
"""

f=open('C:\\Users\\Princess\\Desktop\\Collabera Training\\Data\\Data\\car_prices.csv','r')

print(f.readlines(100))

import numpy as np
import pandas as pd
import csv
import os

os.getcwd()

os.chdir('C:\\Users\\Princess\\Desktop\\Collabera Training\\Data\\Data')

os.getcwd()

f=open('car_prices.csv','r')
print(f.readlines(100))

#IMPORTING DATA
newdata = pd.read_csv('Sample_csv_File_V1.csv')

newdata.dtypes

#CHECKING THE DATA
newdata.shape[1]

newdata.shape[0] # will give you only the observations/ row numbers

newdata.shape
newdata.info()

newdata.dtypes

t = newdata.dtypes


#gives stats about numerical variables

checkingdata = newdata.describe()

checkingdata= newdata.describe().transpose() # you can also write .T instead of .transpose()


#allows us to iew first / last x observation 
t = newdata.head()
t = newdata.head(12) #you can request more than the standard 5
t = newdata.tail()

# allows to view specific file

t= newdata.sample(n=37)
t = newdata.sample(frac =0.2)


# getting frequency table of a single variable

t = newdata ['TRFRID'].value_counts()#PREFERRED METHOD

t=newdata.TRFRID.value_counts()

print(newdata.columns) # prints the columns names


# READING A CSV FILE OPTIONS

newdata1 = pd.read_csv('Sample_csv_File_V2.csv')
newdata1 = pd.read_csv('Sample_csv_File_V2.csv', dtype=str, delimiter= '|')


newdata1['DateofEvaluation']=(pd.to_datetime(newdata1['DateofEvaluation']))

#changing the data type of a variable after reading a file

newdata1['Revenue'] = newdata1['Revenue'].astype(float)

#var='123.234'
#var= var.astype(float)
#var =var.astype(int)
#print(var)

#groupby
newdata1.agg({'Revenue':'mean'})

print(newdata1['Revenue'].mean())


print(newdata1.Revenue.min())

print(newdata1['Revenue'].median())

f=open('car_prices.xlsx')

practiceread = pd.read_excel('car_prices.xlsx')

secondpracticeread = pd.read_csv('vehicles1.csv')




abcd= np.percentile(newdata1['Revenue'],[10,20,30,40,80,90,95,99,99.5], axis= 0)


agefile = pd.read_csv('Sample_Age.csv', dtype= str, delimiter = ',')

agefile['Age']= agefile['Age'].astype(float)
# =============================================================================
# 
# for x, columns in agefile.head(63):
#     if 'Age'.isnull():
#         '
#     else:
#         continue
# =============================================================================

agefile['Age']= agefile['Age'].fillna(agefile['Age'].mean())

t= newdata1[agefile.Age < 110]

#merging files
agefile = pd.merge(newdata1,Age, how = 'left', on = 'PERSONID')



#creating a flag variable

newdata
























