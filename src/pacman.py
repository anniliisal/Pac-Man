
import pygame


class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, left, down, up):
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
