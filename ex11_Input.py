'''
Created on Dec 21, 2015

@author: tcsshvr
'''
#Importing libraries
#Can import only specified functions from library instead of the whole library
from sys import argv

#raw_input function

#raw_input is redefined as input from python 3.x
#To use the same raw_input functionality use eval(input())
abc="su"
y=eval(input("Enter your name:"))
#When user types abc in the input, the eval(input()) function prints the value stored in the variable instead of the string.
# i.e It assumes that the user entered variable name rather than a string.
print (("Your name is: %r" %(y)))

#Normal input function

abc="su"
y=input("Enter your name:")
print (("Your name is: %r" %y))

#Passing arguments when running a program
pname,first,second,third=argv

#Prints variables to the console
print (pname)
print (first)
print (second)
print (third)