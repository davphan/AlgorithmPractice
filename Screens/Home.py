import pygame
from GameFiles.Common import *

class Home (pygame.Surface):
    """Home Screen for the Algorithm Visualizer.

    Args:
        screen (Surface): Display Screen
    """
    def __init__(self, screen: pygame.Surface) -> pygame.Surface:
        super().__init__(screen.get_size())
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
        # colors
        self.white = (255, 255, 255)

        # create home screen title
        title = write('Algoirthm Visualizer', 52)
        titleRect = title.get_rect(center=(self.width // 2, self.height // 6))
        self.blit(title, titleRect)

        self.createAlgorithmText()

        screen.blit(self, (0, 0))


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

        # list of algorithms as rendered text Surfaces
        searchAlgList = []
        for alg in self.searchAlgStrings:
            searchAlgList.append(write(alg, 24))

        sortAlgList = []
        for alg in self.sortAlgStrings:
            sortAlgList.append(write(alg, 24))

        self.drawAlgLists(searchAlgList, self.searchCol)
        self.drawAlgLists(sortAlgList, self.sortCol)

    def drawAlgLists(self, algList: list, col: int) -> None:
        """Draw each text surface in a list to the Home Screen in the
        specified column

        Args:
            algList (list[Surface]): _description_
            col (_type_): _description_
        """
        for i in range(len(algList)):
            searchAlgCenter = (col, self.titlesHeight + 40 + (i * 30))
            searchAlg = algList[i]
            searchAlgRect = searchAlg.get_rect(center=searchAlgCenter)
            self.blit(searchAlg, searchAlgRect)
