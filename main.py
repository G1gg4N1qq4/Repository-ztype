
from os import system
system("cls")
import random


from navicella import NAVICELLA
from nemici import NEMICI
from griglia import GRIGLIA
import pygame, sys
import string
from pygame.locals import *
# from nemici import Nemici
import os
os.system('cls')
pygame.mixer.init(44100, -16, 10, 512)
pygame.mixer.set_num_channels(10)
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

punteggio = 0


# def local_device_score(player, score):
#     scores = []
#     with open("SCORE.txt", "r", encoding = "utf-8") as file:
#         i = 0
#         for line in file:
#             line = line.strip().split(": ")
#             scores.append([line[0], int(line[1])])
#             i+=1
    
#     trovato = True
#     for i,players in enumerate(scores):
#         if players[0] == player:
#             scores[i][1] = score 
#         else:
#             trovato = False
            
#     if trovato == False:
#         scores.append([player, score])
    
#     scores.sort(key = lambda x: -x[1])
#     with open("SCORE.txt", "w", encoding = "utf-8") as file:
#         for player_score in scores:
#             file.write(f"{player_score[0]}: {player_score[1]}\n")
            
def players_data():
    
    finished = False
    player = ""
    timer = 0

    
    while not finished:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        
        if timer == 0:
            if pygame.key.get_pressed()[K_BACKSPACE] and len(player) != 0:
                player= player[0:len(player) - 1:]
                timer = 240
                print("!!")    
            elif pygame.key.get_pressed()[K_RETURN]:
                finished = True
                print("!")
        else:
            timer -=1
            

        for key in alph :
            if timer == 0:
                if pygame.key.get_pressed()[key]:
                    player += chr(key)
                    timer = 240
            else:
                timer -= 1

        
        print(player)
        disegna_testo_centrale(f"Name: {player}",font,(255,255,255), screen, screen_width/2, screen_height/2)
        
        pygame.display.flip()
        clock.tick(fps)
        
    return player
        
        

                
        
def show_scores(name, score):
    finished = False
    global screen, sfondo_immagine
    g = GRIGLIA(screen, (480*2/2, 272*2 - 20))
    g.local_device_score(name, score)
    while not finished:
        screen.blit(sfondo_immagine, (0,0))
        for event in pygame.event.get():
            if pygame.key.get_pressed()[K_RETURN]:
                finished = True
        
        
        g.draw()
        
        pygame.display.flip()
        clock.tick(fps)

    return 0
    
        
        
    # with open("SCORE.txt", "r", encoding = "utf-8") as file:
    #     for line in file:
    #         pass
def start(screen, nav, sfondo1, sfondo2, nemici, level = 1):
    global sfon1, sfon2, posy1,posy2, sfondo_immagine2
    nem.parole = carica_livello(level)
    rocket_sound = pygame.mixer.Sound("audio/rocket-engine.wav")
    rocket_sound.play(-1,0,0)

    if level > 1:
        nemici.maxnem += 2
    nemici.counter = 0
    
    nemici.aggiungi_parola()

    while nav.posy > 0:
        if level <= 1:
            posy1,posy2 = moving_background(screen, sfon1, sfon2, posy1, posy2)
        else:
            screen.blit(sfondo_immagine2,(0,0))
        nav.posy -= 5

        nav.img = pygame.transform.scale(nav.img, nav.size)
        screen.blit(nav.img, (nav.posx + nav.size[0]/2, nav.posy + nav.size[1]/2))
        pygame.display.flip()
        clock.tick(fps)
    
    nav.posy = window_size[1]
    
    arrival = pygame.mixer.Sound("audio/arrival.wav")
    rocket_sound.stop()
    arrival.play(-1,0,0)

    while nav.posy != window_size[1] - 100:
        nav.posy -= 1
        screen.blit(sfondo2,(0,0))

        nav.img = pygame.transform.scale(nav.img, nav.size)
        screen.blit(nav.img, (nav.posx, nav.posy))
        pygame.display.flip()
        clock.tick(fps)

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
    global special_shot, shot_sound, main_music
    # for event in pygame.event.get():
    pygame.mixer.init()
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
                # nav.punteggio_round[1] = False
                # i=1 
                # while pygame.mixer.Channel(i).get_sound() != None:
                #     i += 1
                    # print(pygame.mixer.Channel(i).get_sound())
                pygame.mixer.Channel(1).play(shot_sound)
                timer = 0
                return True, False
                
        
        tempomax = 360
        if pygame.key.get_pressed()[K_RETURN]:
            if timer < tempomax:
                timer += 1
            else:
                if special_shot > 0 :
                    nav.big_shot(nemici)
                    special_shot -= 1
                    
                    timer = 0
                    return False, True

    return False, False

