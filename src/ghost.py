import random
import pygame

from walls import Wall


class Ghosts(pygame.sprite.Sprite):
    def __init__(self, number, x, y):
        super().__init__()
        if number == 1:
            self.image = pygame.image.load("src/pictures/ghost1.2png.png")
        if number == 2:
            self.image = pygame.image.load("src/pictures/ghost2.1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.wall = Wall
        
    def ghost_move(self, ghost, direction, walls):
        if direction == "right":
            ghost.rect.x += 2
        if direction == "left":
            ghost.rect.x -= 2
        if direction == "up":
            ghost.rect.y -= 2
        if direction == "down":
            ghost.rect.y += 2
        collision = self.wall.collision(self, ghost, walls)
        if collision:
            if direction == "right":
                ghost.rect.x -= 2
            if direction == "left":
                ghost.rect.x += 2
            if direction == "up":
                ghost.rect.y += 2
            if direction == "down":
                ghost.rect.y -= 2
            new_direction = self.new_direction(direction)
            return new_direction
        return direction

    def new_direction(self, old_direction):
        direction_list = ["up", "down", "left", "right"]
        direction_list.remove(old_direction)
        direction = random.choice(direction_list)
        return direction

    def ghost_collision(self, pacman, ghosts):
        hit_list = pygame.sprite.spritecollide(pacman, ghosts, False)
        if len(hit_list) >= 1:
            return True
        if len(hit_list) < 1:
            return False
