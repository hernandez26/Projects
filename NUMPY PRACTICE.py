# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:36:52 2019

@author: Princess
"""

import numpy as np

#regular list

list1= [10,20,30,40,50,100]

list2=[100,200,300,400,500,1000]

list2+10

list3= list1+list2 # this creates a new list

#NUMPY ARRAYS

a = np.array([1,9,8,3])
c = np.array(list2)

#MATHEMTICAL OPERATIONS

d = a +10
a* 10

# compare Array and list operations

list1*3

list1+10 # this gives error

#adding another element in list vs arrays

list1.append(200)
print(list1)

a.append(200) # ARRAYS CANNOT USE APPEND LIKE THIS. PRODUCES ERROR

#removing 

#array operations

## THIS SHOWS THAT ARRA
import numpy as np

evenlist= []
oddlist= []
numbers = [7,9,2,4,5,19,34,99,102,3,75]

NewNUM=np.array(numbers)

for x in NewNUM:
    if x % 2 == 0:
        evenlist.append(x)
    elif x % 2 != 0:
        oddlist.append(x)
        
newEVEN=np.array(evenlist)
newODD=np.array(oddlist)

print(newEVEN)
print(newODD)
##THIS CONVERTS ARRAY TO LIST
newEVEN_list = newEVEN.tolist()



#===================================================================================

import numpy as np

evenlist= []
oddlist= []
numbers = [7,9,2,4,5,19,34,99,102,3,75]

NewNUM=np.array(numbers)

for x in NewNUM:
    if x % 2 == 0:
        evenlist.append(x)
    elif x % 2 != 0:
        oddlist.append(x)
        
newEVEN=np.array(evenlist)
newODD=np.array(oddlist)

print(newEVEN)
print(newODD)
#===================================================================================

fruits= [30,'100','983564']
for x in fruits:
    for y in x:
        print(x)
        
        
        
        
        