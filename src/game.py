
import pygame

from pacman import *
from walls import *


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

        self.play()

    def play(self):

        while True:
            self.draw_screen()
            Pacman.move(self)
            pygame.display.flip()

    def screen_measures(self):
        self.screen = pygame.display.set_mode((890, 660))
        return self.screen

    def draw_screen(self):
        self.screen = self.screen_measures()
        self.screen.fill((0, 0, 0))
        Wall.draw_walls(self, self.screen)
        self.pacman1 = Pacman.load_pacman1(self)
        self.pacman2 = Pacman.load_pacman2(self)
        if self.pacman_start:
            self.pacman1.blit(self.pacman1, (self.pacman_x, self.pacman_y))
        if self.pacman_face_right:
            self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))
        if self.pacman_face_left:
            self.screen.blit(self.pacman_left, (self.pacman_x, self.pacman_y))
        if self.pacman_face_up:
            self.screen.blit(self.pacman_up, (self.pacman_x, self.pacman_y))
        if self.pacman_face_down:
            self.screen.blit(self.pacman_down, (self.pacman_x, self.pacman_y))

        if self.move_right == True:
            self.pacman_x += 4

        if self.move_left == True:
            self.pacman_x -= 4

        if self.move_up == True:
            self.pacman_y -= 4

        if self.move_down == True:
            self.pacman_y += 4

    def move_right(self, step: bool):
        if step == True:
            self.move_right = True
            if self.move_right:
                self.pacman_start = False
                self.pacman_face_right = True
                self.pacman_face_left = False
                self.pacman_face_up = False
                self.pacman_face_down = False
                self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))

        if step == False:
            self.move_right = False

    def move_left(self, step: bool):
        if step == True:
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

        if step == False:
            self.move_left = False

    def move_up(self, step: bool):
        if step == True:
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

        if step == False:
            self.move_up = False

    def move_down(self, step: bool):
        if step == True:
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

        if step == False:
            self.move_down = False


if __name__ == "__main__":
    game = Game()
