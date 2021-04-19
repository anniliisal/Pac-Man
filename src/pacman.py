
import pygame


class Pacman:

    def __init__(self):
        self.step = False
        

    def load_pacman1(self):
        self.pacman = pygame.image.load("src/pacman1.png")

        return self.pacman

    def load_pacman2(self):
        self.pacman2 = pygame.image.load("src/pacman2.png")

        return self.pacman2
