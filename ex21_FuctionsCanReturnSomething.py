'''
Created on Dec 30, 2015

@author: tcsshvr
'''

def add(a,b):
    print("Adding %d + %d" %(a,b))
    #Returns value
    return(a+b)

def sub(a,b):
    print("Subtracting %d + %d" %(a,b))
    return(abs(a-b))

def mul(a,b):
    print("Multiply %d + %d" %(a,b))
    return(a*b)

def div(a,b):
    print("Division %d + %d" %(a,b))
    return(a/b)

print("Let's start the operation:")
k=add(20,30)
l=sub(20,30)
m=mul(20,30)
n=div(20,30)

print("The returned values are: %d,%d,%d,%d" %(k,l,m,n))