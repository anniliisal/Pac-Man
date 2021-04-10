import pygame


class Pacman:
    
    def __init__(self, pacman: pygame.Surface, pacman_x: int, pacman_y: int):
        pygame.init()
        self.pacman = pacman
        self.pacman_x = pacman_x
        self.pacman_y = pacman_y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    

    def move(self):
        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left = True

                    if event.key == pygame.K_RIGHT:
                        self.right = True
                    
                    if event.key == pygame.K_UP:
                        self.up = True
 
                    if event.key == pygame.K_DOWN:
                        self.down = True
 
                if event.type == pygame.KEYUP: 
 
                    if event.key == pygame.K_LEFT:
                        self.left = False
                    if event.key == pygame.K_RIGHT:
                        self.right = False
                    if event.key == pygame.K_UP:
                        self.up = False
                    if event.key == pygame.K_DOWN:
                        self.down = False

                if event.type == pygame.QUIT:
                    exit()
                
           
 
            if self.left:
                self.pacman_x -= 4
 
            if self.up:
                self.pacman_y -= 4
 
            if self.down:
                self.pacman_y += 4

if __name__=="__main__":
    Pacman()
 