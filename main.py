import pygame
from ui import UserInterface

system = UserInterface()

run = True
while run:
      
    for event in pygame.event.get():
        #if an in=game event is activated and it is the QUIT event (closing the window), the program stops
            if event.type == pygame.QUIT:
                run = False