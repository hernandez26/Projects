# -*- coding: utf-8 -*-

import numpy as np

import pandas as pd

import csv

# Ex 1 Set your home directory
f=open('C:\\Users\\Princess\\Desktop\\Collabera Training\\Data\\Data\\Practice_data.csv','r')



# EX 2
#Read the practice dataset named as Practice_data.csv data from computer and name this dataframe as pr
pr= pd.read_csv('Practice_data.csv')

# EX 3

#check the data using dtypes, describe, sample, head and tail options
pr.dtypes
pr.describe
pr.sample(35)
pr.head()
pr.tail()

# Ex 4
# reassign the column with the cleaned prices

#pr.item_price = prices 

pr.rename(columns={'item_price': 'prices'}, inplace=True)


# Ex 5

# delete the duplicates in item_name and quantity
pr_filtered = pr.drop_duplicates(['item_name','quantity'])




# EX 6
# select only the products with quantity equals to 1
pr_one_prod = pr_filtered[pr_filtered.quantity == 1]



# EX 7

#Get the uunique no of item_name
pr.item_name.unique()

# Ex 8

#What is the price of each item?
#print a data frame with only two columns item_name and item_price


Each_Price= pr[['item_name', 'prices']]



# Ex 9 
# Select itemname  as chicken bowl and quantity >1

pr[(pr['item_name'] == 'Chicken Bowl') & (pr['quantity'] > 1)]

# ex 10
# select only the products with quantity equals to 1
pr_one_prod = pr_filtered[pr_filtered.quantity == 1]

#OR

prod2= pr_filtered.quantity == 1

# Ex 11

# sort the values from the most to less expensive
descendPR= pr.sort_values(by = "prices", ascending = False).head(20)

#chipo.item_name.sort_values()

# OR

#chipo.sort_values(by = "item_name")


# Ex 12

#How many times were a Veggie Salad Bowl ordered?
pr_salad = pr[pr.item_name == "Veggie Salad Bowl"]

len(pr_salad)

# Ex 13
#How many times people orderd more than one Canned Soda
pr_drink_steak_bowl = pr[(pr.item_name == "Canned Soda") & (pr.quantity > 1)]
len(pr_drink_steak_bowl)

