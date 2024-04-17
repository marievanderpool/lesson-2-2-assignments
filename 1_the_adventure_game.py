# Objective:
# To practice the use of nested if statements in creating a simple text-based adventure game.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to guide a user through an adventure game, 
# but it has some errors. Identify and fix them.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2: Setting the Scene

# Based on the corrected code from Task 1, expand the game. If the user chooses "cave",
#  ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes 
# for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You get attacked by giant moths!!")
    elif action == "proceed in the dark":
        print("You stumble into a giant jewel!")
    else:
        pass

    