# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:09:48 2020

@author: kismet
"""

#%%

def name():
    
   fname = input("Enter your first name: ")
   lname = input("Enter your last name: ")
   city = input("Enter the city you live in: ")
   state = input("Enter the state you live in: ")
   
   fullname = fname + " " + lname
   location = city +", " + state
   
   print("Your name is:", fullname)
   print("You live in:", location)


#%%