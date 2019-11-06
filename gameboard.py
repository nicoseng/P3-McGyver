# -*-coding:Utf-8 -*

from map import Map
from character import Character
from item import Item

class GameBoard:

	"""This class defines the level of the maze with the differents elements included inside"""

	def __init__(self):

		self.labyrinth = Map()

		self.macgyver = Character(self.labyrinth.map,1,1)
		self.guardian = Character(self.labyrinth.map,14,13)

		self.ether = Item(self.labyrinth.map)
		self.ether.display_item(self.labyrinth.map,"E")


		self.tube = Item(self.labyrinth.map)
		self.tube.display_item(self.labyrinth.map,"T")


		self.needle = Item(self.labyrinth.map)
		self.needle.display_item(self.labyrinth.map,"N")


		self.labyrinth.display_map(self.labyrinth.map)
	

	def load_game(self):

		continue_game = True

		while continue_game :
			

			choice = input("Que décidez-vous ? (gauche = g, droite = d, haut = h, bas = b, quitter = q : ")

			if choice == "g":
				self.macgyver.move_left(self.labyrinth.map)
			
			if choice == "d":
				self.macgyver.move_right(self.labyrinth.map)

			if choice == "h":
				self.macgyver.move_up(self.labyrinth.map)

			if choice == "b":
				self.macgyver.move_down(self.labyrinth.map)

			self.labyrinth.display_map(self.labyrinth.map)

			# Quit the game
			if choice == "q":
				print("Merci d'avoir joué et à bientôt !")
				break

			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.ether.pos_x][self.ether.pos_y]:
				self.ether.picked = True
				self.macgyver.nb_item_picked(self.labyrinth,"E")
				self.labyrinth.map[self.ether.pos_x][self.ether.pos_y] = "_"
				continue

			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.tube.pos_x][self.tube.pos_y]:
				self.tube.picked = True
				self.macgyver.nb_item_picked(self.labyrinth,"T")
				self.labyrinth.map[self.tube.pos_x][self.tube.pos_y] = "_"
				continue

			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.needle.pos_x][self.needle.pos_y]:
				self.needle.picked = True
				self.macgyver.nb_item_picked(self.labyrinth.map,"N")
				self.labyrinth.map[self.needle.pos_x][self.needle.pos_y] = "_"
				continue

			# End of the game 
			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.guardian.pos_x][self.guardian.pos_y]:
				if self.tube.picked == True and self.needle.picked == True and self.ether.picked == True : 
					self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] = "M"
					print("Vous avez endormi le garde. Gagné!")
					continue_game = False

				else : 
					print("Vous n'avez pas récupéré les 3 objets nécessaires pour endormir le garde. Perdu ! Vous êtes mort.")
					continue_game = False
	


