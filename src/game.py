
import pygame

from pacman import Pacman

 
        
        
class Game:
    
    def __init__(self):
        
        self.screen = pygame.display.set_mode((840, 450))
        self.play()
        

    def play(self):
        self.draw_screen()
        Pacman.move(self)

    def draw_screen(self):
        Pacman.pacman = pygame.image.load("/Users/anni-liisalaaksonen/ot-harjoitustyo/ot-harjoitustyo-3/src/pacman3.png")
        Pacman.pacman_x = 100
        Pacman.pacman_y = 100
        self.screen.fill((0, 0, 0))
        self.screen.blit(Pacman.pacman, (Pacman.pacman_x, Pacman.pacman_y))
        pygame.display.flip()


if __name__=="__main__":
    Game()

    