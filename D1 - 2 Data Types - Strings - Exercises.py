# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 01:06:05 2019

@author: SHAIL
"""


#exercises =================================================================

s = "Hey there! what should this string be?"
# find length of the above string
print(len(s))

# First occurrence of "s"
print(s.index('s'))

# Number of a's should be ?
print(s.count('a'))

# Slicing the string into bits

#1 - The first five characters are 
print(s[0:5])
#2 - The next five characters are 
print(s[6:11])
#3 - The thirteenth character is 
print(s[12])

#4 - length of total string
print(len(s))

#5 -  Convert everything to uppercase
print(s.upper())


# Convert everything to lowercase
print(s.lower())


# Split the string into separate strings,
# each containing only a word
print(s.split(" "))


s ="  tobacco  free  workplace  "

"tobacco free workplace"

b = 10.789
type(b)

b=str(b)
