import sys, pygame
from GameFiles.ArraySprite import ArrayElement
from GameFiles.Common import *
from Screens.Home import Home

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title
pygame.display.set_caption('Algorithm Visualizer')



num = ArrayElement(1, (0, 0), screen)
target = (800, 30)

Home(screen)

# game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.time.Clock().tick(60)

    # if num.coords != target:
    #     screen.fill((0, 0, 0))
    #     num.move(target)



    pygame.display.flip()
