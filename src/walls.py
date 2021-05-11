
import pygame

purple = (169, 0, 255)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        """class creates walls and checks for collision between pacman and walls

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
                      [10, 650, 890, 10],
                      [435, 0, 10, 100],
                      [80, 90, 250, 10],
                      [545, 90, 250, 10],
                      [80, 550, 270, 10],
                      [545, 550, 270, 10],
                      [435, 550, 10, 100],
                      [0, 320, 80, 10],
                      [810, 320, 80, 10],
                      [80, 200, 10, 270],
                      [180, 200, 10, 270],
                      [700, 200, 10, 270],
                      [800, 200, 10, 270],
                      [535, 190, 175, 10],
                      [180, 190, 370, 10],
                      [180, 460, 165, 10],
                      [545, 460, 155, 10],
                      [280, 260, 10, 120],
                      [600, 260, 10, 120],
                      [280, 380, 330, 10],
                      [280, 260, 100, 10],
                      [280, 260, 100, 10],
                      [510, 260, 100, 10]
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
