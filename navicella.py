import pygame
import random
import math
from ammo import AMMO

class NAVICELLA:
    
    def __init__(self, screen, img,size, shape, posx ,posy, parola_agganciata = None, speed = 7, muniz =[], bloccato = False, punteggio_round = 0) -> None:
        
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
    # def move(self):
    #     cont = 0
    #     if self.actposx < self.posx:
    #         while self.actposx != self.posx and cont != self.speed:
    #             self.actposx = self.actposx + 1
    #             cont += 1
    #     elif self.actposx > self.posx:
    #         while self.actposx != self.posx and cont != self.speed:
    #             self.actposx = self.actposx - 1
    #             cont += 1
        
    #     cont = 0
    #     if self.actposy < self.posy:
    #         while self.actposy != self.posy and cont != self.speed:
    #             self.actposy = self.actposy + 1
    #             cont += 1
    #     elif self.actposy > self.posy:
    #         while self.actposy != self.posy and cont != self.speed:
    #             self.actposy = self.actposy - 1
    #             cont += 1
            
    #     self.shape = pygame.rect.Rect(self.actposx - self.size[0]/2, self.actposy - self.size[1]/2, 
    #                                     self.size[0], self.size[1])
    #     # print(self.actposx, self.actposy)
        
    def draw(self, nem = None):
        self.img = pygame.transform.scale(self.img, self.size)
        
        # self.move()
        if len(nem.actword) >0:
            self.mira(nem)
        self.screen.blit(self.img, (self.posx, self.posy))
        
        lettera_presente = False
        for i, parole in enumerate(nem.actword):
            if self.parola_agganciata != None and parole.scritta[0] == nem.actword[self.parola_agganciata].scritta[0]:
                lettera_presente = True
                
        if lettera_presente:
            for i,proiettile in enumerate(self.muniz):
                # ammo_img = pygame.image.load("immagini/navicella.png")
                # pro = AMMO(self.screen,ammo_img, (10, 5), self.actposx, self.actposy)
                # pro.draw()
                
                # if pygame.Rect.collidepoint(nem.actword[proiettile.parola_agganciata].shape, proiettile.posx,proiettile.posy):
                if (proiettile.centrato(nem, self.parola_agganciata)):
                    self.muniz.pop(i)
                    for i, nemico in enumerate(nem.actword):
                        # print(nem.actword[proiettile.parola_agganciata].scritta, nemico.scritta)
                        
                        if nemico.scritta == nem.actword[self.parola_agganciata].scritta:
                            
                            # nem.colpito(i, proiettile.key)
                            nem.actword[self.parola_agganciata].draw(proiettile.direction)
                if proiettile.posx > 480*2 or proiettile.posx <0 or proiettile.posy >272*2 or proiettile.posy < 0:
                    self.muniz.pop(i)
                else:
                    proiettile.draw()
        
    def shot(self, nem, key):
        lettera_presente = False
        for parola in nem.actword:
            # print(chr(key), parola.scritta[0])
            if chr(key) == parola.scritta[0]:
                lettera_presente = True
                
                break
            # self.muniz = self.muniz[0:-1]
        
        if not lettera_presente:
            self.parola_agganciata == None
            # print("!!")
            return False
        if len(self.muniz) <= 25:
            trovata = False
            ammo_img = pygame.image.load("immagini/proiettile.png")
            
            
            if self.parola_agganciata == None:
                # quale = random.choice(nem.actword)
                aggancio = 0
                #converto la parola agganciata al suo index
                for i, parola in enumerate(nem.actword):

                    if parola.scritta[0] == chr(key):
                        aggancio = i 
                        trovata = True
                        # print("!")
                        break
            else:
                if nem.actword[self.parola_agganciata].scritta[0] == chr(key):
                    aggancio = self.parola_agganciata
                    trovata = True
                    # print("!!")
            if trovata != False:
            
                self.parola_agganciata = aggancio
            else:
                return False
            # while chr(key) != quale.scritta[0]:
            #     if self.parola_agganciata == None:
            #         quale = self.parola_agganciata
            #     aggancio = 0
    
            #     for i, parola in enumerate(nem.actword):

            #         if parola.scritta[0] == chr(key):
            #             # print(parola.scritta, quale.scritta)
            #             aggancio = i 
                        
            #             break
            
            # print(chr(key), quale.scritta[0])
            if nem.colpito(self.parola_agganciata, chr(key)):
                self.parola_agganciata = None
                self.muniz = self.muniz[len(self.muniz)-1:-1:]
                self.punteggio_round +=1
            else:

                pro = AMMO(self.screen,ammo_img, (50, 25), self.posx, self.posy, chr(key),
                        [self.posx - nem.actword[self.parola_agganciata].actposx, self.posy - nem.actword[self.parola_agganciata].actposy])
                
                self.muniz.append(pro)
        else:
            pass
    
    
    def mira(self, nemici):
        if self.parola_agganciata != None:
            for proiettile in self.muniz:
                # if proiettile.posx < nemici.actword[proiettile.parola_agganciata].posx:
                #     proiettile.direction[0] = (nemici.actword[proiettile.parola_agganciata].posx - proiettile.posx)
                # else:
                proiettile.direction[0] = (proiettile.posx - nemici.actword[self.parola_agganciata].actposx)
                
                # if proiettile.posy < nemici.actword[proiettile.parola_agganciata].posy :
                #     proiettile.direction[1] = (nemici.actword[proiettile.parola_agganciata].posy - proiettile.posy)
                # else:
                proiettile.direction[1] = (proiettile.posy - nemici.actword[self.parola_agganciata].actposy)
                proiettile.speed = [ nemici.actword[self.parola_agganciata].actposx,  
                                    nemici.actword[self.parola_agganciata].actposy ]
                # proiettile.ruota(nemici.actword[proiettile.parola_agganciata])
                
            else:
                pass
        
    def centrata(self, nem):
        # if(nem.actword[self.parola_agganciata].actposx - self.posx) <= nem.size[0]:
        #     if(nem.actword[self.parola_agganciata].actposx - self.posx) >= -nem.size[0]:
        #         return True 
        
        if(nem.actposy - self.posy) >= - (self.size[1] - 10):
            if(nem.actposy - self.posy) <= (self.size[1] - 10):
                
                if(nem.actposx - self.posx) >= - (self.size[0] - 10):
                    if(nem.actposx - self.posx) <= (self.size[0] - 10):
                        return True
            
    def colpita(self):
        self.bloccato = True
        

        
