import pygame, sys
from pygame.locals import *
# from nemici import Nemici
import os
os.system('cls')

pygame.init()

window_size = (600, 700)
screen = pygame.display.set_mode(window_size, 0, 32)

pygame.display.set_caption('Zty.pe')

clock = pygame.time.Clock()

# nemici = Nemici(screen, (100, 100), (50, 50))

sfondo_immagine = pygame.image.load('immagini/sfondo.png')
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size) 


while True:
    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # keys = pygame.key.get_pressed()

    screen.blit(sfondo_immagine, (0,0))

    # nemici.draw()
    pygame.display.flip()
    clock.tick(60)

