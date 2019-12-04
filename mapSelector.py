#! /usr/bin/env/python3.7.3
# coding: utf-8 

class MapSelector :

	"""This class is used to choose the map from a file ending by .txt"""

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