# -*-coding:Utf-8 -*

class Map :

	"""This class aims to display the labyrinth"""

	def __init__(self):
		
		print("Bonjour et bienvenue dans notre jeu de labyrinthe !")

		map_name = input("Veuillez entrer le nom du fichier (.txt) : ")
		print("Vous avez choisi la carte {}.".format(map_name))
		
		self.name = map_name
		self.map = list() 

		with open(map_name,"r") as map : 
			for line in map : 
				# We add each line in self.map and delete spaces characters or backlines with .strip()
				line = line.strip()
				self.map.append(list(line))

	def display_map(self,labyrinth):
		for line in labyrinth :
			for case in line:
				print(case, end= "") # for deleting the brackets
			print("")

	