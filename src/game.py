import pygame

from walls import Wall
from pacman import Pacman


class Game:

    def __init__(self):
        pygame.init()

        self.pacman_x = 100
        self.pacman_y = 100
        self.move_down = False
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.pacman_start = True
        self.pacman_face_left = False
        self.pacman_face_right = False
        self.pacman_face_up = False
        self.pacman_face_down = False
        self.screen = pygame.display.set_mode((890, 660))
        self.pacman1 = Pacman.load_pacman1(self)
        self.pacman2 = Pacman.load_pacman2(self)

        self.play()

    def play(self):

        while True:
            self.draw_screen()
            self.move()
            pygame.display.flip()


    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        Wall.draw_walls(self, self.screen)
        if self.pacman_start:
            self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))
        if self.pacman_face_right:
            self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))
        if self.pacman_face_left:
            self.screen.blit(self.pacman_left, (self.pacman_x, self.pacman_y))
        if self.pacman_face_up:
            self.screen.blit(self.pacman_up, (self.pacman_x, self.pacman_y))
        if self.pacman_face_down:
            self.screen.blit(self.pacman_down, (self.pacman_x, self.pacman_y))

        if self.move_right is True:
            self.pacman_x += 1

        if self.move_left is True:
            self.pacman_x -= 1

        if self.move_up is True:
            self.pacman_y -= 1

        if self.move_down is True:
            self.pacman_y += 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:# pylint: disable=(no-member)
                    step = True
                    self.pacman_move_left(step)
                if event.key == pygame.K_RIGHT:# pylint: disable=(no-member)
                    step = True
                    self.pacman_move_right(step)# pylint: disable=(no-member)
                if event.key == pygame.K_UP:
                    step = True
                    self.pacman_move_up(step)
                if event.key == pygame.K_DOWN:# pylint: disable=(no-member)
                    step = True
                    self.pacman_move_down(step)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:# pylint: disable=(no-member)
                    step = False
                    self.pacman_move_left(step)
                if event.key == pygame.K_RIGHT:# pylint: disable=(no-member)
                    step = False
                    self.pacman_move_right(step)
                if event.key == pygame.K_UP:# pylint: disable=(no-member)
                    step = False
                    self.pacman_move_up(step)
                if event.key == pygame.K_DOWN:# pylint: disable=(no-member)
                    step = False
                    self.pacman_move_down(step)

            if event.type == pygame.QUIT:
                exit()

    def pacman_move_right(self, step: bool):
        if step is True:
            self.move_right = True
            if self.move_right:
                self.pacman_start = False
                self.pacman_face_right = True
                self.pacman_face_left = False
                self.pacman_face_up = False
                self.pacman_face_down = False
                self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))

        if step is False:
            self.move_right = False

    def pacman_move_left(self, step: bool):
        if step is True:
            self.move_left = True
            if self.move_left:
                self.pacman_start = False
                self.pacman_face_right = False
                self.pacman_face_up = False
                self.pacman_face_down = False
                self.pacman_face_left = True
                self.pacman_left = pygame.transform.flip(
                    self.pacman1, True, False)
                self.screen.blit(self.pacman_left,
                                 (self.pacman_x, self.pacman_y))

        if step is False:
            self.move_left = False

    def pacman_move_up(self, step: bool):
        if step is True:
            self.move_up = True
            if self.move_up:
                self.pacman_start = False
                self.pacman_face_right = False
                self.pacman_face_left = False
                self.pacman_face_down = False
                self.pacman_face_up = True
                self.pacman_up = self.pacman2
                self.screen.blit(
                    self.pacman_up, (self.pacman_x, self.pacman_y))

        if step is False:
            self.move_up = False

    def pacman_move_down(self, step: bool):
        if step is True:
            self.move_down = True
            if self.move_down:
                self.pacman_start = False
                self.pacman_face_right = False
                self.pacman_face_left = False
                self.pacman_face_up = False
                self.pacman_face_down = True
                self.pacman_down = pygame.transform.flip(
                    self.pacman2, False, True)
                self.screen.blit(self.pacman_down,
                                 (self.pacman_x, self.pacman_y))

        if step is False:
            self.move_down = False


if __name__ == "__main__":
    game = Game()
