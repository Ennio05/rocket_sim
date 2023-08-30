import pygame
from graphing import simulate
import ui
import time
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
def extract_frame_number(filename):
    return int(filename.split("_")[1].split(".")[0])

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

                if system.confirm_button['rect'].collidepoint(event.pos):
                    speed = float(inputs['speed']['text'])
                    angle = int(inputs['angle']['text'])
                    height = float(inputs['height']['text'])
                    
                    graph = simulate(speed, angle, height)
                    system.confirm_button['active'] = True
                    system.draw_confirm_button()

                    pygame.display.flip()

                    graph.run_graph()

                    system.confirm_button['active'] = False
                    
                    filenames = os.listdir('graphs/simulation')
                    sorted_filenames = sorted(filenames, key=extract_frame_number)
                    for filename in sorted_filenames:
                        graph_list.append(pygame.image.load(f'graphs/simulation/{filename}'))

                    frame = 1

            if event.type == pygame.KEYDOWN:
                for input in inputs:
                    if True in inputs[input].values():
                        if event.key == pygame.K_BACKSPACE:
                            inputs[input]['text'] = inputs[input]['text'][:-1]
                        else:
                            inputs[input]['text'] += event.unicode

    for input in inputs:
        system.draw_input_box(input)

    system.draw_confirm_button()

    if graph_list:
        placeholder = pygame.transform.smoothscale(graph_list[frame - 1], ((SCREEN_WIDTH//5 * 3) - 10, SCREEN_HEIGHT - 110))
        screen.blit(placeholder, (455, 55))
        if frame == len(graph_list):
            pass
        else:
            frame += 1
    else:
        system.draw_border()
            
    pygame.display.flip()

    clock.tick(30)
    
        