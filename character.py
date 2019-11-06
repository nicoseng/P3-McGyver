# -*-coding:Utf-8 -*


class Character:
	""" Class for creating and moving the character"""

	def __init__(self,labyrinth,pos_x,pos_y):
		self.pos_x = pos_x # pos_x stands for position in line
		self.pos_y = pos_y # pos_y stands for position in column
		self.inventory = []
		
	
	def move_left(self,labyrinth):
		if labyrinth[self.pos_x][self.pos_y - 1] != "#":
			labyrinth[self.pos_x][self.pos_y - 1] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_y = self.pos_y - 1
			
		else:
			print("Vous êtes face à un mur, déplacement impossible.")

	def move_right(self,labyrinth):
		if labyrinth[self.pos_x][self.pos_y + 1] != "#":
			labyrinth[self.pos_x][self.pos_y + 1] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_y = self.pos_y + 1
			
		else:
			print("Vous êtes face à un mur, déplacement impossible.")

	def move_up(self,labyrinth):
		if labyrinth[self.pos_x - 1][self.pos_y] != "#":
			labyrinth[self.pos_x - 1][self.pos_y] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_x = self.pos_x - 1
	
		else:
			print("Vous êtes face à un mur, déplacement impossible.")

	def move_down(self,labyrinth):
		
		if labyrinth[self.pos_x + 1][self.pos_y] != "#":
			labyrinth[self.pos_x + 1][self.pos_y] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_x = self.pos_x + 1
			
		else:
			print("Vous êtes face à un mur, déplacement impossible.")
		
	
	def nb_item_picked(self,labyrinth,symbol):
	
		self.inventory.append(symbol)
		print("Vous avez récupéré:",symbol)
		print(self.inventory)
		print("Nombre d'objets récupérés : {}/3".format(len(self.inventory)))	

		
				
		

		
