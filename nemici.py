import pygame,sys

from pygame.locals import *
window_size = (480*2, 272*2)
import random

pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(),int(window_size[1]), bold = False, italic = True)

class NEMICI:
    def __init__(self, screen, size , counter = 0, parole = None, actword = None) -> None:
        
        self.screen = screen
        self.counter = counter
        self.size = size
        
        # if parole == None or type(parole) != list:
        self.parole = ['primavera', 'estate', 'autunno', 'inverno']
        # else:
        #     self.parole = parole
        if actword == None or type(actword) != list:
            self.actword = []
        else:
            self.actword = actword
        
    
    def aggiungi_parola(self):
        # print(len(self.parole))
        # print(self.counter)
        if self.counter <= len(self.parole):
            # print(self.counter)
            # for i in range(self.counter):
                
            self.actword.append(parola(self.screen,random.choice(self.parole), random.randint(0,window_size[0]), 
                                    random.randint(0,100)))
            for i,parol in enumerate(self.actword):
                while self.actword[-1].scritta == parol.scritta and i != len(self.actword)-1:
                    self.actword[-1].scritta = random.choice(self.parole)
                        
            self.counter +=1
                        # print(self.parole)
                        
                        
    def draw(self, proiettile = None):
        
        # print(len(self.actword))
        for parol in self.actword:
            if parol.actposy > window_size[1]:
                for elem in self.actword:
                    if elem.scritta == parol.scritta:
                        self.actword.remove(elem)
                        self.counter -= 1

                # print(parol.posy)
                
                
        if proiettile == None:
            for parol in self.actword:
                if parol.posy > window_size[1]:
                    for elem in self.actword:
                        if elem.scritta == parol.scritta:
                            self.actword.remove(elem)
                            self.counter -= 1
                    # print(parol.posy)
                else: 
                    parol.draw()
                    # print(parol.scritta)
                    img = font.render(parol.scritta, True, (200,200,200), None)
                    img = pygame.transform.scale(img,(self.size[0]*2, self.size[1]*3))
                    self.screen.blit(img,(parol.actposx, parol.actposy))
        else:
            for parol in self.actword:

                img = font.render(parol.scritta, True, (200,200,200), None)
                img = pygame.transform.scale(img,self.size)
                self.screen.blit(img,(parol.actposx, parol.actposy))
                        
    
    def colpito(self,i, key):
        if len(self.actword[i].scritta) <= 1:
            self.actword.pop(i)
            self.counter -=1
        else:
            if key == self.actword[i].scritta[0]:
                self.actword[i].scritta = self.actword[i].scritta[1:]
            

class parola:
    def __init__(self, screen, scritta, posx, posy, shape = pygame.rect.Rect(0, 0, window_size[0]/30, window_size[1]/40),
                 speed = 0.3) -> None:
        
        #variabili display
        self.screen = screen
        self.scritta = scritta
        self.shape = shape
        #variabili cinematica
        self.posx = posx
        self.posy = posy
        self.actposx = posx
        self.actposy = posy
        self.speed = speed
        
        
    def move(self, extspeed = None):
        #extspeed è la velocità del proiettile
        if extspeed == None:
            self.actposx = self.posx
            self.actposy = self.actposy + self.speed
            
        else:
            
            self.posx = self.actposx - extspeed[0]/5
            self.posy = self.actposy - extspeed[1]/5
            velocità_movimento = 5
            cont = 0
            
            if self.actposx < self.posx :
                while self.actposx != self.posx and cont != velocità_movimento:
                    self.actposx = self.actposx + 1
                    cont += 1
            elif self.actposx > self.posx:
                while self.actposx != self.posx and cont != velocità_movimento:
                    self.actposx = self.actposx - 1
                    cont += 1
            
            cont = 0
            if self.actposy < self.posy:
                while self.actposy != self.posy and cont != velocità_movimento:
                    self.actposy = self.actposy + 1
                    cont += 1
            elif self.actposy > self.posy:
                while self.actposy != self.posy and cont != velocità_movimento:
                    self.actposy = self.actposy - 1
                    cont += 1
        self.shape = pygame.rect.Rect(self.actposx, self.actposy, window_size[0]/30, window_size[1]/40)
        
    def draw(self, extspeed = None):
        # print(extspeed)
        self.move(extspeed)
        
        