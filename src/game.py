import pygame

from walls import Wall
from pacman import Pacman
from points import Point

class Game:
    def __init__(self):

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
        self.point = Point(self.x, self.y, self.width, self.height)
        pygame.init()# pylint: disable=(no-member)
        self.play()

    def play(self):
        while True:
            self.draw_screen()
            self.update_place()
            self.move()
            self.point.collect_points(self.pacman, self.points)
           # self.collision = self.wall.collision(
               # self.pacman, self.walls, self.move_down, self.move_up, 
               # self.move_right, self.move_left)
            pygame.display.flip()

    def draw_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        self.wall.draw_walls(self.screen, self.walls)
        self.point.draw_points(self.screen, self.points)
        self.all_sprites.add(self.walls)

    def update_place(self):
        if self.pacman_start:
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.pacman_group.add(self.pacman)

        if self.move_right: #and self.collision != "right":
            self.x += 3
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.pacman_group.add(self.pacman)
        if self.move_left: #and self.collision != "left":
            self.x -= 3
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.pacman_group.add(self.pacman)
        if self.move_down: #and self.collision != "down":
            self.y += 3
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.pacman_group.add(self.pacman)
        if self.move_up: #and self.collision != "up":
            self.y -= 3
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.pacman_group.add(self.pacman)
        self.pacman_group.draw(self.screen)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # pylint: disable=(no-member)
                if event.key == pygame.K_LEFT:  # pylint: disable=(no-member)
                    self.pacman_move_left()
                if event.key == pygame.K_RIGHT:  # pylint: disable=(no-member)
                    self.pacman_move_right()  # pylint: disable=(no-member)
                if event.key == pygame.K_UP:# pylint: disable=(no-member)
                    self.pacman_move_up()
                if event.key == pygame.K_DOWN:  # pylint: disable=(no-member)
                    self.pacman_move_down()
            if event.type == pygame.KEYUP:# pylint: disable=(no-member)
                if event.key == pygame.K_LEFT:  # pylint: disable=(no-member)
                    self.pacman_move_left()
                if event.key == pygame.K_RIGHT:  # pylint: disable=(no-member)
                    self.pacman_move_right()
                if event.key == pygame.K_UP:  # pylint: disable=(no-member)
                    self.pacman_move_up()
                if event.key == pygame.K_DOWN:  # pylint: disable=(no-member)
                    self.pacman_move_down()
            if event.type == pygame.QUIT:# pylint: disable=(no-member)
                exit()

    def pacman_move_right(self):
        self.move_right = True
        if self.move_right:
            self.pacman_start = False
            self.move_left = False
            self.move_up = False
            self.move_down = False
        

    def pacman_move_left(self):
        self.move_left = True
        if self.move_left:
            self.pacman_start = False
            self.move_right = False
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


if __name__ == "__main__":
    game = Game()
