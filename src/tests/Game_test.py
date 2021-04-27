import unittest
from src.game import Game
from src.pacman import Pacman
from src.walls import Wall

class TestGame(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_draw_screen(self):
        self.wall.draw_walls(self.screen, self.walls)
        find = self.walls
        self.assertEqual(find, self.walls)

