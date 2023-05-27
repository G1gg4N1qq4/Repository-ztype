import pygame,sys

from pygame.locals import *
window_size = (480*2, 272*2)
import random

pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(),int(window_size[1]), bold = False, italic = True)

class NEMICI:
    def __init__(self, screen, size , direction, counter = 0, actword = None, maxnem = 5) -> None:
        
        self.screen = screen
        self.counter = counter
        self.size = size
        self.direction = direction
        self.maxnem = maxnem
        # if parole == None or type(parole) != list:
        self.parole = []
        # else:
        #     self.parole = parole
        if actword == None or type(actword) != list:
            self.actword = []
        else:
            self.actword = actword
        
    
    def aggiungi_parola(self):
        #Generazione nemici, quindi scelta delle parole 
        while self.counter <= self.maxnem:
            posx = random.randint(0,window_size[0])
            posy = random.randint(0,100)
            word = random.choice(self.parole)
            for p in self.actword:
                while word[0] == p.scritta[0]:
                    word = random.choice(self.parole)
            
            self.actword.append(parola(self.screen,word, posx, 
                                    posy , self.direction[0], self.direction[1]))
            
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
                    img = pygame.transform.scale(img,(self.size[0]*2, self.size[1]*3))
                    self.screen.blit(img,(parol.actposx, parol.actposy))
        else:
            for parol in self.actword:

                img = font.render(parol.scritta, True, (200,200,200), None)
                img = pygame.transform.scale(img,self.size)
                self.screen.blit(img,(parol.actposx, parol.actposy))


# DA SISTEMARE IL PUNTEGGIO QUA SOTTO E NELLA LINEA 144 DI NAVICELLA
    def colpito(self,i, key , nav):
        if len(self.actword[i].scritta) <= 1:
            self.actword.pop(i)
            # self.parole.pop(i)
            # self.counter -=1
            nav.parola_agganciata = None
            nav.punteggio_round = [0, False]
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
        # self.size = size
        # self.shape = pygame.rect.Rect(posx, posy, size[0], size[1]/40)
        #variabili cinematica
        self.posx = posx
        self.posy = posy
        self.actposx = actposx
        self.actposy = actposy
        self.speed = speed
        
        
    def move(self, extspeed = None):
        #extspeed è la velocità del proiettile
        if extspeed != None:
            self.actposx = self.actposx - extspeed[0]/5
            self.actposy = self.actposy - extspeed[1]/5
            # self.actposx = self.posx
            # self.actposy = self.actposy + self.speed
        else:
            # cont = 0
            if self.actposx < self.posx:
                if self.actposx != self.posx :
                    self.actposx = self.actposx + 0.2
                    # cont += 0.2
            elif self.actposx > self.posx:
                if self.actposx != self.posx :
                    self.actposx = self.actposx - 0.2
                    # cont += 0.2
            
            # cont = 0
            if self.actposy < self.posy:
                if self.actposy != self.posy :
                    self.actposy = self.actposy + (0.2*self.speed)
                    # cont += 0.2
            elif self.actposy > self.posy:
                if self.actposy != self.posy :
                    self.actposy = self.actposy - (0.2 *self.speed)
                    # cont += 0.2

        # self.shape = pygame.rect.Rect(self.actposx , self.actposy, self.size[0], self.size[1]/40 )

    def draw(self, extspeed = None):
        self.move(extspeed)