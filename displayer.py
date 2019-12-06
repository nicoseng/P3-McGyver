#! /usr/bin/env/python3.7.3
# coding: utf-8 

import pygame
from pygame.locals import *
from parameters import *
from keyMgmt import KeyMgmt

class Displayer:
	
	"""This class manages the graphic aspects of the labyrinth"""

	def __init__(self):

		# Window display parameters
		self.window = pygame.display.set_mode((labyrinth_size,labyrinth_size),RESIZABLE)
		self.title = pygame.display.set_caption("MacGyver Labyrinth") 

		# Elements of the game
		self.wall_img = pygame.image.load("ressource/wall.png").convert_alpha()
		self.path_img = pygame.image.load("ressource/path.png").convert_alpha()

		self.macgyver_img = pygame.image.load("ressource/macgyver.png").convert_alpha()
		self.guardian_img = pygame.image.load("ressource/guardian.png").convert_alpha()

		self.ether_img = pygame.image.load("ressource/ether.png").convert_alpha()
		self.tube_img = pygame.image.load("ressource/tube.png").convert_alpha()
		self.needle_img = pygame.image.load("ressource/aiguille.png").convert_alpha()

	# This function aims to display the map graphically on the screen
	def display_map(self,labyrinth):

		line_position = 0 # we start from the first line at the beginning
			
		for line in labyrinth:
						
			element_position = 0 # we start from the first element at the beginning
			
			for element in line:

				x = line_position * sprite_size
				y = element_position * sprite_size 
				
				if element == "#":
					self.window.blit(self.wall_img,(y,x))

				if element == "_":
					self.window.blit(self.path_img,(y,x))

				if element == "M":
					self.window.blit(self.macgyver_img,(y,x))

				if element == "E":
					self.window.blit(self.ether_img,(y,x))

				if element == "T":
					self.window.blit(self.tube_img,(y,x))

				if element == "N":
					self.window.blit(self.needle_img,(y,x))

				if element == "G":
					self.window.blit(self.guardian_img,(y,x))

				element_position = element_position + 1
			line_position = line_position + 1

	# To display the number of items picked by the character.
	def display_inventory(self,inventory):
		item_text_font = pygame.font.Font("roboto/Roboto-Medium.ttf",20)
		item_text = item_text_font.render("Items collected : {}/3".format(len(inventory)),True, white)
		item_text_rect = item_text.get_rect()
		item_text_rect.centerx, item_text_rect.centery = labyrinth_size / 2,10
		self.window.blit(item_text,item_text_rect)

	# When the player wins the game, we display a victory text.
	def display_victory_text(self):
		win_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
		win_text = win_font.render("You win !",True, green)
		win_text_rect = win_text.get_rect()
		win_text_rect.centerx, win_text_rect.centery = labyrinth_size / 2, labyrinth_size / 2 # to center the text
		self.window.blit(win_text,win_text_rect)

	# When the player loses the game, we display a failure text.
	def display_failure_text(self):
		lose_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
		lose_text = lose_font.render("You lose !",True, red)
		lose_text_rect = lose_text.get_rect()
		lose_text_rect.centerx, lose_text_rect.centery = labyrinth_size / 2, labyrinth_size / 2 # to center the text
		self.window.blit(lose_text,lose_text_rect)
	
	# to indicate to the player how to exit the game
	def display_stop_game(self):
		stop_font = pygame.font.Font("roboto/Roboto-Medium.ttf",20)
		stop_text = stop_font.render("Press q to exit",True, white)
		stop_text_rect = stop_text.get_rect()
		stop_text_rect.centerx, stop_text_rect.centery = labyrinth_size / 2, labyrinth_size / 3 # to center the text
		self.window.blit(stop_text,stop_text_rect)