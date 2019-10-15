# -*-coding:Utf-8 -*

""" This file contains the class Map"""

# Create or get back the map in a file. 
# Open the map with Python 
# Stock the map in a variable 
# Display the map with Python


class Map :

	# We write the name of the file containing the map. 
	def __init__(self, map_name):
		self.map_name = map_name
		
		# At the beginning, there is nothing in self.map. We can also write self.map = []
		# We want to display the map into a list for using it for the labyrinth
		self.map = list() 
		

		# We open and stock the file desired in a variable.
		with open(map_name,"r") as map : 

			# For each line in the file
			for line in map : 

				# We add each line in self.map and delete spaces characters or backlines with .strip()
				line = line.strip()
				self.map.append(list(line))  
		
		