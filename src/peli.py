import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

pacman = pygame.image.load("/Users/anni-liisalaaksonen/ot-harjoitustyo/ot-harjoitustyo/src/pacman2.png")

naytto.fill((0, 0, 0))
naytto.blit(pacman, (100, 50))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()