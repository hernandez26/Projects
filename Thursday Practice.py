# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:04:00 2019

@author: jonathan
"""

import numpy as np
import pandas as pd
import csv


##### PYNATIVE EXERCISES=======================================================


# EXERCISE 1

f=open('automobile_data.csv')
AutoDF= pd.read_csv('automobile_data.csv')
Firstf= AutoDF.head()
Lastf= AutoDF.tail()


#EXERCISE 2

AutoDF['price']=AutoDF.price.str.replace('nan', 'idk')
