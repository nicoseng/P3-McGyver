from maps import Map
from labyrinth import *


print("Bonjour et bienvenue dans notre jeu de labyrinthe !")

# We ask to the player to enter the name of the file.
map_choice = input("Veuillez entrer le nom du fichier (.txt) : ")

# We create a Map() type object and we add the file we want to display into a map on argument from the map class.
# We can now use the characteristics of the map Class for our objetc we just created.

labyrinth = Map(map_choice)

print("Vous avez choisi la carte {}.".format(labyrinth.map_name))

# We display the labyrinth line by line for greater clarity with the function display() from the file labyrinth.py
display(labyrinth.map)

# On détermine la position du personnage au niveau des lignes
pos_perso_x = 0
# On détermine la position du personnage au niveau des colonnes
pos_perso_y = 0
pos_perso = labyrinth.map[pos_perso_x][pos_perso_y]


pos_needle = "N"
pos_guardian = "G"
pos_exit = "S"

continue_game = True
while continue_game :

	choice = input("Que décidez-vous ? (gauche = g, droite = d, haut = h, bas = b, quitter = q : ")

	if choice == "d" : 
		if labyrinth.map[pos_perso_x][pos_perso_y + 1] == "_":
			labyrinth.map[pos_perso_x][pos_perso_y + 1] = "M"
			labyrinth.map[pos_perso_x][pos_perso_y] = "_"
			pos_perso_y = pos_perso_y + 1
			display(labyrinth.map)
		else: 
			print("Vous êtes devant un mur, déplacement impossible.")
	
	if choice == "g" : 
		if labyrinth.map[pos_perso_x][pos_perso_y - 1] == "_":
			labyrinth.map[pos_perso_x][pos_perso_y - 1] = "M"
			labyrinth.map[pos_perso_x][pos_perso_y] = "_"
			pos_perso_y = pos_perso_y - 1
			display(labyrinth.map)
		else: 
			print("Vous êtes devant un mur, déplacement impossible.")

	if choice == "h" : 
		if labyrinth.map[pos_perso_x - 1][pos_perso_y] == "_":
			labyrinth.map[pos_perso_x - 1][pos_perso_y] = "M"
			labyrinth.map[pos_perso_x][pos_perso_y] = "_"
			pos_perso_x = pos_perso_x - 1
			display(labyrinth.map)
		else: 
			print("Vous êtes devant un mur, déplacement impossible.")
	
	if choice == "b" : 
		if labyrinth.map[pos_perso_x + 1][pos_perso_y] == "_":
			labyrinth.map[pos_perso_x + 1][pos_perso_y] = "M"
			labyrinth.map[pos_perso_x][pos_perso_y] = "_"
			pos_perso_x = pos_perso_x + 1
			display(labyrinth.map)

		else: 
			print("Vous êtes devant un mur, déplacement impossible.")

	if choice != "g" or choice != "d" or choice != "h" or choice != "b" or choice != "q":
		print("Nous n'avons pas compris votre choix. Veuillez saisir à nouveau un choix.")

	if labyrinth.map[pos_perso_x + 1][pos_perso_y] == "E" :
		print("vous avez récupéré l'éther.")
		labyrinth.map[pos_perso_x + 1][pos_perso_y] = "M"
		labyrinth.map[pos_perso_x][pos_perso_y] = "_"
		pos_perso_x = pos_perso_x + 1
		display(labyrinth.map)

	if labyrinth.map[pos_perso_x][pos_perso_y + 1] == "N" :
		print("vous avez récupéré l'aiguille.")
		labyrinth.map[pos_perso_x][pos_perso_y + 1] = "M"
		labyrinth.map[pos_perso_x][pos_perso_y] = "_"
		pos_perso_y = pos_perso_y + 1
		display(labyrinth.map)

	if labyrinth.map[pos_perso_x][pos_perso_y + 1] == "T" :
		print("vous avez récupéré le tube.")
		labyrinth.map[pos_perso_x][pos_perso_y + 1] = "M"
		labyrinth.map[pos_perso_x][pos_perso_y] = "_"
		pos_perso_y = pos_perso_y + 1
		display(labyrinth.map)

	if labyrinth.map[pos_perso_x + 1][pos_perso_y] == "S" :
		print("vous avez trouvé la sortie. Bien joué !")
		labyrinth.map[pos_perso_x][pos_perso_y] = "M"
		display(labyrinth.map)
		continue_game = False

	if choice == "q":
		print("Merci d'avoir joué et à bientôt !")
		break


		



