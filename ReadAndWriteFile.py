'''
Created on Dec 10, 2015

@author: tcsshvr
'''

import sys
#The below program is to write data into the file
#Try and except are like try and catch in java
try:
    #Opens the specified file
    file=open("Resources/InputData.txt","w")    
except IOError:
    #Prints data to console
    print ("There was an error writing to", "InputData.txt")
    #Exits from the program
    sys.exit()
print ("Enter \" 'file_finish' \" When finished")
file_text="null"
#Here file_text is used to compare so the variable should be given some value before
while file_text != "file_finish":
    #Takes input from the console "Use input(new method) in place of raw_input(old method)"
    file_text = input("Enter text: ")
    if file_text == "file_finish":
    # close the file
        file.close()
        break
    #Writes data into file
    file.write(file_text)
    file.write("\n")
    #Closes the file
file.close()
#The below program is to read data from file
file_name = input("Enter filename:")
if len(file_name) == 0:
    print ("Next time please enter something")
    sys.exit()
try:
    #Opens file to read data
    file = open("Resources/" + file_name, "r")
except IOError:
    print ("There was an error reading file")
    sys.exit()
#Reads data from file    
file_text = file.read()
file.close()
#Writes the file data to console or terminal or output stream
print (file_text)
