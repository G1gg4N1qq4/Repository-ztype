import pygame

#gestione font
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font("fonts/techno_hideo_bold.ttf", 50)
font3 = pygame.font.Font("fonts/techno_hideo_bold.ttf", 130)
pygame.init()

class GRIGLIA:
    
    def __init__(self, screen, size) -> None:
        self.screen = screen
        self.size = size
        self.scores = []
    
    def local_device_score(self, player, score):
        self.scores = []
        with open("SCORE.txt", "r", encoding = "utf-8") as file:
            i = 0
            for line in file:
                line = line.strip().split(": ")
                self.scores.append([line[0], int(line[1])])
                i+=1


        self.scores.append([player, score])
        
        self.scores.sort(key = lambda x: -x[1])
        with open("SCORE.txt", "w", encoding = "utf-8") as file:
            for player_score in self.scores:
                file.write(f"{player_score[0]}: {player_score[1]}\n")


#disegnamo la nostra griglia di score finale
    def draw(self):
        posy = 10
        posx = self.size[0]/2 
        back = pygame.Surface(self.size, pygame.SRCALPHA)
        pygame.draw.rect(back, (0, 0, 0, 100), pygame.Rect(0, 0, self.size[0], self.size[1]))
        pygame.draw.rect(back, (0,0,0), pygame.Rect(0, 0, self.size[0], self.size[1]), 3)
        
        self.screen.blit(back,(posx, posy))
        
        for i, players in enumerate(self.scores):
            if i > 17:
                break
            
            posy+=3
            img = font.render(f"{players[0]}:   {players[1]}", True, (255,255,255), None)
            img = pygame.transform.scale(img,(img.get_width(), img.get_height()))
            
            if i != 1:
                self.screen.blit(img,(posx + 6, posy + 9))
            else:
                self.screen.blit(img, (posx + 6, posy + 6))
            
            posy+=img.get_height()
            rect = pygame.Surface((self.size[0], 3))
            pygame.draw.rect(back,(0,0,0), pygame.Rect(0, posy, rect.get_width(), rect.get_height()))
            
        self.screen.blit(back,(posx, 10))