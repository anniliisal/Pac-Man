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
        self.ghost_1_direction = "left"
        self.ghost_2_direction = "right"

    def ghost_1_move(self, ghost, walls):
        if self.ghost_1_direction == "right":
            ghost.rect.x += 2
        if self.ghost_1_direction == "left":
            ghost.rect.x -= 2
        if self.ghost_1_direction == "up":
            ghost.rect.y -= 2
        if self.ghost_1_direction == "down":
            ghost.rect.y += 2
        collision = self.wall.collision(self, ghost, walls)
        if collision:
            if self.ghost_1_direction == "right":
                ghost.rect.x -= 2
            if self.ghost_1_direction == "left":
                ghost.rect.x += 2
            if self.ghost_1_direction == "up":
                ghost.rect.y += 2
            if self.ghost_1_direction == "down":
                ghost.rect.y -= 2
            self.ghost_1_direction = self.new_direction(self.ghost_1_direction)
            print(self.ghost_1_direction)

    def ghost_2_move(self, ghost, walls):
        if self.ghost_2_direction == "right":
            ghost.rect.x += 2
        if self.ghost_2_direction == "left":
            ghost.rect.x -= 2
        if self.ghost_2_direction == "up":
            ghost.rect.y -= 2
        if self.ghost_2_direction == "down":
            ghost.rect.y += 2
        collision = self.wall.collision(self, ghost, walls)
        if collision:
            if self.ghost_2_direction == "right":
                ghost.rect.x -= 2
            if self.ghost_2_direction == "left":
                ghost.rect.x += 2
            if self.ghost_2_direction == "up":
                ghost.rect.y += 2
            if self.ghost_2_direction == "down":
                ghost.rect.y -= 2
            self.ghost_2_direction = self.new_direction(self.ghost_2_direction)
            print(self.ghost_2_direction)

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
