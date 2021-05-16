
import pygame

purple = (169, 0, 255)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """class creates walls and checks for collision between pacman, ghosts and walls 

        Args:
            x (x coordinate for wall)
            y (y coordinate for wall)
            width (wall's width)
            height (wall's height)

        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw_walls(self, screen, walls):
        walls_list = [[0, 0, 10, 660],
                      [0, 0, 890, 10],
                      [880, 0, 10, 660],
                      [0, 650, 890, 10],
                      [435, 0, 10, 100],
                      [160, 90, 190, 10],
                      [535, 90, 190, 10],
                      [160, 560, 190, 10],
                      [545, 560, 190, 10],
                      [435, 560, 10, 120],
                      [0, 320, 80, 10],
                      [810, 320, 80, 10],
                      [80, 90, 10, 370],
                      [180, 190, 10, 270],
                      [700, 190, 10, 270],
                      [800, 90, 10, 380],
                      [535, 180, 175, 10],
                      [180, 180, 370, 10],
                      [180, 460, 150, 10],
                      [435, 380, 10, 90],
                      [545, 460, 165, 10],
                      [280, 260, 10, 120],
                      [600, 260, 10, 120],
                      [280, 380, 330, 10],
                      [280, 260, 100, 10],
                      [510, 260, 100, 10],
                      [800, 540, 10, 120],
                      [80, 540, 10, 120],
                      ]
        for wall in walls_list:
            wall = Wall(wall[0], wall[1], wall[2], wall[3])
            walls.add(wall)
        walls.draw(screen)

    def collision(self, sprite, walls):
        hit_list = pygame.sprite.spritecollide(sprite, walls, False)
        if len(hit_list) >= 1:
            return True
        if len(hit_list) < 1:
            return False
