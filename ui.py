import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class UserInterface():
    
    def init(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Physics simulator')
        self.screen.fill(WHITE)
        pygame.display.update()

    def draw_input_box(self, x, y, surface) -> None:
        user_text = ''
        input_box = pygame.Rect(x, y, 140, 32)


        pass