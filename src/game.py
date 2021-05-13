import pygame

from walls import Wall
from pacman import Pacman
from points import Point
from ghost import Ghosts

class Game:
    def __init__(self):
        """class makes pacman move and draws the screen"""
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
        self.collision = False
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
        pygame.init()  # pylint: disable=(no-member)

    def draw_screen(self):
        """draws the screen with points, walls and updated score and place for pacman
        """
        self.screen.fill((0, 0, 0))
        hit = self.point.collect_points(self.pacman, self.points)
        if hit == 1:
            self.point_count += 1
        self.font = pygame.font.SysFont("Arial", 24)
        text = self.font.render(
            "Score: " + str(self.point_count), True, (18, 247, 110))
        self.screen.blit(text, (775, 20))
        self.points.draw(self.screen)
        self.pacman_group.draw(self.screen)
        self.walls.draw(self.screen)
        self.ghosts_list.draw(self.screen)

    def update_place(self):
        """updates place for pacman and ghosts"""
        if self.pacman_start:
            self.pacman_start_screen()
        if self.pacman_start is False:
            self.pacman_move(self.new_x, self.new_y)
            ghost_collision = self.ghosts.ghost_collision(
                self.pacman, self.ghosts_list)
            if ghost_collision is True:
                print("joo")
            self.ghost_1_direction = self.ghosts.ghost_move(self.ghost_1, self.ghost_1_direction, self.walls)
            self.ghost_2_direction = self.ghosts.ghost_move(self.ghost_2, self.ghost_2_direction, self.walls)
            self.pacman_group.add(self.pacman)

    def pacman_start_screen(self):
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.pacman_group.add(self.pacman)
        start = pygame.image.load("src/pictures/start.png")
        self.screen.blit(start, (205, 180))

    def pacman_move(self, new_x, new_y):
        """updates new coordinates for pacman and uses collision method from Wall class
           to check for collision
        Args:
            new_x (adds new coordinates)
            new_y (adds new coordinates)
        """
        self.x += self.new_x
        self.y += self.new_y
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.collision = self.wall.collision(self.pacman, self.walls)
        if self.collision:
            self.x -= self.new_x
            self.y -= self.new_y
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.pacman_group.add(self.pacman)

    def move(self):
        """Functions for different keys. Uses different move methods depending on 
           which key is pressed"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # pylint: disable=(no-member)
                if event.key == pygame.K_LEFT:  # pylint: disable=(no-member)
                    self.pacman_set_direction_left()
                if event.key == pygame.K_RIGHT:  # pylint: disable=(no-member)
                    self.pacman_set_direction_right()  # pylint: disable=(no-member)
                if event.key == pygame.K_UP:  # pylint: disable=(no-member)
                    self.pacman_set_direction_up()
                if event.key == pygame.K_DOWN:  # pylint: disable=(no-member)
                    self.pacman_set_direction_down()
                if event.key == pygame.K_RETURN:  # pylint: disable=(no-member)
                    self.pacman_start = False
            if event.type == pygame.QUIT:  # pylint: disable=(no-member)
                exit()

    def pacman_set_direction_right(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_right = True
        if self.move_right:
            self.move_left = False
            self.move_up = False
            self.move_down = False
            self.new_x = 2
            self.new_y = 0
            self.pacman_move(self.new_x, self.new_y)

    def pacman_set_direction_left(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_left = True
        if self.move_left:
            self.move_right = False
            self.move_up = False
            self.move_down = False
            self.new_x = -2
            self.new_y = 0
            self.pacman_move(self.new_x, self.new_y)
            
    def pacman_set_direction_up(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_up = True
        if self.move_up:
            self.move_left = False
            self.move_right = False
            self.move_down = False
            self.new_x = 0
            self.new_y = -2
            self.pacman_move(self.new_x, self.new_y)

    def pacman_set_direction_down(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_down = True
        if self.move_down:
            self.move_left = False
            self.move_right = False
            self.move_up = False
            self.new_x = 0
            self.new_y = 2
            self.pacman_move(self.new_x, self.new_y)
