
import pygame


yellow = (0, 0, 255)
black = (0, 0, 0)


class Point(pygame.sprite.Sprite):
    def __init__(self,y, x, width, height):
        super().__init__()
        self.place = pygame.Surface([width, height])
        self.image = pygame.image.load("src/pictures/coin.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        

    def draw_points(self, screen, points):
        point_list = [ [50, 100, 10, 10], 
                       [50, 150, 100, 20],
                       [50, 200, 20, 10],
                       [100, 100, 10, 10]
                        ]
        for point in point_list:
            point = Point(point[0], point[1], point[2], point[3])
            points.add(point)
        return points
       

    def collect_points(self, pacman, points):
        hit_list = pygame.sprite.spritecollide(pacman, points, True)
        if len(hit_list) >= 1:
            return 1
