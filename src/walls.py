
import pygame

purple = (169, 0, 255)
box_size = 10


class Wall:
    def __init__(self, x, y, lenght, direction):
        self.rects = []
        if direction == 1:
            for i in range(lenght):
                rect = pygame.Rect(x+i*box_size, y, box_size, box_size)
                self.rects.append(rect)

        if direction == 0:
            for i in range(lenght):
                rect = pygame.Rect(x, y+i*box_size, box_size, box_size)
                self.rects.append(rect)

    def draw_walls(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, purple, rect)

    def collision(self, pacman_rect):
        for rect in self.rects:
            if pygame.Rect.colliderect(pacman_rect, rect):
                return True
        return False
