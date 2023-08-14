import pygame
from graphing import simulate
import ui
import os

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 850
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

inputs = system.text_inputs

image = None
graph_list = []

run = True
while run:
      
    for event in pygame.event.get():
        #if an in=game event is activated and it is the QUIT event (closing the window), the program stops
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for input in inputs:
                    if inputs[input]['rect'].collidepoint(event.pos):
                        inputs[input]['active'] = True
                    else:
                        inputs[input]['active'] = False

                if system.confirm_button.collidepoint(event.pos):
                    speed = int(inputs['speed']['text'])
                    angle = int(inputs['angle']['text'])
                    height = int(inputs['height']['text'])
                    graph = simulate(speed, angle, height)
                    graph.run_graph()
                    for filename in os.listdir('graphs/simulation'):
                        graph_list.append(pygame.image.load(f'graphs/simulation/{filename}'))

                    frame = 0

            if event.type == pygame.KEYDOWN:
                for input in inputs:
                    if True in inputs[input].values():
                        if event.key == pygame.K_BACKSPACE:
                            inputs[input]['text'] = inputs[input]['text'][:-1]
                        else:
                            inputs[input]['text'] += event.unicode

    for input in inputs:
        color = system.color_state(inputs[input]['active'])
        pygame.draw.rect(screen, color, inputs[input]['rect'])

        label_text = text_font.render(inputs[input]['text'], True, WHITE)
        screen.blit(label_text, system.center_text(inputs[input]['rect'], label_text))

        screen.blit(inputs[input]['label'], (inputs[input]['rect'].x - 100, inputs[input]['rect'].y + 5))

    pygame.draw.rect(screen, pygame.Color('chartreuse4'), system.confirm_button)
    confirm_text = text_font.render('START SIMULATION', True, BLACK)
    center_cord = ((system.confirm_button.width // 2 + system.confirm_button.x - confirm_text.get_rect().width//2), system.confirm_button.y - 5)

    screen.blit(confirm_text, system.center_text(system.confirm_button, confirm_text))

    if graph_list:
        screen.blit(graph_list[frame], (300, 50))
        if frame == len(graph_list):
            break
        else:
            frame += 1
    

    pygame.display.flip()

    clock.tick(30)
    
        