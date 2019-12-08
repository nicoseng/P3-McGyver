#! /usr/bin/env/python3.7.3
# coding: utf-8 

import pygame
from pygame.locals import *
import sys


class KeyManagement:

	""" This class manages the different keys available for the game."""
	
	def select_key(self,labyrinth,character): 

		for event in pygame.event.get():

			# to exit the game
			if event.type == QUIT:
				sys.exit()
		
			elif event.type == KEYDOWN:

				# to exit the game anytime or at the end of the game
				if event.key == K_q:
					sys.exit()
				
				if event.key == K_UP:
					character.move_up(labyrinth)
				
				if event.key == K_DOWN:
					character.move_down(labyrinth)

				if event.key == K_LEFT:
					character.move_left(labyrinth)

				if event.key == K_RIGHT:
					character.move_right(labyrinth)

