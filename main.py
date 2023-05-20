
from os import system
system("cls")

from navicella import NAVICELLA
from nemici import NEMICI
import pygame, sys
from pygame.locals import *
# from nemici import Nemici
import os
os.system('cls')

pygame.init()

window_size = (480*2, 272*2)
screen = pygame.display.set_mode(window_size, 0, 32)

pygame.display.set_caption('Zty.pe')
font = pygame.font.SysFont(pygame.font.get_default_font(),int(window_size[1]), bold = True, italic = False)
clock = pygame.time.Clock()
fps = 60
timer = 333333

def action(nav):
    global timer
    # for event in pygame.event.get():
    #     print(pygame.event.get())
    for key in alph:
        if pygame.key.get_pressed()[key]:

            
            if timer < 7:
                timer+=1
            else:
                nav.shot()
                timer = 0
            

# nemici = Nemici(screen, (100, 100), (50, 50))

sfondo_immagine = pygame.image.load('immagini/sfondo.jpg')
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size) 


#set navicella
immagine_navicella = pygame.image.load('immagini/navicella.png')
pos = pygame.mouse.get_pos()
posx = pos[0]
posy = pos[1]
n = NAVICELLA(screen, immagine_navicella, (50,50), window_size[0]/2, window_size[1]/2, posx, posy)
nem = NEMICI(screen, (window_size[0]/20, window_size[1]/20))

#controllo del mouse
pygame.mouse.set_visible(True)

#alfabeto
alph = [i for i in range(96,123)]
# print(alph)

# pygame.event.set_blocked(pygame.MOUSEMOTION)
while True:
    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # keys = pygame.key.get_pressed()
    
    pos = pygame.mouse.get_pos()
    posx = pos[0]
    posy = pos[1]
    n.posx = (posx - n.size[0]/2)
    n.posy = (posy - n.size[1]/2)

    screen.blit(sfondo_immagine, (0,0))
    
    
    action(n)
    

    n.draw()
    
    #azione nemico
    nem.aggiungi_parola()
    nem.draw()
    # nemici.draw()
    pygame.display.flip()
    clock.tick(fps)

