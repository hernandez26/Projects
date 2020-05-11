# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:54:21 2019

@author: SHAIL
"""

#For loop exercises :

#1 - Calculate age-----------------------------------------------------

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
current_year= 2019
for x in years_of_birth:
    Age= (current_year-int(x))
    print((Age),end=' ')



#2------------------------------------------------------------------

#Write a  program to find those numbers which are divisible by 7 and multiple of 6, between 1600 and 2900 (both included)
for x in range(1600,2900):
    if x % 7 == 0 and x % 6 == 0:
        print((x),end=' ')
    else:
        continue
#3----------------------------------------------------------

#Write a Python program that takes a word from the user and reverse it.
    def reverse():
        word= input("Type a word that will be reversed ")
        for x in word:
            word= word[::-1]
        return word
        
    reverse()

#4-----------------------------------------------------------------

#Write a Python program to count the number of even and odd numbers from the following
evenlist= []
oddlist= []
numbers = [7,9,2,4,5,19,34,99,102,3,75]
for x in numbers:
    if x % 2 == 0:
        evenlist.append(x)
    elif x % 2 != 0:
        oddlist.append(x)
print(len(evenlist))
print(len(oddlist))
        

#5--------------------------------------------------------------

#Write a Python program to get the Fibonacci series between 0 to 50.
#
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, .... 

#Every next number is found by adding up the two numbers before it.
def fibo():
    for x in range(0,50):
        f = fibo(x-1)+fibo(x-2)
    return f

fibo()
    


#6 -----------------------------------------------------------------

#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Three" instead of the number and for the multiples of five print "Five". For numbers which are multiples of both three and five print "ThreeFive".

for x in range(1,50):
    if x % 3 ==0:
        print(("Three"),end=', ')
    elif x% 5 == 0:
        print(("five"),end=', ')
    elif x %3 == 0 and x% 5 ==0:
        print(("Threefive"),end=', ')
    else:
        print((x),end=', ')
        