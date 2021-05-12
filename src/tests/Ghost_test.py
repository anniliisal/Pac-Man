import unittest
import random
from walls import Wall


class TestGhost(unittest.TestCase):
    def setUp(self):

        def __init__(self, number, x, y):
            super().__init__()
            if number == 1:
                self.image = pygame.image.load("src/pictures/ghost1.2png.png")
            if number == 2:
                self.image = pygame.image.load("src/pictures/ghost2.1.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.wall = Wall
            self.ghost_1_direction = "left"
            self.ghost_2_direction = "right"
            self.ghosts = Ghosts
            self.wall = Wall
            self.walls = pygame.sprite.Group()
            self.wall.draw_walls(self.screen, self.walls)
