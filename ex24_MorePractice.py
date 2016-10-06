'''
Created on Jan 4, 2016

@author: tcsshvr
'''
#Cummulative exercise

print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs")

#Use triple quotes if the string is more than a line.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print("--------------------")
print(poem)
print("--------------------")

five=10-2+3-6

#Implicit conversion from int to string
print("This should be five %s" % five)

def secret_formula(started):
    #Scope of these variables is only in this method
    jelly_beans = started * 50
    jars = jelly_beans /1000
    crates = jars /100
    #Can return more than a variable
    return(jelly_beans, jars, crates)

start_point=1000
#Scope of beans variable is through out the program.
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d",start_point)

print("We would have %d beans, %d jars and %d crates" %(beans,jars,crates))

start_point=start_point /10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))