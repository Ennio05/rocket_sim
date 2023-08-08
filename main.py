import pygame
import ui

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

clock = pygame.time.Clock()

text_font = pygame.font.Font(None, 32)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Physics simulator')
screen.fill(WHITE)
pygame.display.update()

system = ui.UserInterface(screen)

run = True
while run:
      
    for event in pygame.event.get():
        #if an in=game event is activated and it is the QUIT event (closing the window), the program stops
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for text_input in system.text_inputs:
                    if text_input['rect'].collidepoint(event.pos):
                        text_input['active'] = True
                    else:
                        text_input['active'] = False

            if event.type == pygame.KEYDOWN:
                for text_input in system.text_inputs:
                    if True in text_input.values():
                        if event.key == pygame.K_BACKSPACE:
                            text_input['text'] = text_input['text'][:-1]
                        else:
                            text_input['text'] += event.unicode

    for text_input in system.text_inputs:
        color = system.color_state(text_input['active'])
        pygame.draw.rect(screen, color, text_input['rect'])

        text_surface = text_font.render(text_input['text'], True, WHITE)
        screen.blit(text_surface, (text_input['rect'].x+5, text_input['rect'].y+5))

        screen.blit(text_input['label'], (text_input['rect'].x - 100, text_input['rect'].y + 5))
    

    pygame.display.flip()

    clock.tick(2)
    
        