import pygame

class Nemici(pygame.sprite.Sprite):
    def __init__(self, parola, x, y) -> None:
        super().__init__()
        self.parola = parola
        self.image = pygame.image.load('immagini/nemico.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def discesa(self):
        self.rect.y += 0.5