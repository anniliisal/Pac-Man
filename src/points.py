
import pygame


class Point(pygame.sprite.Sprite):
    def __init__(self, y, x):
        """class creates points and checks for collision between pacman and points

        Args:
            y (y coordinate for point)
            x (x coordinate for point)

        """
        super().__init__()
        self.place = pygame.Surface([10, 10])
        self.image = pygame.image.load("src/pictures/coin2.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw_points(self, points):
        """creates points coordinates and adds them to the points sprite group

        Args:
            points (sprite group-list where to store points)

        Returns:
            points: [sprite group-list where the points are stored]
        """
        point_list = [[50, 40], [50, 120], [50, 200],
                      [50, 280], [50, 360],
                      [140, 40], [140, 200],
                      [140, 280], [140, 360], [140, 435],
                      [140, 505], [140, 590], [140, 680],
                      [140, 760], [140, 840], [220, 840],
                      [50, 505], [50, 590], [50, 680],
                      [50, 760], [380, 120], [300, 840],
                      [220, 40], [300, 40], [380, 40],
                      [460, 40], [530, 40], [220, 120],
                      [300, 120], [380, 120], [460, 120],
                      [220, 840], [300, 840], [380, 840],
                      [460, 840], [530, 840], [50, 840],
                      [220, 760], [300, 760], [380, 760],
                      [460, 760], [530, 760], [600, 40],
                      [600, 120], [600, 200], [600, 280],
                      [600, 360], [600, 505], [600, 590],
                      [600, 680], [600, 760], [600, 840],
                      [500, 680], [500, 590], [500, 505],
                      [500, 435], [500, 360], [500, 280],
                      [500, 200], [420, 680], [420, 590],
                      [420, 505], [420, 435], [420, 360],
                      [420, 280], [420, 200], [220, 200],
                      [220, 280], [220, 360], [220, 435],
                      [220, 505], [220, 590], [220, 680],
                      [290, 240], [290, 320], [290, 400],
                      [290, 480], [290, 560], [290, 560],
                      [350, 240], [350, 320], [350, 400],
                      [350, 480], [350, 560], [350, 560],
                      [290, 640], [350, 640], [530, 120]
                      ]
        for point in point_list:
            point = Point(point[0], point[1])
            points.add(point)
        return points

    def collect_points(self, pacman, points):
        """tests if there is a collision between pacman and points

        Args:
            pacman (single sprite)
            points (sprite group)

        Returns:
            1, if pacman collides with one or more than one points
            0, if there is no collision
        """
        hit_list = pygame.sprite.spritecollide(pacman, points, True)
        if len(hit_list) == 1:
            return 1
        if len(hit_list) == 2:
            return 2
