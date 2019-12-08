#! /usr/bin/env/python3.7.3
# coding: utf-8 

class Character:
	
	""" This class describes the actions available for the character"""

	def __init__(self,labyrinth,pos_x,pos_y):
		
		# pos_x stands for position in line.
		self.pos_x = pos_x 
		# pos_y stands for position in column
		self.pos_y = pos_y 
		self.inventory = []
		
	def move_left(self,labyrinth):

		if labyrinth[self.pos_x][self.pos_y - 1] != "#":
			labyrinth[self.pos_x][self.pos_y - 1] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_y = self.pos_y - 1

	def move_right(self,labyrinth):
		
		if labyrinth[self.pos_x][self.pos_y + 1] != "#":
			labyrinth[self.pos_x][self.pos_y + 1] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_y = self.pos_y + 1

	def move_up(self,labyrinth):
		
		if labyrinth[self.pos_x - 1][self.pos_y] != "#":
			labyrinth[self.pos_x - 1][self.pos_y] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_x = self.pos_x - 1

	def move_down(self,labyrinth):
		
		if labyrinth[self.pos_x + 1][self.pos_y] != "#":
			labyrinth[self.pos_x + 1][self.pos_y] = "M"
			labyrinth[self.pos_x][self.pos_y] = "_"
			self.pos_x = self.pos_x + 1
		
	def pick_item(self,labyrinth,symbol):
		
		if not symbol in self.inventory:

			self.inventory.append(symbol)
			