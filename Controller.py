import pygame
from sys import exit
from Vue import Vue
from Game import Game 
from Snake import Direction

class Controller():
    def __init__(self):
        pygame.init()
        self.vue = Vue()
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.game_loop()
    
    def game_loop(self) -> None:
        while self.game.is_game_over is False:
            self.tick()
        print("Your score was " + str(self.game.score))
    
    def tick(self):
        new_direction = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    new_direction = Direction.UP
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    new_direction = Direction.DOWN
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    new_direction = Direction.LEFT
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    new_direction = Direction.RIGHT
        if new_direction is not None:
            self.game.snake.change_direction(new_direction)
        
        self.game.tick()
        self.vue.tick(self.game)
        pygame.display.update()
        self.clock.tick(round(self.game.speed))

    def quit(self) -> None:
        pygame.quit()
        exit()

if __name__ == "__main__":
    controller = Controller()