import pygame,sys

from pygame.locals import *
window_size = (480*2, 272*2)
import random

pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(),int(window_size[1]), bold = True, italic = False)

class NEMICI:
    def __init__(self, screen, size , counter = 0, parole = None, actword = None) -> None:
        
        self.screen = screen
        self.counter = counter
        self.size = size
        
        # if parole == None or type(parole) != list:
        self.parole = ['Primavera', 'Estate', 'Autunno', 'Inverno']
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
            print(self.counter)
            # for i in range(self.counter):
                
            self.actword.append(parola(self.screen,random.choice(self.parole), random.randint(0,window_size[0]), 
                                    random.randint(0,100)))
            for i,parol in enumerate(self.actword):
                while self.actword[-1].scritta == parol.scritta and i != len(self.actword)-1:
                    self.actword[-1].scritta = random.choice(self.parole)
                        
            self.counter +=1
                        # print(self.parole)
                        
                        
    def draw(self):
        # print(len(self.actword))
        for parol in self.actword:
            if parol.posy > window_size[1]:
                for elem in self.actword:
                    if elem.scritta == parol.scritta:
                        self.actword.remove(elem)
                        self.counter -= 1
                # print(parol.posy)
            else: 
                parol.draw((0, 0))
                # print(parol.scritta)
                img = font.render(parol.scritta, True, (200,200,200), None)
                img = pygame.transform.scale(img,self.size)
                self.screen.blit(img,(parol.posx, parol.posy))
                
    
    def colpito(self,i):
        self.actword.pop(i)
        self.counter -=1

class parola:
    def __init__(self, screen, scritta, posx, posy, shape = pygame.rect.Rect(0, 0, 50, 50),
                 speed = 0.3) -> None:
        
        #variabili display
        self.screen = screen
        self.scritta = scritta
        self.shape = shape
        #variabili cinematica
        self.posx = posx
        self.posy = posy
        self.speed = speed
        
        
    def move(self, extspeed):
        #extspeed è la velocità del proiettile
        self.posx = self.posx - extspeed[0]
        self.posy = self.posy + self.speed - extspeed[1]
        self.shape = pygame.rect.Rect(self.posx, self.posy, 50, 50)
        
    def draw(self, extspeed):
        self.move(extspeed)
        
        