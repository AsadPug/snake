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
        self.speed = 3
        self.game_loop()
    
    def game_loop(self) -> None:
        while self.game.is_game_over() is False:
            self.tick()
    
    def tick(self):
        keydown_event_done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and keydown_event_done is False:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.game.snake.change_direction(Direction.UP)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.game.snake.change_direction(Direction.DOWN)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.game.snake.change_direction(Direction.LEFT)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.game.snake.change_direction(Direction.RIGHT)
                keydown_event_done = True
        
        self.game.tick()
        self.vue.tick(self.game)
        pygame.display.update()
        self.clock.tick(self.speed)

    def quit(self) -> None:
        pygame.quit()
        exit()

if __name__ == "__main__":
    controller = Controller()