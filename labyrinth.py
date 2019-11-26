# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from constantes import *

class Labyrinth:
	
	""" This class displays the labyrinth with Pygame"""

	def __init__(self,labyrinth):

		pygame.init()

		line_position = 0 # we go from the first line at the beginning
			
		for line in labyrinth:
						
			element_position = 0 # we go from the first element at the beginning
			
			for element in line:

				x = line_position * sprite_size
				y = element_position * sprite_size 
				
				if element == "#":
					window.blit(wall,(y,x))

				if element == "_":
					window.blit(path,(y,x))

				if element == "M":
					window.blit(macgyver,(y,x))

				if element == "E":
					window.blit(ether,(y,x))

				if element == "T":
					window.blit(tube,(y,x))

				if element == "N":
					window.blit(needle,(y,x))

				if element == "G":
					window.blit(guardian,(y,x))

				element_position = element_position + 1
			line_position = line_position + 1

	
