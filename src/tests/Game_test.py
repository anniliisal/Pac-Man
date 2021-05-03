import unittest
from game import Game
from pacman import Pacman
from walls import Wall
from points import Point
import pygame


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game
        self.point = Point
        self.wall = Wall
        self.move_down = False
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.pacman_start = True
        self.width = 890
        self.height = 660
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pacman_group = pygame.sprite.GroupSingle()
        self.points = pygame.sprite.Group()
        self.x = 100
        self.y = 100
        self.collision = None
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.pacman = Pacman(self.x, self.y, self.move_left,
                             self.move_down, self.move_up)
        self.wall = Wall(self.x, self.y, self.width, self.height)
        self.point = Point(self.x, self.y)
        self.point_count = 0
        self.points = self.point.draw_points(self.screen, self.points)

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

    def test_point_collect(self):

        hit = self.point.collect_points(self.pacman, self.points)
        self.assertEqual(hit, 1)

    def test_update_place_start(self):
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        x = 100
        y = 100
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_update_place_right(self):
        self.move_right = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        x = 105
        y = 100
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_update_place_left(self):
        self.move_left = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        x = 95
        y = 100
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_update_place_up(self):
        self.move_up = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        x = 100
        y = 95
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_update_place_down(self):
        self.move_down = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        x = 100
        y = 105
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_collision_right(self):
        self.move_right = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.collision = self.wall.collision(self.pacman, self.walls)
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 105
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_collision_left(self):
        self.move_left = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.collision = self.wall.collision(self.pacman, self.walls)
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 95
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_collision_up(self):
        self.move_up = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.collision = self.wall.collision(self.pacman, self.walls)
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 100
            y = 95
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_collision_down(self):
        self.move_down = True
        self.game.update_place(self)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.collision = self.wall.collision(self.pacman, self.walls)
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 100
            y = 105
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
