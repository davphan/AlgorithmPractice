import pygame, sys
from GameFiles.Common import *
from Screens.BinarySearch import BinarySearch

class Home (pygame.Surface):
    """Home Screen for the Algorithm Visualizer.

    Args:
        screen (Surface): Display Screen
    """
    def __init__(self, screen: pygame.Surface) -> pygame.Surface:
        # display screen
        self.screen = screen
        super().__init__(self.screen.get_size())
        # screen dimensions
        self.width = self.get_width()
        self.height = self.get_height()
        # algorithm name positions
        self.searchCol = self.width // 4
        self.sortCol = self.searchCol * 3
        self.titlesHeight = self.height // 3
        # algorithm names
        # !!! EDIT AS MORE ARE ADDED !!!
        self.searchAlgStrings = ['Binary Search']
        self.sortAlgStrings = ['Merge Sort', 'Quick Sort', 'Selection Sort']
        self.algTextPos = {} # key: str, val: pygame.Rect
        # colors
        self.white = (255, 255, 255)

        # create home screen title
        title = write('Algoirthm Visualizer', 52)
        titleRect = title.get_rect(center=(self.width // 2, self.height // 6))
        self.blit(title, titleRect)

        # Create algorithm lists and buttons
        self.createAlgorithmText()

        # Draw everything to screen
        self.screen.blit(self, (0, 0))


        # Main game loop
        while 1:
            pygame.time.Clock().tick(60)

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                for alg in self.algTextPos:
                    algRect = self.algTextPos[alg]
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if algRect.left <= mouse[0] <= algRect.right and algRect.top <= mouse[1] <= algRect.bottom:
                            pygame.draw.line(screen, self.white, (algRect.left, algRect.bottom), (algRect.right, algRect.bottom), 2)
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.screen.blit(self, (0, 0))
                        if algRect.left <= mouse[0] <= algRect.right and algRect.top <= mouse[1] <= algRect.bottom:
                            # switch to different screens
                            if alg == 'Binary Search':
                                BinarySearch(self.screen)
                                self.screen.blit(self, (0, 0))

            pygame.display.flip()







    def createAlgorithmText(self) -> None:
        """Generates the algorithm type columns and fills them with all of the
        algorithm name text buttons
        """
        # create algorithm column sections
        searchTitle = write('Search Algorithms', 32)
        searchRect = searchTitle.get_rect(center=(self.searchCol, self.titlesHeight))
        sortTitle = write('Sorting Algorithms', 32)
        sortRect = sortTitle.get_rect(center=(self.sortCol, self.titlesHeight))
        self.blits(((searchTitle, searchRect), (sortTitle, sortRect)), False)

        # draw algorithm buttons
        self.drawAlgLists(self.searchAlgStrings, self.searchCol)
        self.drawAlgLists(self.sortAlgStrings, self.sortCol)

    def drawAlgLists(self, algList: 'list[str]', col: int) -> None:
        """Draw each name in a list to the Home Screen in the
        specified column location

        Args:
            algList (list[str]): _description_
            col (_type_): _description_
        """
        for i in range(len(algList)):
            algCenter = (col, self.titlesHeight + 40 + (i * 30))
            alg = write(algList[i], 24)
            algRect = alg.get_rect(center=algCenter)
            self.blit(alg, algRect)
            self.algTextPos[algList[i]] = algRect
