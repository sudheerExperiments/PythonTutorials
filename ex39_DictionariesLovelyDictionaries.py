'''
Created on Jan 13, 2016

@author: tcsshvr
'''

#States dictionary
states = {"Oregon" : "OR", 
          "Florida":"FL",
          "California":"CA",
          "Newyork":"NY",
          "Michigan":"MI"
          }

#Cities dictionary
cities={"CA":"San Fransico",
        "MI":"Detroit",
        "FL":"Jacksonvile"
        }

#Added two nre cities into the cities dictionary
cities["NY"]="Newyork"
cities["OR"]="Portland"

#Print value using the key
print("*" * 10)
print("NY state has:", cities["NY"])
print("OR state has: %s" %cities["OR"] )

#Print value using the key
print("*" * 10)
print("Michigan's abbrevation:", states["Michigan"])
print("Florida's abbrevation:", states["Florida"])

#Print value using the key of value
print("*" * 10)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Newyork"]])

#Print all items in the cities dictionary
print("*" * 10)
for abbrev, city in cities.items():
    print("%s,%s" %(abbrev,city))

#Print states and cities
print("*" * 10)    
for abbrev,state in states.items():
    if(cities[state]=="none"):
        print("%s,%s,%s" %(abbrev,state,cities[state]))
    else:
        print("No city found with the name")
    
print("*" * 10)
state = states.get("Texas")

#If the state is present it returns the value else "none" is returned.
if not state:
    print(state)
    print("Sorry, no state with the name Texas")

#Adds new key and value to the cities dictionary    
city = cities.get("TX", "Does not exist")
print("The city for the state \"TX\" is:%s" % city)