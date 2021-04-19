
import pygame
from game import * 
class Pacman:
    
    def __init__(self):
        self.step = False


    
        

    def load_pacman1(self):
        self.pacman = pygame.image.load("src/pacman1.png")
        
        return self.pacman

    def load_pacman2(self):
        self.pacman2 = pygame.image.load("src/pacman2.png")
        
        return self.pacman2

        
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    step = True
                    Game.move_left(self, step)
                if event.key == pygame.K_RIGHT:
                    step = True
                    Game.move_right(self, step)
                if event.key == pygame.K_UP:
                    step = True
                    Game.move_up(self, step)
                if event.key == pygame.K_DOWN:
                    step = True
                    Game.move_down(self, step)
 
            if event.type == pygame.KEYUP: 
 
                if event.key == pygame.K_LEFT:
                    step = False
                    Game.move_left(self, step)
                if event.key == pygame.K_RIGHT:
                    step = False
                    Game.move_right(self, step)
                if event.key == pygame.K_UP:
                    step = False
                    Game.move_up(self, step)
                if event.key == pygame.K_DOWN:
                    step = False
                    Game.move_down(self, step)

            if event.type == pygame.QUIT:
                exit()


    def pacman_place(self):
        pass
        
        if self.pacman_start:
            self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))
        if self.pacman_face_right:
            self.screen.blit(self.pacman1, (self.pacman_x, self.pacman_y))
        if self.pacman_face_left:
            self.screen.blit(self.pacman_left, (self.pacman_x, self.pacman_y))
        if self.pacman_face_up:
            self.screen.blit(self.pacman_up, (self.pacman_x, self.pacman_y))
        if self.pacman_face_down:
            self.screen.blit(self.pacman_down, (self.pacman_x, self.pacman_y))
    

        if self.move_right == True:
            self.pacman_x += 4

        if self.move_left == True:
            self.pacman_x -= 4
        
        if self.move_up == True:
            self.pacman_y -= 4

        if self.move_down == True:
            self.pacman_y += 4


        



        


 