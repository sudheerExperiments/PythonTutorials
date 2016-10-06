'''
Created on Dec 22, 2015

@author: tcsshvr
'''
#import statements
from sys import argv
from os.path import exists

#Read arguments
filename,from_file,to_file=argv
print ("Copying from %s to %s" (from_file,to_file))

#Opens specified file   
indata=open("/Resources/" + from_file +".txt").read()

#Prints size of the string
print ("The input file is %d bytes long" % len(indata))

#If the specified file exits it returns true or else returns false
print ("Does the output file exists %s" % exists(to_file)) 
print ("Ready, hit RETURN to continue, CNTRL-C to abort.")  
temp=input("Enter the text:")

#Opens output file to write data to the file
out_file=open("/Resources/" + to_file +".txt","w")
out_file.write(indata)
print ("Alright, all done.")

out_file.close()
