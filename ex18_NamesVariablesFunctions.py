'''
Created on Dec 24, 2015

@author: tcsshvr
'''
#Arguments are packed and a pointer is passed as a arguments.
def print_two(*args):
    #Arguments are unpacked.
    #No. of variables used should be same as no. of variables passed.
    #Otherwise error will be displayed
    arg1,arg2=args
    print ("arg1: %s, arg2: %s" %(arg1,arg2))

def print_two_again(arg1,arg2):
    #The arguments are printed
    print ("arg: %s, arg2: %s" %(arg1,arg2))
    
def print_one(arg1):
    #Single argument is passed and printed
    print("arg1: %s" %arg1)
    
def print_none():
    #No argument is passed
    print ("I got nothing to print")
    


print_two("abc","defmgr")
print_two_again("sudheer"," is not human")
print_one("I am not kidding")
print_none()
