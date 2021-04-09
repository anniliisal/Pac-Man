import pygame




class Pacman:

    def __init__(self, pacman: pygame.Surface, pacman_x: int, pacman_y: int):
        self.pacman = pacman
        self.pacman_x = pacman_x
        self.pacman_y = pacman_y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    

    def move(self):
        while True:
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
        if self.right:
            self.pacman_x += 4
 
        if self.left:
            self.pacman_x -= 4
 
        if self.up:
            self.pacman_y -= 4
 
        if self.down:
            self.pacman_y += 4
 
        
        

class Game(Pacman):
    
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

    