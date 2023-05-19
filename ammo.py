
import pygame 

from pygame.locals import*

class AMMO:
    def __init__(self, screen, img, size, posx, posy, speed = 10) -> None:
        self.screen = screen
        self.img = img
        self.size = size
        self.posx = posx
        self.posy = posy
        self.speed = speed
        
    def move(self):
        self.posy -= self.speed
        
        
    def draw(self):
        self.img = pygame.transform.scale(self.img, self.size)
        self.move()
        self.screen.blit(self.img, (self.posx, self.posy))
        pass