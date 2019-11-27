# -*-coding:Utf-8 -*

from map import Map
from character import Character
from item import Item
from labyrinth import Labyrinth
import pygame
from pygame.locals import *
from parameters import *

class GameBoard:

	"""This class extracts the differents elements included in the labyrinth : Map, characters, items"""

	def __init__(self):

		self.labyrinth = Map()

		self.macgyver = Character(self.labyrinth.map,0,0)
		self.guardian = Character(self.labyrinth.map,14,13)

		self.ether = Item(self.labyrinth.map)
		self.ether.display_item(self.labyrinth.map,"E")
		
		self.tube = Item(self.labyrinth.map)
		self.tube.display_item(self.labyrinth.map,"T")

		self.needle = Item(self.labyrinth.map)
		self.needle.display_item(self.labyrinth.map,"N")
		

	def load_game(self):

		continue_game = True 

		pygame.key.set_repeat(400,30)

		pygame.display.flip()

		while continue_game:

			pygame.init()

			pygame.time.Clock().tick(30)

			# We display the labyrinth graphically from the file labyrinth.py
			labyrinth = Labyrinth(self.labyrinth.map)
			
			for event in pygame.event.get():

				if event.type == QUIT:
					continue_game = False
				
				elif event.type == KEYDOWN:
					if event.key == K_UP:
						self.macgyver.move_up(self.labyrinth.map)
					
					if event.key == K_DOWN:
						self.macgyver.move_down(self.labyrinth.map)

					if event.key == K_LEFT:
						self.macgyver.move_left(self.labyrinth.map)

					if event.key == K_RIGHT:
						self.macgyver.move_right(self.labyrinth.map)				

					if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.ether.pos_x][self.ether.pos_y]:
						self.macgyver.nb_item_picked(self.labyrinth,"E")
						self.labyrinth.map[self.ether.pos_x][self.ether.pos_y] = "M"
						

					if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.tube.pos_x][self.tube.pos_y]:
						self.macgyver.nb_item_picked(self.labyrinth,"T")
						self.labyrinth.map[self.tube.pos_x][self.tube.pos_y] = "M"
						

					if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.needle.pos_x][self.needle.pos_y]:
						self.macgyver.nb_item_picked(self.labyrinth.map,"N")
						self.labyrinth.map[self.needle.pos_x][self.needle.pos_y] = "M"
						
					# End of the game 
					if self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] == self.labyrinth.map[self.guardian.pos_x][self.guardian.pos_y]:
						if len(self.macgyver.inventory) == 3: 
							self.labyrinth.map[self.macgyver.pos_x][self.macgyver.pos_y] = "M"
							labyrinth.win_game()
							continue_game = False 

						else : 
							labyrinth.lose_game()
							continue_game = False
												
			pygame.display.flip()	



		
