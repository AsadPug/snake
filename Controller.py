import pygame
from sys import exit
from Vue import Vue
from Game import Game 

class Controller():
    def __init__(self):
        pygame.init()
        self.vue = Vue()
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.tick()
        
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
        
        self.game.tick()
        self.vue.tick(self.game)
        pygame.display.update()
        self.clock.tick(1)
        self.tick()

    def quit(self) -> None:
        pygame.quit()
        exit()

if __name__ == "__main__":
    controller = Controller()