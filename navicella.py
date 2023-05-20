import pygame
import random
import math
from ammo import AMMO

class NAVICELLA:
    
    def __init__(self, screen, img,size, shape, posx ,posy, actposx=480, actposy=272*2, speed = 7, muniz =[], bloccato = False) -> None:
        
        #variabili visive
        self.screen = screen
        self.img = img
        self.size = size
        
        #variabili Cinematica
        self.posx = posx
        self.posy = posy
        self.actposx = actposx
        self.actposy = actposy
        self.speed = speed
        
        #variabili di funzione
        self.muniz=muniz
        self.shape = shape
        self.bloccato = bloccato
        
    def move(self):
        cont = 0
        if self.actposx < self.posx:
            while self.actposx != self.posx and cont != self.speed:
                self.actposx = self.actposx + 1
                cont += 1
        elif self.actposx > self.posx:
            while self.actposx != self.posx and cont != self.speed:
                self.actposx = self.actposx - 1
                cont += 1
        
        cont = 0
        if self.actposy < self.posy:
            while self.actposy != self.posy and cont != self.speed:
                self.actposy = self.actposy + 1
                cont += 1
        elif self.actposy > self.posy:
            while self.actposy != self.posy and cont != self.speed:
                self.actposy = self.actposy - 1
                cont += 1
            
        self.shape = pygame.rect.Rect(self.actposx - self.size[0]/2, self.actposy - self.size[1]/2, 
                                        self.size[0], self.size[1])
        # print(self.actposx, self.actposy)
        
    def draw(self, nem):
        self.img = pygame.transform.scale(self.img, self.size)
        
        self.move()
        if len(nem.actword) >0:
            self.mira(nem)
        self.screen.blit(self.img, (self.actposx, self.actposy))
        for i,proiettile in enumerate(self.muniz):
            # ammo_img = pygame.image.load("immagini/navicella.png")
            # pro = AMMO(self.screen,ammo_img, (10, 5), self.actposx, self.actposy)
            # pro.draw()
            if pygame.Rect.collidepoint(nem.actword[proiettile.parola_agganciata].shape, proiettile.posx,proiettile.posy):
                self.muniz.pop(i)
                for i, nemico in enumerate(nem.actword):
                    if nemico.scritta == nem.actword[proiettile.parola_agganciata].scritta:
                        nem.colpito(i)
            if proiettile.posx > 480*2 or proiettile.posx <0 or proiettile.posy >272*2 or proiettile.posy < 0:
                self.muniz.pop(i)
            else:
                proiettile.draw()
        
    def shot(self, nem):
        if len(self.muniz) <= 25:

            ammo_img = pygame.image.load("immagini/proiettile.png")
            
            quale = random.choice(nem.actword)
            aggancio = 0
            for i, parola in enumerate(nem.actword):

                if parola.scritta == quale.scritta:
                    aggancio = i - 1 
                    break
            
            pro = AMMO(self.screen,ammo_img, (50, 25), self.actposx, self.actposy, aggancio, [self.actposx, self.actposy])
            self.muniz.append(pro)
        else:
            pass
    
    
    def mira(self, nemici):
        for proiettile in self.muniz:
            if proiettile.posx < nemici.actword[proiettile.parola_agganciata].posx:
                proiettile.direction[0] = (nemici.actword[proiettile.parola_agganciata].posx - proiettile.posx)
            else:
                proiettile.direction[0] = (proiettile.posx - nemici.actword[proiettile.parola_agganciata].posx)
            
            if proiettile.posy < nemici.actword[proiettile.parola_agganciata].posy :
                proiettile.direction[1] = (nemici.actword[proiettile.parola_agganciata].posy - proiettile.posy)
            else:
                proiettile.direction[1] = (proiettile.posy - nemici.actword[proiettile.parola_agganciata].posy)
                
            # proiettile.ruota(nemici.actword[proiettile.parola_agganciata])
        else:
            pass
            
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