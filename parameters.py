# -*-coding:Utf-8 -*
import pygame 
from pygame.locals import *

pygame.init()

# Window parameters
sprite_size = 30
sprite_number = 15 
labyrinth_size = sprite_size * sprite_number

# Window details
window = pygame.display.set_mode((labyrinth_size,labyrinth_size),RESIZABLE)
title = pygame.display.set_caption("MacGyver Labyrinth") # Title of the window

# Elements included in the labyrinth
wall = pygame.image.load("ressource/wall.png").convert_alpha()
path = pygame.image.load("ressource/path.png").convert_alpha()

tube = pygame.image.load("ressource/tube.png").convert_alpha()
ether = pygame.image.load("ressource/ether.png").convert_alpha()
needle = pygame.image.load("ressource/aiguille.png").convert_alpha()

macgyver = pygame.image.load("ressource/macgyver.png").convert_alpha()
guardian = pygame.image.load("ressource/guardian.png").convert_alpha()

# Display items collected 
white = (255,255,255) # color of the text
item_text_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
inventory = []
item_text = item_text_font.render("Items collected : {}/3".format(len(inventory)),True, white)
item_text_rect = item_text.get_rect()
item_text_rect.centerx, item_text_rect.centery = labyrinth_size / 2, 100

# Display a text when the player wins the game
green = (51,153,102) # color of the text
win_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
win_text = win_font.render("You win !",True, green)
win_text_rect = win_text.get_rect()
win_text_rect.centerx, win_text_rect.centery = labyrinth_size / 2, labyrinth_size / 2 # to center the text 

# Display a text when the player loses the game
red = (212,0,0) # color of the text
lose_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
lose_text = lose_font.render("You lose !",True, red)
lose_text_rect = lose_text.get_rect()
lose_text_rect.centerx, lose_text_rect.centery = labyrinth_size / 2, labyrinth_size / 2 # to center the text 