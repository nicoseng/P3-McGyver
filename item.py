# -*-coding:Utf-8 -*

import random 

class Item :
	
	"""This class displays items randomly in the labyrinth."""

	def __init__(self,labyrinth):
		
		self.pos_x = 0
		self.pos_y = 0
		self.picked = False
		
		while labyrinth[self.pos_x][self.pos_y] != "_":
			self.pos_x = random.randint(0,14)
			self.pos_y = random.randint(0,14)

	def display_item(self,labyrinth,symbol):
		
		labyrinth[self.pos_x][self.pos_y] = symbol

			



				
				
			
		
