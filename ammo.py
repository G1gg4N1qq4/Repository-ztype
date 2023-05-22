import math
import pygame 

from pygame.locals import*

class AMMO:
    def __init__(self, screen, img, size, posx, posy, key, direction = [0, 10]) -> None:
        self.screen = screen
        self.img = img
        self.size = size
        self.posx = posx
        self.posy = posy

        self.direction = direction
        # self.parola_agganciata = parola_agganciata
        self.key = key
        
    def move(self):
        self.posy -= self.direction[1]/10
        self.posx -= self.direction[0]/10
        
    # rotazione di prova
    def ruota(self, nemico):
        ipo = []
        # if nemico.posx > self.posx:
        ipo = [(nemico.posx - self.posx)]
        # else:
        #     ipo = [math.sqrt((self.posx - nemico.posx))]
            
        # if nemico.posy > self.posy:
        ipo.append((nemico.posy - self.posy))
        # else:
        #     ipo.append(math.sqrt((self.posy - nemico.posy)))
            
        ipodef = math.sqrt(ipo[0]**2 + ipo[1]**2)
        print(ipodef, ipo)
        angle = math.acos(ipo[0]/ipodef)
        
        self.img = pygame.transform.rotate(self.img, angle)
        print(angle)
        
        
    def centrato(self, nem, parola_agganciata):
        # if(nem.actword[self.parola_agganciata].actposx - self.posx) <= nem.size[0]:
        #     if(nem.actword[self.parola_agganciata].actposx - self.posx) >= -nem.size[0]:
        #         return True 
        
        if(nem.actword[parola_agganciata].actposy - self.posy) >= - nem.size[1]:
            if(nem.actword[parola_agganciata].actposy - self.posy) <= nem.size[1]:
                return True
            
            
            
        return False
        
    def draw(self):
        self.img = pygame.transform.scale(self.img, self.size)
        self.move()
        # self.img = pygame.transform.rotate(self.img, )
        self.screen.blit(self.img, (self.posx, self.posy))
        pass