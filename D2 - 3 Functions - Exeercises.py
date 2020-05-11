# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:32:33 2019

@author: SHAIL
"""
# 1 

#Create a function to calculate the absolute value of a number without using the abs() function to calculate the absolute value for -9 and 7.2
vals=[7.2,-9]
def abso():
    for x in vals:
        if x > 0:
            X=(x*1)
        elif x < 0:
            Y=(x*(-1))
    return X,Y

abso()
 
    

# 2

# for the given data (20,30,40,50,100), create a function to calcuate the total/3 
#note that all the calcualtions have to be done within the function
data=[20,30,40,50,100]

def totalDiv3():
    TD3= sum(data)/3
    return TD3
totalDiv3()
        


## 3
#create a function to work in range(43,60) such that if the number is <50, it prints out "LT_50" else it should print out (number+3)
Newlist= []
def LTFifty():
    for x in range(43,60):
        if x < 50:
            x = "LT_50"
            Newlist.append(x)
            
        else:
            y = x+3
            Newlist.append(y)
    return(Newlist)

LTFifty()
            
    

#4

# create a function which takes 2 inputs as num and x and do the following
#if num>=0 then calcuate num*x else num*x/2
def calc(num, x):
    if num>= 0:
        print(num*x)
    else:
        print(num*(x/2))
    return

calc(-4,-4)

#5 create a function to create a new list with only the nos which can be divided by 3 from the following list
Threelist=[]
li = [5, 7, 21, 99, 51, 62, 77, 27, 73, 61] 
def div3list():
    for x in li:
        if x %3== 0:
            Threelist.append(x)
        else:
            continue
    print(Threelist)
    return

div3list()


# 6

#create a function using lambda function to overwrite the following list with all the elements squared

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
newlist= list(map(lambda x: x*x,li))
print(newlist)
    