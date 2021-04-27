import unittest
from game import Game
from pacman import Pacman
from walls import Wall

class TestGame(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")


    def test_move_left(self):
        find = self.pacman_move_left()
        self.assertEqual(self.move_left, True) 
        
        
    def test_move_right(self):
        find = self.pacman_move_right()
        self.assertEqual(self.move_right, True)

    def test_move_up(self):
        find = self.pacman_move_up()
        self.assertEqual(self.move_up, True)

    def test_move_down(self):
        find = self.pacman_move_down()
        self.assertEqual(self.move_down, True)

    def pacman_move_left(self):
        self.move_left = True
        if self.move_left:
            self.pacman_start = False
            self.move_right = False
            self.move_up = False
            self.move_down = False

    def pacman_move_right(self):
        self.move_right = True
        if self.move_right:
            self.pacman_start = False
            self.move_left = False
            self.move_up = False
            self.move_down = False


    def pacman_move_up(self):
        self.move_up = True
        if self.move_up:
            self.pacman_start = False
            self.move_left = False
            self.move_right = False
            self.move_down = False


    def pacman_move_down(self):
        self.move_down = True
        if self.move_down:
            self.pacman_start = False
            self.move_left = False
            self.move_right = False
            self.move_up = False

    #def assert_coordinates_equal(self, self.pacman, self.x, self.y):
     #   self.assertEqual(self.pacman, self.x)
     #   self.assertEqual(self.pacman, self.y)


   # def update_place(self):
    #    if self.pacman_start:
     #       self.pacman = Pacman(
      #          self.x, self.y, self.move_left, self.move_down, self.move_up)
       #     self.pacman_group.add(self.pacman)
        #    return self.pacman_start


    #def test_update_place(self):
     #   find = self.update_place
        
      #  self.assertEqual(self.pacman, self.x)
       # self.assertEqual(self.pacman, self.y)