def continua(altezza0):
    conti_img = "Ritornare alla Home?"
    conti_img = font3.render(conti_img, True, (180,180, 180))
    conti_img = pygame.transform.scale(conti_img, ((conti_img.get_width()*window_size[1]/conti_img.get_height())/20,
                                                   window_size[1]/20))
    rect = pygame.Surface((conti_img.get_width() +10, conti_img.get_height() + 10), pygame.SRCALPHA)
    pygame.draw.rect(rect, (0, 0, 0, 140), pygame.Rect(0, 0, rect.get_width(), rect.get_height()))
    screen.blit(rect, ((window_size[0] - conti_img.get_width())/2 - 5, altezza0 + conti_img.get_height()/2 + 40 - 5 ))
    screen.blit(conti_img,((window_size[0] - conti_img.get_width())/2, altezza0 + conti_img.get_height()/2 + 40 ))
    



def reset(navicella, nemici, destra, leveling = True):
    global punteggio, soundtime

    soundtime = 1
    if not destra:
        if leveling:
            nemici = NEMICI(screen, (window_size[0]/30, window_size[1]/40) ,(posx,posy),0,None, nemici.maxnem)
            navicella = NAVICELLA(screen, immagine_navicella, (50,50), pygame.rect.Rect(window_size[0]/2, window_size[1]/2, 50, 50), 
                        window_size[0]/2 - 50, window_size[1] - 100)
        else:
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

def moving_background(screen, sfondo1,sfondo2, posy1, posy2):
    global window_size
    screen.blit(sfondo1, (0,posy1))
    screen.blit(sfondo2, (0, posy2))
    if posy1 >= window_size[1]:
        posy1 =-window_size[1] + 1
    else:
        posy1 += 1

    if posy2 >= window_size[1]:
        posy2 = -window_size[1] + 1
    else:
        posy2 += 1
        
    return posy1,posy2
    
#set immagini
sfondo_immagine = pygame.image.load('immagini/spazio.png')
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
alph.append(32)

destra = False
level = 1
punteggio = 0
playername = ""
vittoria = False
special_shot = 3
main_music = pygame.mixer.Sound("audio/mainmusic.mp3")
# main_music.set_volume(0.3)


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

