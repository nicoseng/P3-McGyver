""" This file contains the functions about the labyrinth"""


# We display the labyrinth like a chain list 
def display(labyrinth) :
    for line in labyrinth:
        for character in line:
        	print(character, end= "") # for deleting the brackets
        print("")



