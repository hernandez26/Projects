# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:34:19 2019

@author: Princess
"""

a = 200
b = 400
if b > a:
    print("b is greater than a")
elif b < a:
    print("a is greater than b")
else:
    print("a and b are equal")
    
myname = "Jonny"

if myname == "Jonny":
    print("correct")
    
else:
    print("error")
    


i = 20
if(i > 15):
    print ("10 is less than 15")


num = -1

if (num % 2)== 0 and num > 0:
    print("NUM is a positive even number")
elif (num % 2) == 0 and num <0:
    print("NUM is a negative even number")
elif num == 0:
    print("NUM is equal to zero")
elif (num % 2)!= 0 and num > 0:
    print("NUM is a positive odd number")
elif (num % 2) != 0 and num < 0:
    print("num is a negative odd number")
    
    
##PART 2
    
num2 =-2
    
if num2 == 0:
    print("NUM is equal to Zero")
elif num2 > 0:
    if (num2 %2)==0:
        print("NUM is a positive even number")
elif num2 > 0:
    if (num2 %2)!= 0:
        print("NUM is a positive odd number")
elif num2 < 0:
    if (num2 %2)==0:
        print("NUM is a negative even number")
elif num2 < 0:
    if (num2 %2)!= 0:
        print("NUM is a negative odd number")
   

        
        
# VERSION 1
 i = 11
 
if (i == 10):  
    #  First if statement
    if (i < 15) :
        print ("i is smaller than 15")
elif (i != 10):
    if (i < 15):
         print ("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print ("i is smaller than 12 too")
    else:
        print ("i is greater than 15")
        

# VERSION 2   
 i = 11
 
if (i == 10) or (i < 15):  
    print ("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print ("i is smaller than 12 too")
    else:
        print ("i is greater than 15")



#short

if a > b: print("a is greater than b")



## LEAP YEAR CALCULATOR

Year = 2100

if (Year % 4) == 0:
    print("It is a leap year")
elif (Year % 100)== 0:
    if (Year % 400) == 0:
        print("It is a leap year")
elif (Year % 100)== 0:
    if (Year % 400) != 0:
        print("It is not a leap year")
elif (Year % 100)!= 0:
    if (Year % 400) != 0:
        print("It is not a leap year")
        
Year = 2400

if (Year % 4) == 0:
    if (Year % 100) == 0:
        if (Year % 400) == 0:
            print("It is a leap year")
elif (Year % 4) == 0:
    if (Year % 100)== 0:
        if (Year % 400) != 0:
            print("It is not a leap year")
else:
    print(" who knows!!?")
    
# ONLINE EXAMPLE
 Year = 2000   
    
if (Year % 4) == 0:
    if(Year % 100) == 0:
        if(Year % 400)==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
            print("It is not a leap year")
else:
            print("It is not a leap year")

   

    


    