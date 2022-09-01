import pygame

class ArrayElement(pygame.Surface):

    def __init__(self, num, coords, visible, screen):
        super().__init__((60, 60))

        # instance variables
        self.val = num
        self.coords = coords
        self.screen = screen
        self.speed = 5
        self.visible = visible

        # position number
        start = 21
        if int(num) < -9:
            start = 5
        elif int(num) < 0 or int(num) > 9:
            start = 12

        # draw array element
        num = str(num)
        white = (255, 255, 255)
        gray = (105,105,105)
        color = white
        if not visible:
            color = gray
        pygame.draw.rect(self, color, pygame.Rect((0, 0), self.get_size()), 5)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(num, True, color)
        self.blit(text, (start, 15))

        # draw onto screen
        screen.blit(self, self.coords)

    def move(self, target):
        if target != self.coords:
            x = self.coords[0]
            y = self.coords[1]
            tx = target[0]
            ty = target[1]

            # move towards target
            if x < tx:
                if tx - x < self.speed:
                    x = tx
                else:
                    x += self.speed
            if y < ty:
                if ty - y < self.speed:
                    y = ty
                else:
                    y += self.speed
            if x > tx:
                if x - tx < self.speed:
                    x = tx
                else:
                    x -= self.speed
            if y > ty:
                if y - ty < self.speed:
                    y = ty
                else:
                    y -= self.speed

            self.coords = (x, y)

            self.screen.blit(self, self.coords)

    def changeState(self):
        if self.visible:
            self.__init__(self.num, self.coords, False, self.screen)
        else:
            self.__init__(self.num, self.coords, True, self.screen)
