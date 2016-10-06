'''
Created on Jan 13, 2016

@author: tcsshvr
'''
import sys

ten_things="Apples Oranges Crows Pigs Telephone Light Sugar"

stuff=ten_things.split(" ")

more_stuff=["carrot", "banana", "Mango"]

while(len(stuff)!=10):
    temp = more_stuff.pop()
    stuff.append(temp)

#Prints the second item in the list    
print (stuff[1]) 
#Prints the top item in the list    
print (stuff[-1])
#The list is a stack so it pops the top element in the list
print (stuff.pop())
print ("\n")
#Places space in between every item in the list
print (' '.join(stuff))
#Places # in between 3 and 5 item in the list
print ('#'.join(stuff[3:5]))

