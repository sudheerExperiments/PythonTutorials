'''
Created on Jan 6, 2016

@author: tcsshvr
'''

the_count = [1,2,3,4,5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3]

for number in the_count:
    print("The number in the list is: %d" % number)
    
for fruit in fruits:
    print("The fruit is: %s" % fruit)

#Prints raw data    
for i in change:
    print("I got %r" % i)
    
elements = []

#range(0,6) returns numbers in a particular range.
for i in range(0,6):
    print("Adding %d to the list." % i)
    #elements can be added to a list using append()
    elements.append(i)
    
for i in elements:
    print("After adding elements: %d" % i)

#While loop example
i=0
numbers=[]
while(i<6):
    numbers.append(i)
    i+=1

print("The numbers in the list is:")

for i in numbers:
    print(i)  
   
        