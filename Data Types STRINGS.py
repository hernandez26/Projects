# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:06:55 2019

@author: Princess
"""

a = 5

print(a, "is of type", type(a))


s=1
z= (a,"is of type", type(a))

a = 2.0

print(a,"is of type",type(a))


a = 1+2j
print(a, "is complex number?" isinstance(a,complex))



#escape sequences
print('a\
      b\
      c')


#double backspace
print('python\\data-Science')


#tab
print('python\t data-Science')


#newline
print('python\n data-Science')

#raw
print('python\"" data-Science')


statement = "my training is good"
print(statement[0]) #prints first character of the string

print(statement[2:11]) #prints characters starting from 3rd to 5th


print(statement + " and interesting")


#length of the string
print(len(statement))

#position of a char in a string
print(statement.index("i"))

#countof of a char in a string
print(statement.count("0"))



#subsetting of string
st = (statement[3:11])


#reversing a string
print(statement[::-1])

#uppercase string
print(statement.upper())

#lower case string
print('STATEMENT'.lower())


#splitting a string
splitwords= statement.split("")


splitwords = "smoking is bad".split(" ")








