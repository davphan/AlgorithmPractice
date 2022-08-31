import pygame

white = (255, 255, 255)

def write(text: str, size: int) -> pygame.Surface:
        """Create a rendered text Surface.

        Args:
            text (String): Text string

        Returns:
            Surface: rendered text Surface
        """
        font = pygame.font.Font('freesansbold.ttf', size)
        name = font.render(text, True, white)
        return name