import pygame

from walls import Wall
from pacman import Pacman
from points import Point
from ghosts import Ghosts


class Game:
    def __init__(self):
        """class makes pacman move and draws the screen"""
        self.move_down = False
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self._pacman_start = True
        self.first_game_screen = True
        self.game_over_screen = False
        self.game_win_screen = False
        self.game_over = False
        self.game_win = False
        self.play_again = None
        self.width = 890
        self.height = 660
        self.x = 100
        self.y = 100
        self._new_x = 0
        self._new_y = 0
        self._collision = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pac-Man")
        self.walls = pygame.sprite.Group()
        self.pacman_group = pygame.sprite.GroupSingle()
        self.points = pygame.sprite.Group()
        self.ghosts_list = pygame.sprite.Group()
        self.pacman = Pacman(self.x, self.y, self.move_left,
                             self.move_down, self.move_up)
        self.ghosts = Ghosts(1, 500, 210)
        self.ghost_1 = Ghosts(1, 775, 40)
        self.ghost_2 = Ghosts(2, 500, 210)
        self.ghost_3 = Ghosts(3, 100, 460)
        self._ghost_collision = False
        self.ghosts_list.add(self.ghost_1, self.ghost_2, self.ghost_3)
        self.ghosts_list.add(self.ghost_2)
        self.ghost_1_direction = "left"
        self.ghost_2_direction = "right"
        self.ghost_3_direction = "down"
        self.wall = Wall(self.x, self.y, self.width, self.height)
        self.wall.draw_walls(self.screen, self.walls)
        self.point = Point(self.x, self.y)
        self.points = self.point.draw_points(self.points)
        self.point_count = 0
        pygame.init()  # pylint: disable=(no-member)

    def draw_screen(self):
        """draws the screen with points, walls and updated score and place for pacman and ghosts"""
        self.screen.fill((0, 0, 0))
        self._get_points()
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(
            "Score: " + str(self.point_count), True, (18, 247, 110))
        self.screen.blit(text, (775, 20))
        self.points.draw(self.screen)
        self.pacman_group.draw(self.screen)
        self.walls.draw(self.screen)
        self.ghosts_list.draw(self.screen)

    def _get_points(self):
        """Uses point_collect method from Point class to test if pacman collides with points.
        Saves the score if pacman collects points and sets the self.game_win True."""
        hit = self.point.collect_points(self.pacman, self.points)
        if hit == 1:
            self.point_count += 1
        if hit == 2:
            self.point_count += 2
        if self.point_count == 87:
            self.game_win = True

    def update_place(self):
        """updates place for pacman and ghosts"""
        if self._pacman_start:
            self.pacman_start_screen()
        if self._pacman_start is False:
            self.pacman_move()
            self._ghost_collision = self.ghosts.ghost_collision(
                self.pacman, self.ghosts_list)
            if self._ghost_collision is True:
                self.game_over = True
            self.ghost_1_direction = self.ghosts.ghost_move(
                self.ghost_1, self.ghost_1_direction, self.walls)
            self.ghost_2_direction = self.ghosts.ghost_move(
                self.ghost_2, self.ghost_2_direction, self.walls)
            self.ghost_3_direction = self.ghosts.ghost_move(
                self.ghost_3, self.ghost_3_direction, self.walls)
            self.pacman_group.add(self.pacman)

    def pacman_start_screen(self):
        """creates a new start view. Different views for first game, game over and winning."""
        if self.first_game_screen:
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
            self.pacman_group.add(self.pacman)
            start = pygame.image.load("src/pictures/start.png")
            self.screen.blit(start, (205, 170))
        if self.game_over_screen:
            game_over = pygame.image.load("src/pictures/Game_over.png")
            self.screen.blit(game_over, (205, 170))
            self.screen.blit(self.game_over_score, (457, 273))
        if self.game_win_screen:
            win = pygame.image.load("src/pictures/you_won.png")
            self.screen.blit(win, (205, 170))

    def save_game_over_score(self, score):
        """saves the score for new start view"""
        font = pygame.font.SysFont("Jellee-Roman", 48)
        self.game_over_score = font.render(str(score), True, (18, 247, 95))

    def pacman_move(self):
        """updates new coordinates for pacman and uses collision method from Wall class
           to check for collision
        Args:
            new_x (adds new coordinates)
            new_y (adds new coordinates)
        """
        self.x += self._new_x
        self.y += self._new_y
        self.pacman = Pacman(
            self.x, self.y, False, False, True)
        self._collision = self.wall.collision(self.pacman, self.walls)
        if self._collision:
            self.x -= self._new_x
            self.y -= self._new_y
            self.pacman = Pacman(
                self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.pacman = Pacman(
            self.x, self.y, self.move_left, self.move_down, self.move_up)
        self.pacman_group.add(self.pacman)

    def move(self):
        """Functions for different keys. Uses different move methods depending on 
           which key is pressed"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # pylint: disable=(no-member)
                if event.key == pygame.K_LEFT:  # pylint: disable=(no-member)
                    self._pacman_set_direction_left()
                if event.key == pygame.K_RIGHT:  # pylint: disable=(no-member)
                    self._pacman_set_direction_right()  # pylint: disable=(no-member)
                if event.key == pygame.K_UP:  # pylint: disable=(no-member)
                    self._pacman_set_direction_up()
                if event.key == pygame.K_DOWN:  # pylint: disable=(no-member)
                    self._pacman_set_direction_down()
                if event.key == pygame.K_RETURN:  # pylint: disable=(no-member)
                    self._pacman_start = False
            if event.type == pygame.QUIT:  # pylint: disable=(no-member)
                exit()

    def _pacman_set_direction_right(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_right = True
        if self.move_right:
            self.move_left = False
            self.move_up = False
            self.move_down = False
            self._new_x = 1
            self._new_y = 0

    def _pacman_set_direction_left(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_left = True
        if self.move_left:
            self.move_right = False
            self.move_up = False
            self.move_down = False
            self._new_x = -1
            self._new_y = 0

    def _pacman_set_direction_up(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_up = True
        if self.move_up:
            self.move_left = False
            self.move_right = False
            self.move_down = False
            self._new_x = 0
            self._new_y = -1

    def _pacman_set_direction_down(self):
        """Sets the moving direction. The current direction is True, others are False"""
        self.move_down = True
        if self.move_down:
            self.move_left = False
            self.move_right = False
            self.move_up = False
            self._new_x = 0
            self._new_y = 1
