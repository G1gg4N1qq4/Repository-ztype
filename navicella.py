import pygame
import random
import math
from ammo import AMMO

class NAVICELLA:
    
    def __init__(self, screen, img,size, shape, posx ,posy, parola_agganciata = None, speed = 7, muniz =[], bloccato = False, punteggio_round = [0, False]) -> None:
        
        #variabili visive
        self.screen = screen
        self.img = img
        self.size = size
        
        #variabili Cinematica
        self.posx = posx
        self.posy = posy
        # self.actposx = actposx
        # self.actposy = actposy
        self.speed = speed
        
        #variabili di funzione
        self.muniz=muniz
        self.shape = shape
        self.bloccato = bloccato
        self.parola_agganciata = parola_agganciata
        self.punteggio_round = punteggio_round
        self.shape = pygame.Rect(posx, posy, size[0], size[1])


#gestione disegno della navicella
    def draw(self, nem = None):
        self.img = pygame.transform.scale(self.img, self.size)
        
        
        if nem != None:
            if len(nem.actword) >0:
                self.mira(nem)
        self.screen.blit(self.img, (self.posx, self.posy))
        
        if nem!= None:
            lettera_presente = False
            for i, parole in enumerate(nem.actword):
                if self.parola_agganciata != None and parole.scritta[0] == nem.actword[self.parola_agganciata].scritta[0]:
                    lettera_presente = True
            
            if lettera_presente:
                for i,proiettile in enumerate(self.muniz):
                    
                    if (proiettile.centrato(nem, self.parola_agganciata)):
                        self.muniz.pop(i)
                        for i, nemico in enumerate(nem.actword):
                            
                            if nemico.scritta == nem.actword[self.parola_agganciata].scritta:
                                nem.actword[self.parola_agganciata].draw(proiettile.direction)
                    
                    if proiettile.posx > 480*2 or proiettile.posx <0 or proiettile.posy >272*2 or proiettile.posy < 0:
                        self.muniz.pop(i)
                    else:
                        proiettile.draw()


    def shot(self, nem, key):
        lettera_presente = False
        parola_trovata = False
        
        if self.parola_agganciata != None and nem.actword[self.parola_agganciata].scritta == " ":
            nem.actword.pop(self.parola_agganciata)
            self.parola_agganciata == None
            self.punteggio_round = [1, True]
            self.muniz = []
            
            return True
        
        if self.parola_agganciata != None:
            if chr(key) == nem.actword[self.parola_agganciata].scritta[0]:
                lettera_presente = True


        for i,parola in enumerate(nem.actword):
            
            if self.parola_agganciata != None and parola.scritta ==  nem.actword[self.parola_agganciata].scritta:
                parola_trovata = True
                
            if self.parola_agganciata == None and chr(key) == parola.scritta[0]:
                lettera_presente = True
                
                break
        
        
        if not parola_trovata:
            self.parola_agganciata = None
        
        if not lettera_presente and not self.parola_agganciata:
            return False
        
        if len(self.muniz) <= 25:
            ammo_img = pygame.image.load("immagini/proiettile.png")
            
            
            if self.parola_agganciata == None:
                aggancio = 0
                #converto la parola agganciata al suo index
                for i, parola in enumerate(nem.actword):

                    if parola.scritta[0] == chr(key):
                        aggancio = i 
                        # trovata = True

                        break
            else:
                if nem.actword[self.parola_agganciata].scritta[0] == chr(key):
                    aggancio = self.parola_agganciata
                    # trovata = True
                else:
                    self.punteggio_round = [1, False]
                    return False


            self.parola_agganciata = aggancio

            if nem.colpito(self.parola_agganciata, chr(key), self):
                self.parola_agganciata = None
                self.muniz = []
                self.punteggio_round = [1, True]
            else:
                self.punteggio_round = [0, False]
                pro = AMMO(self.screen,ammo_img, (50, 25), self.posx, self.posy, chr(key),
                        [self.posx - nem.actword[self.parola_agganciata].actposx, self.posy - nem.actword[self.parola_agganciata].actposy])
                
                self.muniz.append(pro)
                # shot_sound.play(0,0,0)
                # pygame.mixer.quit()
                # pygame.mixer.init()
        else:
            pass
    
    
    def big_shot(self, nemici):
        while (len(nemici.actword) > 0):
            for i,par in enumerate(nemici.actword):
                nemici.actword.pop(i)


    def mira(self, nemici):
        if self.parola_agganciata != None:
            for proiettile in self.muniz:
                proiettile.direction[0] = (proiettile.posx - nemici.actword[self.parola_agganciata].actposx)
                
                proiettile.direction[1] = (proiettile.posy - nemici.actword[self.parola_agganciata].actposy)
                proiettile.speed = [ nemici.actword[self.parola_agganciata].actposx,  
                                    nemici.actword[self.parola_agganciata].actposy ]
        
        else:
            pass
    
    
    def centrata(self, nem):
        if pygame.rect.Rect.colliderect(self.shape, nem.shape):
            # print("!")
            return True
    

    def colpita(self):
        self.bloccato = True
