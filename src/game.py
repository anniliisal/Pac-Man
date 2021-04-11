
import pygame

from pacman import *
        
class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((490, 680))
        
        
        self.pacman_x = 100
        self.pacman_y = 100
        self.move_down = False
        self.move_up = False
        self.move_right = False
        self.move_left = False
       

        self.play()

        

    def play(self):

        while True:
            self.draw_screen()
            Pacman.move(self)
            pygame.display.flip()
            


    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        self.pacman = Pacman.load_pacman(self)
        self.screen.blit(self.pacman, (self.pacman_x, self.pacman_y))

        if self.move_right == True:
            self.pacman_x += 1

        if self.move_left == True:
            self.pacman_x -= 1
        
        if self.move_up == True:
            self.pacman_y -= 1

        if self.move_down == True:
            self.pacman_y += 1

        if self.pacman_x + self.pacman.get_width() >= 490:
            self.pacman_x -= 1
        if self.pacman_x + self.pacman.get_width() <= 55:
            self.pacman_x += 1
        if self.pacman_y + self.pacman.get_width() >= 680:
            self.pacman_y -= 1
        if self.pacman_y + self.pacman.get_width() <= 60:
            self.pacman_y += 1
        
        


    def move_right(self, step: bool):
        if step == True:
            self.move_right = True
        if step == False:
            self.move_right = False

    def move_left(self, step: bool):
        if step == True:
            self.move_left = True
        if step == False:
            self.move_left= False

    def move_up(self, step: bool):
        if step == True:
            self.move_up = True
        if step == False:
            self.move_up = False

    def move_down(self, step: bool):
        if step == True:
            self.move_down = True
        if step == False:
            self.move_down = False
        


if __name__=="__main__":
    game = Game()

    