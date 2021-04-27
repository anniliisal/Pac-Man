
import pygame


yellow = (0, 0, 255)
black = (0, 0, 0)


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.place = pygame.Surface([width, height])
        self.image = pygame.image.load("src/pictures/coin.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw_points(self, screen, points):
        point = Point(200, 40, 10, 10)
        points.add(point)
        point = Point(100, 40, 100, 20)
        points.add(point)
        point = Point(150, 40, 20, 10)
        points.add(point)
        points.draw(screen)

    def collect_points(self, pacman, points):
        hit_list = pygame.sprite.spritecollide(pacman, points, True)
