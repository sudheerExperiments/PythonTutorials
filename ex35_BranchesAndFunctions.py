'''
Created on Jan 7, 2016

@author: tcsshvr
'''

from sys import exit

#Called when the hero escapes from the monster.
def gold_room():
    print("The room is full of gold. How much do you take?")
    
    choice = input(">")
    if(choice<"50"):
        print("Nice, you are not greedy, you win!!!")
        exit(0)
    else:
        dead("You are too greedy")

#Room to the left        
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear.")
    
    #Bear is not moved yet, you are safe.
    bear_moved=False
    
    #Remember, this executes infinite times.
    while(True):
        choice = input(">")
        
        if(choice == "take honey"):
            dead("The bear looks at you and slaps at your face")
        elif(choice == "taunt bear" and not bear_moved):
            bear_moved = True        
        elif(choice == "Open door" and bear_moved):
            gold_room()
        else:
            print("I got no idea what that meant")

#Room to the right            
def cthulhu_room():
    print("Here you see the great evil chutulu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")
      
    choice = input(">")
      
    if(choice == "flee"):
        start()
    elif(choice == "head"):
        dead("well that was tasty!")
    else:
        cthulhu_room()
        
def dead(why):
    print(why, "Good job!!!")
    exit(0)
    
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which door you choose:")
    
    choice = input(">")
    
    if(choice == "left"):
        bear_room()
    elif(choice == "right"):
        cthulhu_room()
    else:
        print("You stumble around the room until you starve to death.")
        
start()    