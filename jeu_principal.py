# -*-coding:Utf-8 -*

from map import Map
from character import Character
from item import Item


labyrinth = Map()

macgyver = Character(labyrinth.map,1,1)
guardian = Character(labyrinth.map,14,13)

ether = Item(labyrinth.map)
ether.display_item(labyrinth.map,"E")


tube = Item(labyrinth.map)
tube.display_item(labyrinth.map,"T")


needle = Item(labyrinth.map)
needle.display_item(labyrinth.map,"N")


labyrinth.display_map(labyrinth.map)
	
# Main game

continue_game = True

while continue_game :
	

	choice = input("Que décidez-vous ? (gauche = g, droite = d, haut = h, bas = b, quitter = q : ")

	if choice == "g":
		macgyver.move_left(labyrinth.map)
	
	if choice == "d":
		macgyver.move_right(labyrinth.map)

	if choice == "h":
		macgyver.move_up(labyrinth.map)

	if choice == "b":
		macgyver.move_down(labyrinth.map)

	labyrinth.display_map(labyrinth.map)

	# Quit the game
	if choice == "q":
		print("Merci d'avoir joué et à bientôt !")
		break

	if labyrinth.map[macgyver.pos_x][macgyver.pos_y] == labyrinth.map[ether.pos_x][ether.pos_y]:
		ether.picked = True
		macgyver.nb_item_picked(labyrinth.map,"E")
		labyrinth.map[ether.pos_x][ether.pos_y] = "_"
		continue

	if labyrinth.map[macgyver.pos_x][macgyver.pos_y] == labyrinth.map[tube.pos_x][tube.pos_y]:
		tube.picked = True
		macgyver.nb_item_picked(labyrinth.map,"T")
		labyrinth.map[tube.pos_x][tube.pos_y] = "_"
		continue

	if labyrinth.map[macgyver.pos_x][macgyver.pos_y] == labyrinth.map[needle.pos_x][needle.pos_y]:
		needle.picked = True
		macgyver.nb_item_picked(labyrinth.map,"N")
		labyrinth.map[needle.pos_x][needle.pos_y] = "_"
		continue

	

	# End of the game 
	if labyrinth.map[macgyver.pos_x][macgyver.pos_y] == labyrinth.map[guardian.pos_x][guardian.pos_y]:
		if tube.picked == True and needle.picked == True and ether.picked == True : 
			labyrinth.map[macgyver.pos_x][macgyver.pos_y] = "M"
			print("Vous avez endormi le garde. Gagné!")
			continue_game = False

		else : 
			print("Vous n'avez pas récupéré les 3 objets nécessaires pour endormir le garde. Perdu ! Vous êtes mort.")
			continue_game = False
	


