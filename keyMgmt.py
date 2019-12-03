# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *


class KeyMgmt:

	""" This class manages the different keys available for the game."""
	
	def select_key(self,labyrinth,character): 

		for event in pygame.event.get():

			if event.type == QUIT:
				continue_game = False
		
			elif event.type == KEYDOWN:

				if event.key == K_q:
					continue_game = False
				
				if event.key == K_UP:
					character.move_up(labyrinth)
				
				if event.key == K_DOWN:
					character.move_down(labyrinth)

				if event.key == K_LEFT:
					character.move_left(labyrinth)

				if event.key == K_RIGHT:
					character.move_right(labyrinth)