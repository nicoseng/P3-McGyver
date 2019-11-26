# -*-coding:Utf-8 -*

import pygame 
from pygame.locals import *

# display the maze 
pygame.init()

# Window parameters
sprite_size = 30
sprite_number = 15 
labyrinth_size = sprite_size * sprite_number


# Window details
window = pygame.display.set_mode((labyrinth_size,labyrinth_size),RESIZABLE)
title = pygame.display.set_caption("MacGyver Labyrinth") # Title of the window

# display a text when the player wins the game
green = (51,153,102)
win_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
win_text_surface = win_font.render("You win !",True, green)

# display a text when the player loses the game
red = (212,0,0)
lose_font = pygame.font.Font("roboto/Roboto-Medium.ttf",30)
lose_text_surface = lose_font.render("You lose !",True, red)


# Elements included in the labyrinth
wall = pygame.image.load("ressource/wall.png").convert_alpha()
path = pygame.image.load("ressource/path.png").convert_alpha()
tube = pygame.image.load("ressource/tube.png").convert_alpha()
ether = pygame.image.load("ressource/ether.png").convert_alpha()
needle = pygame.image.load("ressource/aiguille.png").convert_alpha()

macgyver = pygame.image.load("ressource/macgyver.png").convert_alpha()

guardian = pygame.image.load("ressource/guardian.png").convert_alpha()