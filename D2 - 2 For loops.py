# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:50:57 2019

@author: SHAIL
"""

#loops in python


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x[0]=='b':
        print(x)

for x in range(0,n):
    print(x*x)
    




#ex 1

frus = ["Apple","Peach",30]
for a in frus:
    print(a)
  
  
#Ex 2  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   for y in x:
      print(y)
      
      
fruits = [30,'100','983564']
for x in fruits:
  for y in x:
      print(y)
      
  
 #Ex 3

for x in range(7):
  print(x+12) 
  
for i in range(9):
    print(i)
  
  
#ex 4

for x in range(2, 6):
  print(x)
 
#ex 5

for x in range(10):
  print(x)
else:
  print("Done till 10!")

    
#ex 6

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#ex 7    
  
list = [10,20,35,50,55,60]
evenlist = []
oddlist = []


for i in list:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
 
print(evenlist)
print(oddlist)                

#ex 8
n = 21
    
for i in range(0,n):
    print(i+1,end ="~")    
    
# ex 9

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break    
   
#The while loop below defines the condition (x < 10) and repeats the instructions until that condition is true. Type this code:


x = 3                              
while x < 10:
    print(x)
    x = x + 1
    
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Check if a triangle is scalene, isosceles or equilateral
  

x = int(3)
y = int(7)
z = int(4)

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")




    
# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
  
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items)) 


## for num from 10 to 51 create 3 new lists as follows:
#    list1 = if num <=25 do num+1
#    list2 = if 25 < num<= 40 do num*2
#    list 3 = if num > 40 do num*1.2


x=10
y=51

nos_lt_25=[]
nos_25_40 = []
nos_40_plus = []
for num in range(x,y):
    if num<=25:
        nos_lt_25.append(num+1)
    elif num>25 and num<=40:
        nos_25_40.append(num*2)
    elif num>40:
        nos_40_plus.append(num*1.2) 
        

#Check if all the elements of a string are nos
        
text = ("+107")
text = text.strip()
if len(text) < 1:
    print("Input a valid text")
else:
    if all(text[i] in "0123456789" for i in range(len(text))):
        print("The string is an integer.")
    elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         print("The string is an integer.")
    else:
        print("The string is not an integer.")         
        
# Getting the astro sign

day = int(9)
month = ("december")
if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign) 

#check which of the three nos is the middle no 

a = float(2)
b = float(6.4)
c = float(7.3)
if a > b:
    if a < c:
        middle = a
    elif b > c:
        middle = b
    else:
        middle = c
else:
    if a > c:
        middle = a
    elif b < c:
        middle = b
    else:
        middle = c

print("The middle is", middle)
       