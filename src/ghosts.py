import random
import pygame
from walls import Wall


class Ghosts(pygame.sprite.Sprite):
    def __init__(self, number, x, y):
        """class creates ghost sprite

        Args:
            number (defines which picture is loaded)
            x (x coordinate for ghost)
            y (y coordinate for ghost)
        """
        super().__init__()
        if number == 1:
            self.image = pygame.image.load("src/pictures/ghost1.2png.png")
        if number == 2:
            self.image = pygame.image.load("src/pictures/ghost2.1.png")
        if number == 3:
            self.image = pygame.image.load("src/pictures/ghost3.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.wall = Wall
        self._collision = False

    def ghost_move(self, ghost, direction, walls):
        """defines new coordinates for ghost

        Args:
            ghost (ghost sprite)
            direction (ghost's current direction)
            walls (self.walls)

        Returns:
            direction if ghost don't hit walls, new_direction 
            if self.collision = True
        """
        if direction == "right":
            ghost.rect.x += 1
        if direction == "left":
            ghost.rect.x -= 1
        if direction == "up":
            ghost.rect.y -= 1
        if direction == "down":
            ghost.rect.y += 1
        self._collision = self.wall.collision(self, ghost, walls)
        if self._collision:
            if direction == "right":
                ghost.rect.x -= 1
            if direction == "left":
                ghost.rect.x += 1
            if direction == "up":
                ghost.rect.y += 1
            if direction == "down":
                ghost.rect.y -= 1
            new_direction = self._new_direction(direction)
            return new_direction
        return direction

    def _new_direction(self, old_direction):
        """creates new random direction for ghost

        Args:
            old_direction (old direction)

        Returns:
            direction (new direction for ghost)
        """
        direction_list = ["up", "down", "left", "right"]
        direction_list.remove(old_direction)
        direction = random.choice(direction_list)
        return direction

    def ghost_collision(self, pacman, ghosts):
        """Test if there is collision between pacman and ghosts

        Args:
            pacman (sprite)
            ghosts (sprite list)

        Returns:
            True (if collision)
            False (if no collision)
        """
        hit_list = pygame.sprite.spritecollide(pacman, ghosts, False)
        if len(hit_list) >= 1:
            return True
        if len(hit_list) < 1:
            return False
