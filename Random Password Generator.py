# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:27:06 2019

@author: Princess
"""

import random
import string

numlist= ['0','1','2','3','4','5','6','7','8','9']
characterList= [ '@', '^','&','*','!','$','?']
signature= 'JH'
password=[]
PassReady=[]



def randPass(LetLen=4, Numlen=4, Charlen= 2):
    #function to Generate a Password
    
   #Random letter List
    characters = string.ascii_lowercase
    ranLet = ''.join(random.choice(characters) for i in range(LetLen))
    
    #Random Number list
    ranNum= ''.join(random.choice(numlist)for x in range(Numlen))
   
    #random character list
    ranchar=''.join(random.choice(characterList)for Y in range(Charlen))
    
    #Join the random lists together to form password
    password.append(ranLet)
    password.append(ranNum)
    password.append(ranchar)
    password.append(signature)
    
    PassReady.append(password)
        
    return PassReady


print ("The generated Password is", randPass() )
