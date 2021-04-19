
from src.game import Game



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

