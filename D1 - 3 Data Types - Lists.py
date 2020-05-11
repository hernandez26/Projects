# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:22:10 2019

@author: SHAIL
"""

#I am doing this for checking how comments work

abcd = []

# list of integers as well as a string
abcd = [1, 2, 3,"shail"]

print(abcd)

#positioning
list1 = abcd[2]


# list with mixed datatypes
mixedlist = [9, "Shail", 67.4,0]

# nested list
nestedlist = ["shail", [11,8, 4, 6], ['toronto'],abcd, "abcd"]
print(nestedlist)

#mathg operations on lists

list1= [10, 20, 30, 40, 50, 100]

print(list1[2])
print(list1[-2])



list2 = [100, 'richmond', 300, 400, 500,1000]

list3 = list1+list2

print(list1*3)


print(list3)

#selecting and printing a specific element from an array

print(list1[2])


# Negative indexing
print(list1[-1])

#length of array

len(list1)


#Adding another element

newl = [100,120]
newl.append(200)
print(newl)

#Adding part of list
list1[:4] + list2[4:]


#in and not in

99 in list3

110 not in list3 

# concatenation (+) and replication (*) operators

list1 + ['shail', 990]


list1 * 2


min(list1)

max(list1)

# append & del

list1.append(199)

del list1[2]

#iterating over a list


list1= [10, 65,20, 30,93,  40, 50, 100]

for x in list1:
    print(x)

#sorting

list2= list1.sort()
print(list1)

print(list1)

    
list1.sort(reverse = True)

print(list1)


list2 = ["oranges", "apples", "Bananas", "Papayas",'32','76','21']

list2.sort()
print(list2)


list2.sort(key=str.lower)
print(list2)





