from Game import Game

import pygame

class Vue():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 1000
        self.play_area_size = 800
        self.screen = pygame.display.set_mode(
            (self.screen_width,self.screen_height)
        )
        self.HUD_height =  self.screen_height - self.play_area_size
        

    def load_play_area(self, game: Game) -> None:

        self.tile_width = self.play_area_size / game.grid_width
        self.tile_height = self.play_area_size / game.grid_height
        for x in range(game.grid_width):
            for y in range(game.grid_height):
                pygame.draw.rect(
                    self.screen, game.grid[x][y].color , pygame.Rect(
                        (self.tile_width*(x-1)),
                        self.HUD_height + (self.tile_height*(game.grid_height-y-1)),
                        (self.tile_width*x),
                        self.HUD_height + (self.tile_height*(game.grid_height-y)),
                    )
                )
    
    def tick(self, game: Game) -> None:
        self.load_play_area(game)