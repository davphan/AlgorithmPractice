import pygame

class ArrayElement(pygame.Surface):

    def __init__(self, num, coords, screen):
        super().__init__((60, 60))

        # instance variables
        self.coords = coords
        self.screen = screen
        self.speed = 5

        # position number
        start = 21
        if int(num) < -9:
            start = 5
        elif int(num) < 0 or int(num) > 9:
            start = 12

        # draw array element
        num = str(num)
        white = (255, 255, 255)
        pygame.draw.rect(self, white, pygame.Rect((0, 0), self.get_size()), 5)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(num, True, white)
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
