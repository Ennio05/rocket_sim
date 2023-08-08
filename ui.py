import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class UserInterface():

    text_inputs = []

    def __init__(self, surface) -> None:

        label_font = pygame.font.Font(None, 32)

        self.screen = surface

        speed_text = label_font.render('SPEED', True, BLACK)
        angle_text = label_font.render('ANGLE', True, BLACK)
        height_text = label_font.render('HEIGHT', True, BLACK)

        speed_input = {'text': '', 'active': False, 'rect': self.draw_input_box(150, 100), 'label': speed_text}
        angle_input = {'text': '', 'active': False, 'rect': self.draw_input_box(150, 200), 'label': angle_text}
        height_input = {'text': '', 'active': False, 'rect': self.draw_input_box(150, 300), 'label': height_text}

        self.text_inputs.extend([speed_input, angle_input, height_input])

    def draw_input_box(self, x, y) -> pygame.Rect:
        input_box = pygame.Rect(x, y, 140, 32)
        return input_box
    
    def color_state(self, state):
        if state == False:
            color = pygame.Color('chartreuse4')
        else:
            color = pygame.Color('lightskyblue3')

        return color




# https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/



# MOUSE DOWN --> TURN INPUT ACTIVE --> ASSIGN DIFFERENT TEXT INPUTS FOR SEPERATE BOXES --> MOUSE DOWN OFF BOX --> NOT ACTIVE