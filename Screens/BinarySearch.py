import pygame, sys
import random

from setuptools import SetuptoolsDeprecationWarning
from GameFiles.Common import *
from GameFiles.ArraySprite import ArrayElement

class BinarySearch(pygame.Surface):
    """Binary Search demonstration screen from the Algorithm Visualizer

    Args:
        screen (Surface): Display screen
    """
    def __init__(self, screen):
        # display screen
        self.screen = screen
        super().__init__(self.screen.get_size())
        # screen dimensions
        self.width = self.get_width()
        self.height = self.get_height()
        # holds array
        self.array = []
        self.target = None
        # rects
        self.backButton = None
        self.textBox = None

        # initialize screen
        self.update()
        self.step1()

        # draw screen to display
        self.screen.blit(self, (0, 0))

        exit = False
        while not exit:
            pygame.time.Clock().tick(60)

            mouse = pygame.mouse.get_pos()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.backButton.left <= mouse[0] <= self.backButton.right and self.backButton.top <= mouse[1] <= self.backButton.bottom:
                        exit = True


            # PROCESS:
            # Change curr screen
            # - clear
            # - add necessary elements
            # Blit screen to display
            # if num.coords != target:
            #     self.fill((0, 0, 0))
            #     self.blit(title, titleRect)
            #     num.move(target)
            #     self.screen.blit(self, (0, 0))
            # else:
            #     break

            pygame.display.flip()




    def update(self):
        # Blank screen
        self.fill((0, 0, 0))

        # Title
        title = write('Binary Search', 54)
        titleRect = title.get_rect(center=(self.width // 2, self.height // 8))
        self.blit(title, titleRect)

        # Back button
        self.backButton = makeBackButton(self)

        # Text box
        self.textBox = textBox(self, self.width, self.height)



    # STEPS FOR BINARY SEARCH:
    # - Start with sorted array
    # - Check midpoint
    #   - if mid == target, return index
    #   - if mid less than target, repeat with upper half of array
    #   - if midd more than target, repeat with lower half of array
    def step1(self):
        # Create sorted array
        arrLen = 9
        temp = []

        # Randomly set numbers in regular intervals
        for i in range(arrLen):
            temp.append(-99 + random.randint(i * (198 // arrLen), (i + 1) * (198 // arrLen)))

        # Draw array elements and store
        startX = (self.width // 2) - (arrLen * 30)
        startY = (self.height // 3)
        for i, num in enumerate(temp):
            self.array.append(ArrayElement(num, (startX + i * 60, startY), True, self))

        # Track target number
        ind = random.randint(0, arrLen - 1)
        self.target = self.array[ind]

    def step2(self):
        pass