
from os import system
system("cls")
import random

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

def start(screen, nav, sfondo1, sfondo2):
    while nav.posy > 0:
        nav.posy -= 5
        screen.blit(sfondo1,(0,0))

        nav.img = pygame.transform.scale(nav.img, nav.size)
        screen.blit(nav.img, (nav.posx, nav.posy))
        pygame.display.flip()
        clock.tick(fps)
    
    nav.posy = window_size[1]
    
    while nav.posy != window_size[1] - 100:
        nav.posy -= 1
        screen.blit(sfondo2,(0,0))

        nav.img = pygame.transform.scale(nav.img, nav.size)
        screen.blit(nav.img, (nav.posx, nav.posy))
        pygame.display.flip()
        clock.tick(fps)
        
        
def action(nav, nemici):
    global timer
    # for event in pygame.event.get():
    #     print(pygame.event.get())
    for key in alph:
        if pygame.key.get_pressed()[key]:

            if len(nav.muniz) < 1:
                tempomax = 5
            else:
                tempomax = 2
            if timer < tempomax:
                timer+=1
            else:
                nav.shot(nemici, key)

                timer = 0
            
def continua(altezza0, destra):
    conti_img = "CONTINUARE?"
    conti_img = font.render(conti_img, True, (100,0,0))
    conti_img = pygame.transform.scale(conti_img, ((conti_img.get_width()*window_size[1]/conti_img.get_height())/10,
                                                   window_size[1]/10))
    screen.blit(conti_img,((window_size[0] - conti_img.get_width())/2, altezza0 + 10))
    
    si = "SI"
    no = "No"
    if not destra:
        si = font.render(si, True, (0,100,0), (250,250,250))
    else:
        si = font.render(si, True, (0,100,0))
    si = pygame.transform.scale(si, ((si.get_width()*window_size[1]/si.get_height())/20,
                                                   window_size[1]/20))
    screen.blit(si,((window_size[0]/2 - si.get_width()*2 - 5), altezza0 + 10 + conti_img.get_height() + 10))
    
    if destra:
        no = font.render(no, True, (0,100,0), (250,250,250))
    else:
        no = font.render(no, True, (0,100,0))
        
    no = pygame.transform.scale(no, ((no.get_width()*window_size[1]/no.get_height())/20,
                                                   window_size[1]/20))
    screen.blit(no,((window_size[0]/2 + si.get_width()*2 - no.get_width() + 5), altezza0 + 10 + conti_img.get_height() + 10))
    
    
    
def reset(navicella, nemici, destra):
    
    if not destra:
        navicella = NAVICELLA(screen, immagine_navicella, (50,50), pygame.rect.Rect(window_size[0]/2, window_size[1]/2, 50, 50), 
                    window_size[0]/2 - 50, window_size[1] - 100)
        nemici = NEMICI(screen, (window_size[0]/30, window_size[1]/40) ,(posx,posy))
        return navicella, nemici
    else:
        pygame.quit()
        sys.exit()
        
def carica_livello(livello):
    parole = []
    file_name = "level" + f"{livello}" + ".txt"
    with open(file_name, "r", encoding = "utf-8") as f:
        
        parole = f.read().split("\n")
        
            
    return parole
# nemici = Nemici(screen, (100, 100), (50, 50))

sfondo_immagine = pygame.image.load('immagini/sfondo.jpg')
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
sfondo_immagine2 = pygame.image.load('immagini/sfondo.png')
sfondo_immagine2 = pygame.transform.scale(sfondo_immagine, window_size)


#set navicella
immagine_navicella = pygame.image.load('immagini/navicella.png')
# pos = pygame.mouse.get_pos()
posx = window_size[0]/2 - 50
posy = window_size[1] - 100
n = NAVICELLA(screen, immagine_navicella, (50,50), pygame.rect.Rect(window_size[0]/2, window_size[1]/2, 50, 50), 
              posx, posy)
nem = NEMICI(screen, (window_size[0]/30, window_size[1]/40), (n.posx, n.posy))

#controllo del mouse
pygame.mouse.set_visible(True)

#alfabeto
alph = [i for i in range(96,123)]
# print(alph)

# pygame.event.set_blocked(pygame.MOUSEMOTION)
destra = False
level = 1

start(screen, n, sfondo_immagine2, sfondo_immagine)
sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
while True:
    
    screen.blit(sfondo_immagine, (0,0))
    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # keys = pygame.key.get_pressed()
    if not n.bloccato:

        for i,nemico in enumerate(nem.actword):
            if n.centrata(nemico):
                n.draw(nem)
                n.colpita()
        
        action(n,nem)
        
        nem.parole = carica_livello(level)
    else:
        sfondo_immagine = pygame.image.load("immagini/sfondo.jpg")
        sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
        n.img = pygame.image.load("immagini/Exp.png")
        sconfitta = font.render("HAI PERSO", True, (200,20,20), None)
        sconfitta = pygame.transform.scale(sconfitta,((sconfitta.get_width()*window_size[1]/sconfitta.get_height())/5,(window_size[1]/5)))
        screen.blit(sconfitta, ((window_size[0] - sconfitta.get_width())/2, (window_size[1] - sconfitta.get_height())/2 )) 
        
        if pygame.key.get_pressed()[K_RIGHT]:
            destra = True
        
        if pygame.key.get_pressed()[K_LEFT]:
            destra = False
        
        continua( (window_size[1]+ sconfitta.get_height())/2, destra)
        
        if pygame.key.get_pressed()[K_RETURN]:
            n, nem = reset(n,nem,destra)
            sfondo_immagine = pygame.image.load("immagini/sfondo.jpg")
            sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
            start(screen, n, sfondo_immagine2, sfondo_immagine)
            sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
            sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
        
    


    
    n.draw(nem)
    
    #azione nemico
    nem.aggiungi_parola()
    nem.draw()
    # nemici.draw()
    pygame.display.flip()
    clock.tick(fps)

