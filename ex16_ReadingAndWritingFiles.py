'''
Created on Dec 24, 2015

@author: tcsshvr
'''
filename="ex11_Input Data"
print ("We are going to erase %s file" %filename)
print ("Press \' cntrl + c \' to quit")

open1=open("Resources/InputData.txt","w")

print("Truncating data")
open1.truncate()

print("Now I'm going to ask you for three lines.")

line1=input("Enter line1:")
line2=input("Enter line2:")
line3=input("Enter line3:")

open1.write(line1)
open1.write("\n")
open1.write(line2)
open1.write("\n")
open1.write(line3)
open1.write("\n")

print ("File copying is finished")

open1.close()

