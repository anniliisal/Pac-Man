import unittest
from game import *
from pacman import *

class TestGame(unittest.TestCase):
      def setUp(self):
          print("Set up goes here")
     
      
      def test_pacman_load_pacman1(self):
          self.pacman1 = Pacman.load_pacman1(self)
          find = self.pacman1
          self.assertEqual(find, self.pacman1)
     
      def test_pacman_load_pacman2(self):
          self.pacman2 = Pacman.load_pacman2(self)
          find = self.pacman2
          self.assertEqual(find, self.pacman2)
      
      def test_draw_screen(self):
          self.screen = self.screen_measures()
          find = self.screen
          self.assertEqual(find, self.screen)
