import pygame

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 850
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.font.init()
text_font = pygame.font.Font(None, 32)

class UserInterface():

    text_inputs = {}
    screen: pygame.Surface
    confirm_button: pygame.Rect

    def __init__(self, surface) -> None:

        label_font = pygame.font.Font(None, 32)

        self.screen = surface

        self.confirm_button = pygame.Rect(50, 400, 240, 32)

        self.confirm_button = {'text': 'START SIMULATION', 'active': False, 'rect': pygame.Rect(50, 400, 240, 32)}

        speed_text = label_font.render('SPEED', True, BLACK)
        angle_text = label_font.render('ANGLE', True, BLACK)
        height_text = label_font.render('HEIGHT', True, BLACK)

        speed_input = {'text': '', 'active': False, 'rect': self.render_input_box(150, 100), 'label': speed_text}
        angle_input = {'text': '', 'active': False, 'rect': self.render_input_box(150, 200), 'label': angle_text}
        height_input = {'text': '', 'active': False, 'rect': self.render_input_box(150, 300), 'label': height_text}

        self.text_inputs['speed'] = speed_input
        self.text_inputs['angle'] = angle_input
        self.text_inputs['height'] = height_input
        
    def render_input_box(self, x, y) -> pygame.Rect:
        rect = pygame.Rect(x, y, 140, 32)
        return rect
    
    def color_state(self, state):
        if state == False:
            color = pygame.Color('chartreuse4')
        else:
            color = pygame.Color('lightskyblue3')

        return color

    def center_text(self, target, text):
        x = target.width // 2 + target.x - text.get_rect().width//2
        y = target.height // 2 + target.y - text.get_rect().height//2
        return (x, y)
    
    def draw_input_box(self, type):
        color = self.color_state(self.text_inputs[type]['active'])
        pygame.draw.rect(self.screen, color, self.text_inputs[type]['rect'])

        label_text = text_font.render(self.text_inputs[type]['text'], True, WHITE)
        self.screen.blit(label_text, self.center_text(self.text_inputs[type]['rect'], label_text))

        self.screen.blit(self.text_inputs[type]['label'], (self.text_inputs[type]['rect'].x - 100, self.text_inputs[type]['rect'].y + 5))
    
    def draw_border(self):
        pygame.draw.rect(self.screen, pygame.Color(BLACK), pygame.Rect(450, 50, SCREEN_WIDTH//5 * 3, SCREEN_HEIGHT - 100))
        pygame.draw.rect(self.screen, pygame.Color(WHITE), pygame.Rect(455, 55, (SCREEN_WIDTH//5 * 3) - 10, SCREEN_HEIGHT - 110))

    def draw_confirm_button(self):
        pygame.draw.rect(self.screen, pygame.Color(self.color_state(self.confirm_button['active'])), self.confirm_button['rect'])
        if self.confirm_button['active'] == False:
            confirm_text = text_font.render('SIMULATE GRAPH', True, BLACK)
        else:
            confirm_text = text_font.render('RENDERING GRAPH', True, BLACK)
        self.screen.blit(confirm_text, self.center_text(self.confirm_button['rect'], confirm_text))



# https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/



# MOUSE DOWN --> TURN INPUT ACTIVE --> ASSIGN DIFFERENT TEXT INPUTS FOR SEPERATE BOXES --> MOUSE DOWN OFF BOX --> NOT ACTIVE