import unittest
import random
from game import Game
from pacman import Pacman
from walls import Wall
from points import Point
from ghosts import Ghosts
from main import Main

import pygame


class TestGame(unittest.TestCase):
    def setUp(self):
        self.point = Point
        self.wall = Wall
        self.ghosts = Ghosts
        self.game = Game()

    def test_set_direction_left(self):
        self.game._pacman_set_direction_left()
        self.assertEqual(self.game.move_left, True)
        self.assertEqual(self.game._new_x, -1)
        self.assertEqual(self.game._new_y, 0)

    def test_set_direction_right(self):
        self.game._pacman_set_direction_right()
        self.assertEqual(self.game.move_right, True)
        self.assertEqual(self.game._new_x, 1)
        self.assertEqual(self.game._new_y, 0)

    def test_set_direction_up(self):
        self.game._pacman_set_direction_up()
        self.assertEqual(self.game.move_up, True)
        self.assertEqual(self.game._new_x, 0)
        self.assertEqual(self.game._new_y, -1)

    def test_set_direction_down(self):
        self.game._pacman_set_direction_down()
        self.assertEqual(self.game.move_down, True)
        self.assertEqual(self.game._new_x, 0)
        self.assertEqual(self.game._new_y, 1)

    def test_pacman_move_down(self):
        self.game._new_x = 0
        self.game._new_y = 1
        self.game.pacman_move()
        x = 100
        y = 101
        self.assertEqual(self.game.x, x)
        self.assertEqual(self.game.y, y)

    def test_pacman_collision(self):
        self.game._new_x = 0
        self.game._new_y = -1
        self.game.pacman_move()
        if self.game._collision:
            x = 100
            y = 100
            self.assertEqual(self.game.x, x)
            self.assertEqual(self.game.y, y)

    def test_pacman_move_left(self):
        self.game._new_x = -1
        self.game._new_y = 0
        self.game.pacman_move()
        x = 99
        y = 100
        self.assertEqual(self.game.x, x)
        self.assertEqual(self.game.y, y)

    def test_pacman_move_right(self):
        self.game._new_x = 1
        self.game._new_y = 0
        self.game.pacman_move()
        x = 101
        y = 100
        self.assertEqual(self.game.x, x)
        self.assertEqual(self.game.y, y)

    def test_pacman_start_screen(self):
        self.game.pacman_start = True
        self.game.pacman_start_screen()
        x = 100
        y = 100
        self.assertEqual(self.game.x, x)
        self.assertEqual(self.game.y, y)

    def test_point_collect_points(self):
        self.game.point_count = 86
        test_pacman = Pacman(40, 460, False, False, True)
        hit = self.point.collect_points(self, test_pacman, self.game.points)
        self.game.point_count += hit
        self.game._get_points()
        self.assertEqual(self.game.game_win, True)

    def test_game_point_collect(self):
        test_pacman = Pacman(40, 460, True, False, False)
        hit = self.point.collect_points(self, test_pacman, self.game.points)
        self.assertEqual(hit, 1)

    def test_ghost_move_right(self):
        x = 501
        y = 210
        self.ghosts.ghost_move(self, self.game.ghost_2,
                               self.game.ghost_2_direction, self.game.walls)
        self.assertEqual(self.game.ghost_2.rect.x, x)
        self.assertEqual(self.game.ghost_2.rect.y, y)

    def test_ghost_move_left(self):
        x = 774
        y = 40
        self.ghosts.ghost_move(self, self.game.ghost_1,
                               self.game.ghost_1_direction, self.game.walls)
        self.assertEqual(self.game.ghost_1.rect.x, x)
        self.assertEqual(self.game.ghost_1.rect.y, y)

    def test_ghost_move_down(self):
        x = 100
        y = 461
        self.ghosts.ghost_move(self, self.game.ghost_3,
                               self.game.ghost_3_direction, self.game.walls)
        self.assertEqual(self.game.ghost_3.rect.x, x)
        self.assertEqual(self.game.ghost_3.rect.y, y)

    def test_ghost_move_up(self):
        test_ghost = Ghosts(2, 100, 460)
        test_ghost_direction = "up"
        x = 100
        y = 459
        self.ghosts.ghost_move(
            self, test_ghost, test_ghost_direction, self.game.walls)
        self.assertEqual(test_ghost.rect.x, x)
        self.assertEqual(test_ghost.rect.y, y)

    def test_ghost_and_walls_collision(self):
        test_ghost = Ghosts(1, 180, 190)
        test_ghost_direction = "right"
        new_direction = self.ghosts.ghost_move(
            self, test_ghost, test_ghost_direction, self.game.walls)
        collision = self.wall.collision(self, test_ghost, self.game.walls)
        self.assertEqual(collision, True)
        self.assertNotEqual(new_direction, test_ghost_direction)

    def test_pacman_and_ghosts_collision(self):
        test_pacman1 = Pacman(100, 461, False, True, False)
        self.game.ghost_collision = self.ghosts.ghost_collision(
            self, test_pacman1, self.game.ghosts_list)
        self.assertEqual(self.game.ghost_collision, True)
        self.game.ghost_collision = self.ghosts.ghost_collision(self,
                                                                self.game.pacman, self.game.ghosts_list)
        self.assertEqual(self.game.ghost_collision, False)

    def _new_direction(self, old_direction):
        direction_list = ["up", "down", "left", "right"]
        direction_list.remove(old_direction)
        direction = random.choice(direction_list)
        return direction

    def test_ghost_new_direction(self):
        direction = self.game.ghost_1_direction
        new_direction = self.ghosts._new_direction(self, direction)
        self.assertNotEqual(direction, new_direction)

    def test_pacman_and_wall_collision_False(self):
        collision = self.wall.collision(
            self, self.game.pacman, self.game.walls)
        self.assertEqual(collision, False)

    def test_pacman_and_wall_collision_True(self):
        test_pacman = Pacman(180, 190, True, False, False)
        collision = self.wall.collision(self, test_pacman, self.game.walls)
        self.assertEqual(collision, True)
