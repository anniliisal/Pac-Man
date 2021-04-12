import unittest
from game import *
from pacman import *

class TestGame(unittest.TestCase):
      def setUp(self):
          print("Set up goes here")
     
      
      def test_pacman_load_pacman(self):
          self.pacman = Pacman.load_pacman(self)
          find = self.pacman
          self.assertEqual(find, self.pacman)
