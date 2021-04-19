import pygame

from game import *

purple = (169, 0, 255)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y,  width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

   
    
    def draw_walls(self, screen):
        self.wall_list = pygame.sprite.Group()
        wall = Wall(0, 0, 10, 660)
        self.wall_list.add(wall)
        wall = Wall(0, 0, 890, 10)
        self.wall_list.add(wall)
        wall = Wall(0, 650, 890, 60)
        self.wall_list.add(wall)
        wall = Wall(880, 0, 10, 890)
        self.wall_list.add(wall)
        self.wall_list.draw(screen)

        
        
        return











