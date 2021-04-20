import unittest
from src.game import Game
from src.pacman import Pacman

class TestGame(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_pacman_load_pacman(self):
        self.pacman1 = Pacman.load_pacman(self)
        find = self.pacman1
        self.assertEqual(find, self.pacman)