# class Nemici:
#     def __init__(self, screen, pos, size) -> None:
#         self.screen = screen
#         self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
#         # self.image = pygame.image.load('immagini/nemici.png')
#         self.image = pygame.transform.scale(self.image, size)
#         self.vel = [0,0]
#         self.gravita = 0.3

#         self.moving_right = False
#         self.moving_left = False

#         self.vel_orizz = 5
#         self.falling = False
#         self.forza_jump = 10

#     def move_right(self):
#         self.moving_right = True
    
#     def stop_moving_right(self):
#         self.moving_right = False

#     def move_left(self):
#         self.moving_left = True
    
#     def stop_moving_left(self):
#         self.moving_left = False

#     def jump(self):
#         if not self.falling:
#             self.vel[1] -= self.forza_jump

#     def muovi(self):
#         # caduta
#         self.vel[1] += self.gravita
#         self.rect.bottom += self.vel[1]
#         self.falling = True

#         # collisione col pavimento
#         if self.rect.bottom > self.screen.get_height():
#             self.rect.bottom = self.screen.get_height()
#             self.vel[1] = 0
#             self.falling = False

#         # muovi orizzontale
#         if self.moving_right:
#             self.rect.right += self.vel_orizz
#             if self.rect.right > self.screen.get_width():
#                 self.rect.right = self.screen.get_width()
#         if self.moving_left:
#             self.rect.left -= self.vel_orizz
#             if self.rect.left < 0:
#                 self.rect.left = 0



#     def draw(self):
#         self.screen.blit(self.image, self.rect)