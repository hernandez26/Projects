# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:28:00 2019

@author: Jonathan
"""

num = 400
evens=[]


for x in range(1,num):
    if x % 2 != 0:
        continue  
    for y in str(x):
        if (int(y) % 2) != 0:
            break
    else:
        evens.append(x)
        
        
print(len(evens))



items = []
for i in range(1,401):
    s= str(i)
    if (int(s[0])%2 ==0) and (int(s[1])%2 ==0) and (int(s[2])%2 ==0):
        items.append(s)
        break
        
print(len(items))


# =============================================================================
# text= ("+107")
# text = text.strip()
# if len(text) < 1:
#     print("input a valid text")
# =============================================================================
    
    
phoneNum = "+16e09304424"
phoneNum = phoneNum.strip()
if len(phoneNum)== 10:
    if phoneNum.isdigit() == True:
            print("This is a valid number")
            print(phoneNum)
    else: print("the number is not valid")
elif len(phoneNum) == 12:
    if phoneNum[0] =="+":
        NewNum= phoneNum[1:12]
        if NewNum.isdigit() == True:
            print("This is a valid number")
            print(NewNum)
        else:
            print("This number is not vaild")
    else:
            print("This number is not vaild")
else:
            print("This number is not vaild")



##Recursive function
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial (num-1)
        
x = 5        
print("The Factorial of", x, "is",factorial(x))


x = lambda *args: sum(args)
print(x(1,2,3))


def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(3)
print(mydoubler(11))



    
                  
    
            
         
        
                


