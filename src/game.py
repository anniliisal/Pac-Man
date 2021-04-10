
import pygame

from pacman import Pacman
        
class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((840, 450))
        self.pacman = Pacman()
        self.pacman_x = 100
        self.pacman_y = 100
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.move_up = False
        self.play()

        

    def play(self):
        while True:
            self.draw_screen()
            Pacman.move(self)


    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.pacman, (self.pacman_x, self.pacman_y))
        pygame.display.flip()

    def move_right(self, step: bool):
        if step == False:
            self.pacman_x += 0
        if step == True:
            self.pacman_x += 4

    def move_left(self, step: bool):
        if step == False:
            self.pacman_x += 0
        if step == True:
            self.pacman_x -= 4

    def move_up(self, step: bool):
        if step == False:
            self.pacman_y += 0
        if step == True:
            self.pacman_y -= 4

    def move_down(self, step: bool):
        if step == False:
            self.pacman_y += 0
        if step == True:
            self.pacman_y += 4


if __name__=="__main__":
    Game()

    