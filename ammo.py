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
        self.shape = pygame.Rect(posx,posy,size[0], size[1])

        self.direction = direction
        # self.parola_agganciata = parola_agganciata
        self.key = key

    
    def move(self):
        self.posy -= self.direction[1]/10
        self.posx -= self.direction[0]/10
        self.shape = pygame.Rect(self.posx, self.posy, self.size[0], self.size[1])
    

    # rotazione di prova
    def ruota(self, nemico):
        ipo = []
        ipo = [(nemico.posx - self.posx)]
        
        ipo.append((nemico.posy - self.posy))
        
        ipodef = math.sqrt(ipo[0]**2 + ipo[1]**2)
        print(ipodef, ipo)
        angle = math.acos(ipo[0]/ipodef)
        
        self.img = pygame.transform.rotate(self.img, angle)
        print(angle)
    
    
    def centrato(self, nem, parola_agganciata): 
        if pygame.Rect.colliderect(self.shape, nem.actword[parola_agganciata].shape):
            # print("!!")
            return True
        return False


    def draw(self):
        self.img = pygame.transform.scale(self.img, self.size)
        self.move()
        self.screen.blit(self.img, (self.posx, self.posy))
        pass
