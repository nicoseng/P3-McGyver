#! /usr/bin/env/python3.7.3
# coding: utf-8 

from mapSelector import MapSelector
from character import Character
from itemMgmt import ItemMgmt
from displayer import Displayer
from keyMgmt import KeyMgmt
import pygame
from pygame.locals import *
from parameters import *

class GameBoard:

	"""This class is used to define the differents elements included in the labyrinth : Map, characters, items"""

	def __init__(self):

		self.labyrinth = MapSelector()

		self.macgyver = Character(self.labyrinth.map,0,0)
		self.guardian = Character(self.labyrinth.map,13,13)

		self.ether = ItemMgmt(self.labyrinth.map)
		self.ether.position_item(self.labyrinth.map,"E")

		self.tube = ItemMgmt(self.labyrinth.map)
		self.tube.position_item(self.labyrinth.map,"T")

		self.needle = ItemMgmt(self.labyrinth.map)
		self.needle.position_item(self.labyrinth.map,"N")

		self.loader = Displayer()
		self.key_controller = KeyMgmt()
	
	def load_game(self):

		pygame.init()

		pygame.key.set_repeat(400,30) 	

		continue_game = True

		while continue_game:

			pygame.time.Clock().tick(30)

			# We load the map to display it on the game board.
			self.loader.display_map(self.labyrinth.map)

			# To display the number of items picked by the player on the screen
			self.loader.display_inventory(self.macgyver.inventory)
			
			# To activate the keys available for the game.
			self.key_controller.select_key(self.labyrinth.map,self.macgyver)
			
			# To play the game properly speaking
			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.ether.pos_x][self.ether.pos_y]:
				self.macgyver.pick_item(self.labyrinth.map,"E")
				self.loader.display_inventory(self.macgyver.inventory)
				self.labyrinth.map[self.ether.pos_x][self.ether.pos_y] = "M"
						
			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.tube.pos_x][self.tube.pos_y]:
				self.macgyver.pick_item(self.labyrinth.map,"T")
				self.loader.display_inventory(self.macgyver.inventory)
				self.labyrinth.map[self.tube.pos_x][self.tube.pos_y] = "M"
				
			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.needle.pos_x][self.needle.pos_y]:
				self.macgyver.pick_item(self.labyrinth.map,"N")
				self.loader.display_inventory(self.macgyver.inventory)
				self.labyrinth.map[self.needle.pos_x][self.needle.pos_y] = "M"
 
			if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.guardian.pos_x][self.guardian.pos_y]:
				if len(self.macgyver.inventory) == 3: 
					self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] = "M"
					self.loader.display_victory_text()
					self.loader.display_stop_game()
					
				else : 
					self.loader.display_failure_text()
					self.loader.display_stop_game()	
			
			pygame.display.flip()	