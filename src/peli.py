import pygame


class Game:
    pygame.init()

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.height = 480
        self.widht = 640
        self.pacman = Pacman()
        self.move = Pacman()
        self.play()
        



    def play(self):
        self.draw_screen()
        self.move()



    def draw_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.pacman,(self.pacman_x, self.pacman_y))

        pygame.display.flip


    

class Pacman:

    def __init__(self):

        self.pacman = pygame.image.load("pacman.png")
        self.pacman_x = 100
        self.pacman_y = 100
       



    def move(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()



        
    




if __name__=="__main__":
    Pacman()