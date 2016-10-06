'''
Created on Jan 6, 2016

@author: tcsshvr
'''

people = 20
cats = 30
dogs = 15

if(people<cats):
    print("Too many cats than people")
    
if(people>cats):
    print("Too many people than cats")
    
if(people<dogs):
    print("Too many dogs than people")
    
if(people>dogs):
    print("Too many people than dogs")
    
dogs += 10
    
if(people >= dogs):
    print("People may be more than dogs")
    
if(people <= dogs):
    print("Dogs may be more than people")
    
if(people == dogs):
    print("People and dogs are equal")
    
#Now use else if
#In Python else if is written as elif
people = 30
cars = 40
trucks =15

if(cars>people):
    print("We should take the cars")
elif(cars<people):
    print("We should not take cars")
else:
    print("We can't decide")
    
    
