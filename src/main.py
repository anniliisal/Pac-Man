
import pygame

from game import Game


class Main:
    def __init__(self):
        self.game = Game()
        self.score = 0
        self.play()

    def play(self):
        """game loop"""
        while True:
            if self.game.game_over is True:
                self.score = self.game.point_count
                self.game = Game()
                self.game.save_game_over_score(self.score)
                self.game.first_game_screen = False
                self.game.game_over_screen = True
            if self.game.game_win is True:
                self.game = Game()
                self.game.first_game_screen = False
                self.game.game_win_screen = True
            pygame.time.Clock().tick(300)
            self.game.draw_screen()
            self.game.update_place()
            self.game.move()
            pygame.display.flip()


if __name__ == "__main__":
    main = Main()
