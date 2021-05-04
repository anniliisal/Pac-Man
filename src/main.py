
import pygame
from game import Game


class Main:
    def __init__(self):
        self.game = Game()
        self.play()

    def play(self):
        while True:
            self.game.draw_screen()
            self.game.update_place()
            self.game.move()
            pygame.display.flip()


if __name__ == "__main__":
    main = Main()
