
import pygame
import random
from walls import Wall



class Ghosts(pygame.sprite.Sprite):
    def __init__(self,number, x, y):
        super().__init__()
        if number is 1:
            self.image = pygame.image.load("src/pictures/ghost1.2png.png")
        if number is 2:
            self.image = pygame.image.load("src/pictures/ghost2.1png.png")
        self.rect =  self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.wall = Wall


    #def get_ghost(self, screen, ghosts):
    #    self.ghosts_list = [[1,500, 210], [2, 300, 300]]
     #   for ghost in self.ghosts_list:
      #      ghost = Ghosts(ghost[0], ghost[1], ghost[2])
       #     ghosts.add(ghost)
        #return ghosts






    






