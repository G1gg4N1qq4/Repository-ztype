import pygame,sys

from pygame.locals import *
window_size = (480*2, 272*2)
import random

pygame.font.init()
font = pygame.font.Font("fonts/eElectroBox.ttf", 120)

class NEMICI:
    # inizializzazione classe NEMICI
    def __init__(self, screen, size , direction, counter = 0, actword = None, maxnem = 5) -> None:
        
        self.screen = screen
        self.counter = counter
        self.size = size
        self.direction = direction
        self.maxnem = maxnem
        self.parole = []
        
        if actword == None or type(actword) != list:
            self.actword = []
        else:
            self.actword = actword
    
    # assocazione di una parola ad un "nemico" e aggiunta dello stesso alla totalità dei nemici
    def aggiungi_parola(self):
        
        while self.counter <= self.maxnem:
            posx = random.randint(0,window_size[0])
            posy = random.randint(0,100)
            word = random.choice(self.parole)
            for p in self.actword:
                while word[0] == p.scritta[0]:
                    word = random.choice(self.parole)
                    print(p.scritta, word)
                
                while posx == p.actposx:
                    posx = random.randint(0,window_size[0])
                
                while posy == p.actposy:
                    posy = random.randint(0,100)

            if len(word) >= 5:
                speed = 0.4
            elif len(word) > 2:
                speed = 0.45
            else:
                speed = 0.6
            self.actword.append(parola(self.screen,word, posx, 
                                    posy , self.direction[0], self.direction[1], speed))
            
            for i,parol in enumerate(self.actword):
                while self.actword[-1].scritta == parol.scritta and i != len(self.actword)-1:
                    self.actword[-1].scritta = random.choice(self.parole)
                    
            self.counter +=1



    def draw(self, proiettile = None):
        
        for parol in self.actword:
            if parol.actposy > window_size[1]:
                for elem in self.actword:
                    if elem.scritta == parol.scritta:
                        self.actword.remove(elem)


        if proiettile == None:
            for parol in self.actword:
                if parol.posy > window_size[1]:
                    for elem in self.actword:
                        if elem.scritta == parol.scritta:
                            self.actword.remove(elem)
                            self.counter -= 1
                
                else: 
                    parol.draw()

                    img = font.render(parol.scritta, True, (200,200,200), None)
                    img = pygame.transform.scale(img,(img.get_width()/4, img.get_height()/4))
                    rect = pygame.Surface((img.get_width() +10, img.get_height()+ 1), pygame.SRCALPHA)
                    pygame.draw.rect(rect, (100, 0, 100, 80), pygame.Rect(0, 0, rect.get_width(), rect.get_height()))
                    self.screen.blit(rect, (parol.actposx - 5, parol.actposy - 0.5))
                    parol.shape = pygame.Rect(parol.actposx - img.get_width()/8 , parol.actposy - img.get_height()/8,
                                              img.get_width()/4, img.get_height()/4 )
                    
                    self.screen.blit(img,(parol.actposx, parol.actposy))
        else:
            for parol in self.actword:

                img = font.render(parol.scritta, True, (200,200,200, 180), None)
                img = pygame.transform.scale(img,(img.get_width()/4, img.get_height()/4))
                parol.shape = pygame.Rect(parol.actposx - img.get_width()/8 , parol.actposy - img.get_height()/8, 
                                          img.get_width()/4, img.get_height()/4 )
                self.screen.blit(img,(parol.actposx, parol.actposy))



    def colpito(self,i, key , nav):
        if len(self.actword[i].scritta) <= 1:
            self.actword.pop(i)
            nav.parola_agganciata = None
            
            return True
        else:

            if key == self.actword[i].scritta[0]:
                self.actword[i].scritta = self.actword[i].scritta[1:]
            return False


class parola:
    def __init__(self, screen, scritta, actposx, actposy, posx,posy,
                 speed = 1.5) -> None:
        
        #variabili display
        self.screen = screen
        self.scritta = scritta
        
        #variabili cinematica
        self.posx = posx
        self.posy = posy
        self.actposx = actposx
        self.actposy = actposy
        self.speed = speed
        self.shape = pygame.Rect(actposx, actposy, 0.5,0.5)
        
        
    def move(self, extspeed = None):
        #extspeed è la velocità del proiettile
        if extspeed != None:
            self.actposx = self.actposx - extspeed[0]/10
            self.actposy = self.actposy - extspeed[1]/5
            
        else:
            
            if self.actposx < self.posx:
                if self.actposx != self.posx :
                    self.actposx = self.actposx + 0.3*self.speed *window_size[0]/window_size[1]
            
            elif self.actposx > self.posx:
                if self.actposx != self.posx :
                    self.actposx = self.actposx - 0.3*self.speed *window_size[0]/window_size[1]
            
            
            if self.actposy < self.posy:
                if self.actposy != self.posy :
                    self.actposy = self.actposy + (1.3*self.speed) *window_size[1]/window_size[0] 
            
            elif self.actposy > self.posy:
                if self.actposy != self.posy :
                    self.actposy = self.actposy - (1.3 *self.speed)  *window_size[1]/window_size[0]



    def draw(self, extspeed = None):
        self.move(extspeed)
