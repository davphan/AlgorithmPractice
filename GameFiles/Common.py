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

def makeBackButton(screen: pygame.Surface) -> pygame.Rect:
    """Create a back button for the current screen and return the rectangle for
    button position info

    Args:
        screen (pygame.Surface): Current screen

    Returns:
        pygame.Rect: Rectangle of the back button with positional arguments
    """
    back = write('Back', 24)
    backButton = back.get_rect(center=(50, 50))
    screen.blit(back, backButton)
    return backButton

def textBox(screen: pygame.Surface, screenWidth: int, screenHeight: int) -> pygame.Rect:
    """Create the textbox for the current screen to display instructions/explain
    on-screen events

    Args:
        screen (pygame.Surface): Current screen
        screenWidth (int): Width of the current screen
        screenHeight (int): Height of the current screen

    Returns:
        pygame.Rect: Rectangle of the textbox with positional arguments
    """
    textBoxRect = pygame.Rect(screenWidth // 6, screenHeight // 5 * 4, screenWidth // 3 * 2, screenHeight // 5)
    pygame.draw.rect(screen, white, textBoxRect)
    return textBoxRect