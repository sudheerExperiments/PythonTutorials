'''
Created on Dec 15, 2015

@author: tcsshvr
'''

days=100

#Prints variable of any data type, "," is not printed in output though
#Note:A space is automatically inserted after printing the string
print ("No. of days",days)

#Prints only string variable,Conversion to string is necessary
#str(variable) converts any variable to string explicitly
print ("No. of days" + str(days))

#Use %s to print a string and use '% variable name to' to print the variable value in 
#between a string
print ("Hey %s there." %"you")

#Use this statement when printing multiple variable in single print statement.
print ("He's got %s eyes and %s nose" %("good", "bad"))

#To print raw use %r"
hilarious=False
joke_evaluation="Isn't that joke so funny! %r"
result=joke_evaluation % hilarious

print (result)

#Prints . 20 times
print ("." * 20)

end1="a"
end2=1
end3=3+2j
end4='c'
end5=3.4567
end6=-10

#When %s is used only the string(a) is printed
#When %r is used with quotes("a") everything is printed.Same with other data types
#Any data type can be printed using %r
print ("end values" + " %s %r %r %r %r %r %r" %(end1,end1,end2,end3,end4,end5,end6))

#When you use triple quotes it tells interpreter that remaining statements are in next line.
print ("""
There's something going on here.
Come here please mom.
They are beating me.
""")
