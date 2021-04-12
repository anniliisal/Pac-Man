import pygame

from game import *


class Pacman:
    
    def __init__(self):
        pygame.init()
        self.step = False
        self.load_pacman()
        

    def load_pacman(self):
        self.pacman = pygame.image.load("/Users/anni-liisalaaksonen/ot-harjoitustyo_oikea/ot-harjoitustyo-2/src/pacman3.png")
        return self.pacman

        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    step = True
                    Game.move_left(self, step)
                if event.key == pygame.K_RIGHT:
                    step = True
                    Game.move_right(self, step)
                if event.key == pygame.K_UP:
                    step = True
                    Game.move_up(self, step)
                if event.key == pygame.K_DOWN:
                    step = True
                    Game.move_down(self, step)
 
            if event.type == pygame.KEYUP: 
 
                if event.key == pygame.K_LEFT:
                    step = False
                    Game.move_left(self, step)
                if event.key == pygame.K_RIGHT:
                    step = False
                    Game.move_right(self, step)
                if event.key == pygame.K_UP:
                    step = False
                    Game.move_up(self, step)
                if event.key == pygame.K_DOWN:
                    step = False
                    Game.move_down(self, step)

            if event.type == pygame.QUIT:
                exit()
        


 