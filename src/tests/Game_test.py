import unittest
from game import Game
from pacman import Pacman
from walls import Wall
from points import Point
from ghost import Ghosts
import pygame

class TestGame(unittest.TestCase):
    def setUp(self):
        self.point = Point
        self.wall = Wall
        self.ghosts = Ghosts
        self.move_down = False
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.pacman_start = True
        self.width = 890
        self.height = 660
        self.x = 100
        self.y = 100
        self.new_x = 0
        self.new_y = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-Man")
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pacman_group = pygame.sprite.GroupSingle()
        self.points = pygame.sprite.Group()
        self.ghosts_list = pygame.sprite.Group()
        self.ghosts = Ghosts(1, 500, 210)
        self.ghost_1 = Ghosts(1, 775, 40)
        self.ghost_2 = Ghosts(2, 500, 210)
        self.ghosts_list.add(self.ghost_1)
        self.ghosts_list.add(self.ghost_2)
        self.ghost_1_direction = "left"
        self.ghost_2_direction = "right"
        self.pacman = Pacman(self.x, self.y, self.move_left,
                             self.move_down, self.move_up)
        self.wall = Wall(self.x, self.y, self.width, self.height)
        self.wall.draw_walls(self.screen, self.walls)
        self.point = Point(self.x, self.y)
        self.points = self.point.draw_points(self.screen, self.points)
        self.point_count = 0
        self.game = Game()

    def test_set_direction_left(self):
        self.game.pacman_set_direction_left()
        self.assertEqual(self.move_left, True)

    def test_set_direction_right(self):
        self.game.pacman_set_direction_right()
        self.assertEqual(self.move_right, True)

    def test_set_direction_up(self):
        self.game.pacman_set_direction_up()
        self.assertEqual(self.move_up, True)

    def test_set_direction_down(self):
        find = self.game.pacman_set_direction_down()
        self.assertEqual(self.move_down, True)

    def test_point_collect(self):
        hit = self.point.collect_points(self.pacman, self.points)
        self.assertEqual(hit, 0)

    def test_pacman_start_screen(self):
        self.pacman_start = True
        self.pacman = self.game.pacman_start_screen()
        x = 100
        y = 100
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_pacman_move(self):
        self.move_right = True
        self.pacman = self.game.pacman_move()
        x = 102
        y = 100
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_pacman_move_left(self):
        self.move_left = True
        new_x = 0
        new_y = 2
        x = 100
        y = 98
        self.pacman = self.game.pacman_move(new_x, new_y)
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_pacman_move_up(self):
        self.move_up = True
        x = 100
        y = 98
        self.game.pacman_set_direction_up()
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_pacman_move_down(self):
        self.move_down = True
        x = 100
        y = 102
        self.pacman = self.game.pacman_move(new_x, new_y)
        self.assertEqual(self.x, x)
        self.assertEqual(self.y, y)

    def test_collision_right(self):
        self.move_right = True
        self.pacman = self.game.pacman_move()
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 102
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_collision_left(self):
        self.move_left = True
        self.pacman = self.game.pacman_move(self)
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 98
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_collision_up(self):
        self.move_up = True
        new_x = 0
        new_y = -2
        self.game.pacman_move(new_x, new_y)
        self.game.update_place()
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 100
            y = 98
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_collision_down(self):
        self.move_down = True
        self.pacman = self.game.pacman_move(self)
        if self.collision:
            x = 100
            y = 100
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)
        if self.collision is False:
            x = 100
            y = 102
            self.assertEqual(self.x, x)
            self.assertEqual(self.y, y)

    def test_ghost_2_move(self):
        x = 502
        y = 210
        self.ghosts.ghost_move(self.ghost_2, self.ghost_2_direction, self.walls)
        self.assertEqual(self.ghost_2.rect.x, x)
        self.assertEqual(self.ghost_2.rect.y, y)

    def test_ghost_1_move(self):
        x = 773
        y = 40
        self.ghosts.ghost_move(self.ghost_1, self.ghost_1_direction, self.walls)
        self.assertEqual(self.ghost_1.rect.x, x)
        self.assertEqual(self.ghost_1.rect.y, y)

    def test_ghost_1_collision(self):
        collision = self.wall.collision(self.ghost_1, self.walls)
        self.assertEqual(collision, False)

    def test_ghost_2_collision(self):
        collision = self.wall.collision(self.ghost_2, self.walls)
        self.assertEqual(collision, False)

    def test_ghost_collision(self):
        collision = self.ghosts.ghost_collision(self.pacman, self.ghosts_list)
        self.assertEqual(collision, False)

    def test_wall_collision(self):
        collision = self.wall.collision(self.pacman, self.walls)
        self.assertEqual(collision, False)

    def test_wall_collision(self):
        collision = self.wall.collision(self.pacman, self.walls)
        self.assertNotEqual(collision, True)
    

    def test_pacman_set_direction_down(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_down = True
        if self.move_down:
            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.new_x = 0
            self.new_y = 2
            self.game.pacman_move(self.new_x, self.new_y)
            x = 100
            y = 102
            self.assertEqual(self.game.x, x)
            self.assertEqual(self.game.y, y)
