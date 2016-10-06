'''
Created on Dec 30, 2015

@author: tcsshvr
'''
#Notes:
#This program uses a file pointer as argument 

def print_all(f):
    #Prints whole data in a file instead of a line
    print(f.read())

#Sets the cursor to start of the file    
def rewind(f):
    print(f.seek(0))

#Prints first line only    
def print_a_line(lineCount, f):
    print(lineCount + " " + f.readline())

file=open("Resources\InputData.txt")

print ("The whole file data:")

print_all(file)

print("Cursor is set to zero")

rewind(file)

print("Print a line from file:")

print_a_line(1, file)
