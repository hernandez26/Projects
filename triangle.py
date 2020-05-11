# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:25:30 2019

    @author: Princess


"""
from collections import Counter
# WHILE LOOP

x = 3
while x < 10:
    print(x)
    x = x + 1


x = int(3)
y = int(7)
z = int(4)

if x == y == z:
    print("Equalateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")

isos=[]
equal=[]   
trianglecount=[]
scale=[]
finalset= {}
for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            if (a!=b!=c and a+b > c) or (a!=b!=c and b+c > a) or (a!=b!=c and c+a > b): #Scalene check
                scale.append(1)
            elif a==b!=c  or b==c!=a or c==a!=b: #Isosceles check
                 isos.append(1)
            elif  a == b == c: #Equalateral check
                 equal.append(1)
            else:
                 print("That is all of the posible triangles")
                 
trianglecount = scale+isos+equal               
print(len(trianglecount))

(tuple(trianglecount))

print(len(finalset))

             

    