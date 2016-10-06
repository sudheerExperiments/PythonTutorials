#Initialize value to a variable
str1="hello world"

#prints the whole string
print (str1)
#prints first char of the string
print (str1[0])
#prints 2 to 5 characters
print (str1[2:5])
#prints 2 to all characters
print (str1[2:])
#prints string twice
print (str1*2)
#concats "test" to string
print (str1 + " test")

#frees str1 string space
del str1

#Initialize and assign values to list. List should be initialized with []
list1=["abcd",2.34,54678,3+2j]

print (list1)
print (list1[0])
print (list1[1:3])
print (list1[2:])
print (list1 * 3)
#As list1 is a list this will work
print (list1 + ["mundane"])

del list1

#Initialize and assign values to Tuple. Tuple should be initialized with ()
tuple1=("abcd",4576,2.34,"sudheer")

print (tuple1)
print (tuple1[0])
print (tuple1[1:3])
print (tuple1[2:])
print (tuple1 * 3)

#The below line will not work because size of tuple cannot be changed 
#print (tuple1 + ["mundane"])

#The below line will not work because the value assigned should not be changed
#tuple1[2]=7865

del tuple1

#Creates a dictionary or hash map
dict1={}

#The position should not be a number as in java or c. It can be a string.
dict1["one"]="Omg!!! I am number one"
dict1[2]="Omg!!! I am number two"

#Create and initialize a dictionary with keys and values
tinydict={"name":"sudheer","registration number":"115014079","year":2015}

print (dict1["one"])
print (dict1[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())

del dict1
del tinydict
