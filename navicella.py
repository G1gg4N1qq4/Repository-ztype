import pygame

class Navicella:
    def __init__(self, screen, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(275, 550, size[0], size[1])
        self.image = pygame.image.load('immagini/navicella.png')
        self.image = pygame.transform.scale(self.image, size)
    
    def draw(self):
        self.screen.blit(self.image, self.rect)