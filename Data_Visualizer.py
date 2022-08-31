import sys, pygame
from GameFiles.ArraySprite import ArrayElement
from GameFiles.Common import *

from Screens.Home import Home
from Screens.BinarySearch import BinarySearch

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title
pygame.display.set_caption('Algorithm Visualizer')

Home(screen)
# BinarySearch(screen)