def bottone_home():
    button_width = 150
    button_height = 50
    button_x = screen_width // 2 - button_width // 2
    button_y = screen_height // 2 - button_height // 2 + 100

    play_button = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
    pygame.draw.rect(play_button, (0, 0, 0, 180), pygame.Rect(0, 0, button_width, button_height))
    pygame.draw.rect(play_button, WHITE, pygame.Rect(0, 0, button_width, button_height), 3)

    screen.blit(play_button, (button_x, button_y))
    disegna_testo_centrale("Home", font, WHITE, screen, window_size[0]//2, window_size[1]//2 + 100)
    
def bottone_punteggi():
    button_width = 150
    button_height = 50
    button_x = screen_width // 2 - button_width // 2
    button_y = screen_height // 2 - button_height // 2 + 220

    play_button = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
    pygame.draw.rect(play_button, (0, 0, 0, 180), pygame.Rect(0, 0, button_width, button_height))
    pygame.draw.rect(play_button, WHITE, pygame.Rect(0, 0, button_width, button_height), 3)

    screen.blit(play_button, (button_x, button_y))
    disegna_testo_centrale("Scores", font, WHITE, screen, window_size[0]//2, window_size[1]//2 + 220)

    
    
# menu_sound.play(-1)
sfon1 = sfondo_immagine 
sfon1 = pygame.transform.scale(sfondo_immagine, window_size)
sfon2 = sfon1
posy1 = 0
posy2 = window_size[1]

def schermata_iniziale():
    global screen, sfon1, sfon2, posy1, posy2, window_size, WHITE, playername
    global font, font2, font3, n, punteggio, menu_sound
    giocare = False
    pygame.mixer.init()
    menu_sound = pygame.mixer.Sound("audio/start_menu_audio.wav")
    menu_sound.set_volume(5)
    menu_sound.play(-1)
    
    while not giocare:
        # screen.blit(sfondo_immagine, (0,0))
        posy1,posy2 = moving_background(screen, sfon1, sfon2, posy1, posy2)
        bottone_gioca()
        bottone_quitta()
        disegna_testo_centrale("Benvenuto", font2, WHITE, screen, window_size[0]//2, window_size[1]//2 - 130)
        disegna_testo_centrale("in", font2, WHITE, screen, window_size[0]//2, window_size[1]//2 - 75)
        disegna_testo_centrale("ZTY.PE", font3, WHITE, screen, window_size[0]//2, window_size[1]//2)
        n.img = pygame.transform.scale(n.img, n.size)
        screen.blit(n.img, (n.posx + n.size[0]/2 , n.posy + n.size[1]/2 + 10))

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
                else:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 - 25 + 100, 150, 50)
                    if button_rect.collidepoint(mouse_pos):
                        giocare = True
        
        pygame.display.update()
     
    playername = players_data()
    menu_sound.stop()
    start(screen, n, sfondo_immagine, sfondo_immagine2, nem)
    punteggio = 0
    # pygame.mixer.quit()
    # pygame.mixer.init()



schermata_iniziale()
shot_sound = pygame.mixer.Sound("audio/shot.mp3")
shot_sound.set_volume(0.3)
explsound = pygame.mixer.Sound("audio/explosionmusic.wav")
#animazione iniziale
sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
livello = 1
tempo = 0

soundtime = 1
while True:
    #Costruzione sfondo con parola digitata e punteggio
    screen.blit(sfondo_immagine, (0,0))
    disegna_testo(f"Level: {livello}", (10, 10))
    disegna_testo(f"Punteggio: {punteggio}", (10, 50))
    disegna_testo(f"Electric Camp: {special_shot}", (10, 90))
    main_music.set_volume(0.1)
    explsound.set_volume(0.3)
    main_music.play(-1,0,0)


    

    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #controllo vittoria
    if vittoria:
        livello += 1
        n.muniz = []
        n, nem = reset(n,nem,False, True)
        n.punteggio_round[1] = False
        sfondo_immagine = pygame.image.load("immagini/sfondo.jpg")
        sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
        start(screen, n, sfondo_immagine2, sfondo_immagine, nem, livello)
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

            
            action(n,nem)[0]

                
            
            
            
            #Disegno dei nemici
            n.draw(nem)
            
            #Aggiornamento punteggio totale
            if n.punteggio_round[1]:
                punteggio += n.punteggio_round[0]
                n.punteggio_round[1] = False
            
            #Azione nemico
            nem.draw()
            
        
        else:
            main_music.stop()
            sfondo_immagine = pygame.image.load("immagini/sfondo.jpg")
            sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
            n.img = pygame.image.load("immagini/Exp.png")
            if soundtime==1:
                explsound.play(0,0,0)
                soundtime -= 1 
            
            n.draw(nem)
            
            
            sconfitta = font3.render("game over", True, (200,20,20), None)
            sconfitta = pygame.transform.scale(sconfitta,((sconfitta.get_width()*window_size[1]/sconfitta.get_height())/7,(window_size[1]/7)))
            screen.blit(sconfitta, ((window_size[0] - sconfitta.get_width())/2, (window_size[1]/2 - sconfitta.get_height())))   
            livello = 0
            continua( (window_size[1]/2 - sconfitta.get_height()/2))
            bottone_home()
            bottone_quitta()
            bottone_punteggi()
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
                    else:
                        mouse_pos = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 - 25 + 100, 150, 50)
                        if button_rect.collidepoint(mouse_pos):
                            pygame.mixer.quit()
                            n, nem = reset(n,nem,destra)
                            schermata_iniziale()
                        else:
                            mous_pos = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(screen_width // 2 - 75, screen_height // 2 - 25 + 200, 150, 50)
                            if button_rect.collidepoint(mouse_pos):
                                show_scores(playername, punteggio)
                # sfondo_immagine = pygame.image.load("immagini/sfondo.jpg")
                # sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
                # start(screen, n, sfondo_immagine2, sfondo_immagine, nem)
                # sfondo_immagine = pygame.image.load("immagini/sfondo2.jpg")
                # sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size)
            
        vittoria = controlla_vittoria(nem)


    pygame.display.flip()
    clock.tick(fps)

