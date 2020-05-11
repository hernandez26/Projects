# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:22:10 2019

@author: SHAIL
"""
abcd = ['nintendo','Spain', 1, 2, 3]

print(abcd)

# Ex1 - Select the third element of the list and print it

print(abcd[2])



# Ex2 - Type a nested list with the follwing list elements inside list abcd mentioned above and print it

newlist = [54,76]

MyNesList = [abcd,newlist]

print(MyNesList)


# Ex3 - Print the 1 and the 4 position element in the following list

nestedlist = ["shail", [11,8, 4, 6], ['toronto'],abcd, "abcd"]

print(nestedlist[0],nestedlist[3])


# Ex4  - add the following 2 lists and create list3 and print 

list1= [10, 20, 'company', 40, 50, 100]

list2 = [100, 200, 300, 'orange', 400, 500,1000]

list3 = list1 + list2

print(list3)

# Ex 4.1 - unique elements in a list

l=[10,10,20,30,30,40,50]

i = set(l)

j =list(i)


# Ex 5 - print the lenght of the list3
print(len(list3))



# Ex 6 Add 320 to list 1 and print

print(list1.append(320))

#Ex 7 - Add parts of list1 & 2 by tking first 4 elements from list1 and last 2 elements from list2
print(list1[0:4] + list2[-2:0])


#ex 8 check if 99 is in list 1 
print(99 in list1)


#ex 9 check if 99 is not in list 1 

print(99 not in list1 )


# concatenation (+) and replication (*) operators
#ex 10 - CONCATENANTE  list 1 and ['cool', 1990]

print(list1 +['COOL',1990])


# Ex 11 -  triplicate the list 1
print(list1*3)

# ex 12 - find min & max of list2
del list2['orange']

print(min(list2))

print(max(list2))

# append & del
# Ex 13 append 'training' to list 1
print(list1.append("training"))

# Ex 14 delete 2nd position element from list 2
del list2[1]

# Ex 15 - iterate over list1 and print all elements by adding 10 to each element

list1= [10, 65,20, 30,93,  40, 50, 100]

# for x in list1:
for x in list1:
    print(x+10)
    


#Ex 16 sorting

#sort list1 by ascending order
print(list1.sort(reverse=false))

#sort list1 by reverse order
    
print(list1.sort(reverse=true))
