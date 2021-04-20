
import pygame


class Pacman:

    def __init__(self):
        self.step = False

    def load_pacman(self):
        self.pacman = pygame.image.load("src/pacman1.png")
        return self.pacman
