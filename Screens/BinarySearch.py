import pygame, sys
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

        title = write('Binary Search', 54)
        titleRect = title.get_rect(center=(self.width // 2, self.height // 8))
        self.blit(title, titleRect)

        num = ArrayElement(1, (40, 40), self)
        target = (600, 450)


        self.screen.blit(self, (0, 0))

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            pygame.time.Clock().tick(60)

            # PROCESS:
            # Change curr screen
            # - clear
            # - add necessary elements
            # Blit screen to display
            if num.coords != target:
                self.fill((0, 0, 0))
                self.blit(title, titleRect)
                num.move(target)
                self.screen.blit(self, (0, 0))
            else:
                break

            pygame.display.flip()