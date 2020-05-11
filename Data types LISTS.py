# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:12:22 2019

@author: Princess
"""

#I am doing this for checking how comments work

#abcd =[]

# list of integers as well as string
abcd=[1,2,3, "shail"]

print(abcd)

#positioning
list1= abcd[2] # this is still an integer because it only has one element

list2= abcd[0:3]


#nested list
nestedlist= ["shail", [11,8.4.6],['toronto'], abcd, "abcd"]
print(nestedlist)

#math operations on list
list1 = [10,20,30,40,50,100]

print(list1[2])
print(list1[-2])

list2=[100,'richond' 300, 400, 500, 1000]

list3= list1+list2

print(list3)


#appending another element
list1.append(200)
print(listl)

#append and del

list1.append(199)

del list1[2]


#iterating over a list

list1=[10,65,20, 30]
for x in list1:
    print(x)
    
