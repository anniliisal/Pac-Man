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
        self.point_count = 0
        self.points = self.point.draw_points(self.screen, self.points)
        pygame.init()# pylint: disable=(no-member)
        self.play()

     
    def play(self):
        while True:
            self.draw_screen()
            self.update_place()
            self.move()
            pygame.display.flip()

    def draw_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        hit = self.point.collect_points(self.pacman, self.points)
        if hit is 1:
            self.point_count += 1
        self.font = pygame.font.SysFont("Arial", 24)
        text = self.font.render("Points: " + str(self.point_count), True, (250, 0, 0))
        self.screen.blit(text, (775,20))
        self.wall.draw_walls(self.screen, self.walls)
        self.points.draw(self.screen)        
        self.all_sprites.add(self.walls, self.points)
        self.pacman_group.draw(self.screen)

    def update_place(self):

        if self.pacman_start:
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
        if self.move_right:
            self.x += 5
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.collision = self.wall.collision(self.pacman, self.walls)
            if self.collision:
                self.x -= 5
                self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
        if self.move_left:
            self.x -= 5
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.collision = self.wall.collision(self.pacman, self.walls)
            if self.collision:
                self.x += 5
                self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
        if self.move_down:
            self.y += 5
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.collision = self.wall.collision(self.pacman, self.walls)
            if self.collision:
                self.y -= 5
                self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
        if self.move_up:
            self.y -= 5
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.collision = self.wall.collision(self.pacman, self.walls)
            if self.collision:
                self.y += 5
                self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)

        self.pacman_group.add(self.pacman)
      

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
        



