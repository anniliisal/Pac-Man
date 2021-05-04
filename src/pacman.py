
import pygame


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, left, down, up):
        """class creates single sprite pacman

        Args:
            y (y coordinate for pacman)
            x (x coordinate for pacman)
            left (rotates image to left if True)
            down (rotates image to down if True)
            up (rotates image to up if True)
        """
        super().__init__()
        self.image = pygame.image.load("src/pictures/pacman4png.png")
        if up is True:
            self.image = pygame.transform.rotate(self.image, 90)
        if left is True:
            self.image = pygame.transform.flip(self.image, True, False)
        if down is True:
            self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
