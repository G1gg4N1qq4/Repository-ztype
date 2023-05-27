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
screen_width = window_size[0]
screen_height = window_size[1]
screen = pygame.display.set_mode(window_size, 0, 32)

pygame.display.set_caption('Zty.pe')
WHITE = (255,255,255)
BLACK = (0,0,0)
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font("fonts/techno_hideo_bold.ttf", 50)
font3 = pygame.font.Font("fonts/techno_hideo_bold.ttf", 130)

clock = pygame.time.Clock()
fps = 60
timer = 333333



def start(screen, nav, sfondo1, sfondo2, nemici, leveling = False):
    nem.parole = carica_livello(level)
    rocket_sound = pygame.mixer.Sound("audio/rocket-engine.mp3")
    rocket_sound.play(-1,0,0)

    if leveling:
        nemici.maxnem += 2
        nemici.counter = 0
    
    nemici.aggiungi_parola()

    while nav.posy > 0:
        nav.posy -= 5
        screen.blit(sfondo1,(0,0))

        nav.img = pygame.transform.scale(nav.img, nav.size)
        screen.blit(nav.img, (nav.posx, nav.posy))
        pygame.display.flip()
        clock.tick(fps)
    
    nav.posy = window_size[1]
    
    arrival = pygame.mixer.Sound("audio/arrival.mp3")
    arrival.play(-1,0,0)

    while nav.posy != window_size[1] - 100:
        nav.posy -= 1
        screen.blit(sfondo2,(0,0))

        nav.img = pygame.transform.scale(nav.img, nav.size)
        screen.blit(nav.img, (nav.posx, nav.posy))
        pygame.display.flip()
        clock.tick(fps)

    rocket_sound.stop()
    arrival.stop()


#funzioni disegna testo
def disegna_testo(testo, posizione):
    testo_renderizzato = font.render(testo, True, WHITE)
    screen.blit(testo_renderizzato, posizione)

def disegna_testo_centrale(text, font, color, surface, posX, posY):
    scritta = font.render(text, True, color)
    scritta_rect = scritta.get_rect()
    scritta_rect.center = (posX, posY)
    surface.blit(scritta, scritta_rect)



def action(nav, nemici):
    global timer
    global special_shot
    # for event in pygame.event.get():

    for key in alph:
        if pygame.key.get_pressed()[key]:

            if len(nav.muniz) < 1:
                tempomax = 3
            else:
                tempomax = 2
                
            if timer < tempomax:
                timer += 1
                nav.punteggio_round[1] = False
            else:
                nav.shot(nemici, key)

                timer = 0
        
        if pygame.key.get_pressed()[K_RETURN]:

            if special_shot > 0:
                nav.big_shot(nemici)
                special_shot -= 1



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
    global punteggio
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
    file_name = "level1.txt"
    with open(file_name, "r", encoding = "utf-8") as f:
        parole = f.read().split("\n")
    
    return parole


def controlla_vittoria(nemici):
    if len(nemici.actword) < 1:
        return True
    return False

#set immagini
sfondo_immagine = pygame.image.load('immagini/spazio.jpg')
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
sfondo_immagine2 = pygame.image.load('immagini/sfondo.jpg')
sfondo_immagine2 = pygame.transform.scale(sfondo_immagine2, window_size)
sfondo_immagine3 = pygame.image.load('immagini/sfondo2.jpg')
sfondo_immagine3 = pygame.transform.scale(sfondo_immagine3, window_size)


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


destra = False
level = 1
punteggio = 0
vittoria = False
special_shot = 0
# main_music = pygame.mixer.Sound("audio/mainmusic.mp3")



#bottone di play
def bottone_gioca():
    button_width = 150
    button_height = 50
    button_x = screen_width // 2 - button_width // 2
    button_y = screen_height // 2 - button_height // 2 + 100

    play_button = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
    pygame.draw.rect(play_button, (0, 0, 0, 180), pygame.Rect(0, 0, button_width, button_height))
    pygame.draw.rect(play_button, WHITE, pygame.Rect(0, 0, button_width, button_height), 3)

    screen.blit(play_button, (button_x, button_y))
    disegna_testo_centrale("Gioca", font, WHITE, screen, window_size[0]//2, window_size[1]//2 + 100)

#bottone di quit
def bottone_quitta():
    button_width = 150
    button_height = 50
    button_x = screen_width // 2 - button_width // 2
    button_y = screen_height // 2 - button_height // 2 + 160

    play_button = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
    pygame.draw.rect(play_button, (0, 0, 0, 180), pygame.Rect(0, 0, button_width, button_height))
    pygame.draw.rect(play_button, WHITE, pygame.Rect(0, 0, button_width, button_height), 3)

    screen.blit(play_button, (button_x, button_y))
    disegna_testo_centrale("Esci", font, WHITE, screen, window_size[0]//2, window_size[1]//2 + 160)


giocare = True
while giocare:
    screen.blit(sfondo_immagine, (0,0))
    bottone_gioca()
    bottone_quitta()
    disegna_testo_centrale("Benvenuto", font2, WHITE, screen, window_size[0]//2, window_size[1]//2 - 130)
    disegna_testo_centrale("in", font2, WHITE, screen, window_size[0]//2, window_size[1]//2 - 75)
    disegna_testo_centrale("ZTY.PE", font3, WHITE, screen, window_size[0]//2, window_size[1]//2)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 - 25 + 160, 150, 50)
            if button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit() 
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 - 25 + 100, 150, 50)
            if button_rect.collidepoint(mouse_pos):
                giocare = False
    
    pygame.display.update()


#animazione iniziale
start(screen, n, sfondo_immagine, sfondo_immagine2, nem)
sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)

while True:
    #Costruzione sfondo con parola digitata e punteggio
    screen.blit(sfondo_immagine, (0,0))
    disegna_testo(f"Parola: ", (10, 10))
    disegna_testo(f"Punteggio: {punteggio}", (10, 50))
    disegna_testo(f"Electric Camp: {special_shot}", (10, 90))
    # main_music.play(-1,0,0)

    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #controllo vittoria
    if vittoria:
        n, nem = reset(n,nem,False)
        sfondo_immagine = pygame.image.load("immagini/sfondo.jpg")
        sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
        start(screen, n, sfondo_immagine2, sfondo_immagine, nem, True)
        sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
        sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
        vittoria = False
        
        if random.randint(-1,1) == 1:
            special_shot += 1

    else:
        if not n.bloccato:

            for i,nemico in enumerate(nem.actword):
                if n.centrata(nemico):
                    n.draw(nem)
                    n.colpita()
            
            action(n,nem)
            
        
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
                start(screen, n, sfondo_immagine2, sfondo_immagine, nem)
                sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
                sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
                punteggio = 0
            
        vittoria = controlla_vittoria(nem)


    #Disegno dei nemici
    n.draw(nem)
    
    #Aggiornamento punteggio totale
    if n.punteggio_round[1]:
        punteggio += n.punteggio_round[0]
    
    #Azione nemico
    nem.draw()
    pygame.display.flip()
    clock.tick(fps)

