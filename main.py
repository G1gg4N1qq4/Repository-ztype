import os
os.system('cls')

import random
import pygame, sys
from pygame.locals import *
from nemici import Nemici
from navicella import Navicella


pygame.init()

window_size = (600, 700)
screen = pygame.display.set_mode(window_size, 0, 32)

pygame.display.set_caption('Zty.pe')

clock = pygame.time.Clock()

navicella = Navicella(screen, (50, 50))
BIANCO = (255, 255, 255)

sfondo_immagine = pygame.image.load('immagini/sfondo.png')
sfondo_immagine = pygame.transform.scale(sfondo_immagine, window_size) 
# -----------------------------------

parole = [
"Ciao", "Buongiorno", "Grazie", "Prego", "Amore", "Sole", "Luna", "Gatto", "Cane", "Casa", "Albero",
"Libro", "Scuola", "Studente", "Computer", "Gioco", "Musica", "Arte", "Ristorante", "Cibo", "Acqua",
"Montagna", "Mare", "Città", "Strada", "Parco", "Amico", "Famiglia", "Felicità", "Vacanza", "Calcio",
"Pallacanestro", "Film", "Teatro", "Musica", "Lingua", "Natura", "Viaggio", "Auto", "Moto", "Bicicletta",
"Orologio", "Giardino", "Festa", "Sorpresa", "Nuvola", "Stelle", "Sogno", "Felicità", "Sorriso"
]
font = pygame.font.Font(None, 36)
def disegna_testo( testo, posizione):
        testo_renderizzato = font.render(testo, True, BIANCO)
        screen.blit(testo_renderizzato, posizione)

punteggio = 0
parola_digitata = 0

while True:
    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # keys = pygame.key.get_pressed()

    screen.blit(sfondo_immagine, (0,0))

    disegna_testo(f"Parola: {parola_digitata}", (10, 10))
    disegna_testo(f"Punteggio: {punteggio}", (10, 50))
    navicella.draw()
    # nemici.draw()
    pygame.display.flip()
    clock.tick(60)

