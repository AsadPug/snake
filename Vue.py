from Game import Game

import pygame

class Vue():
    def __init__(self):
        self.play_area_size = 600
        self.screen_width = self.play_area_size
        self.screen_height = self.play_area_size*1.1
        self.HUD_height =  self.screen_height - self.play_area_size
        self.font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', int(self.HUD_height))
        
        self.last_score = -1
        self.screen = pygame.display.set_mode(
            (self.screen_width,self.screen_height)
        )
        
        
        
        
    
       
        

    def load_play_area(self, game: Game) -> None:
        self.tile_width = self.play_area_size / game.grid_width
        self.tile_height = self.play_area_size / game.grid_height
        for x in range(game.grid_width):
            for y in range(game.grid_height):
                pygame.draw.rect(
                    self.screen, game.grid[x][y].color , pygame.Rect(
                        (self.tile_width*x),
                        self.HUD_height + (self.tile_height*(game.grid_height - y - 1)),
                        self.tile_width,
                        self.tile_height,
                    )
                )
    
    def load_score(self, score : int) -> None:
        pygame.draw.rect(
            self.screen,(0, 0, 0), pygame.Rect(
            0,0,
            self.screen_width, self.HUD_height
            )
        )
        score_text = self.font.render(
            "Score: " + str(score), True , "WHITE"
        )
        score_text_rect = score_text.get_rect()
        self.screen.blit(score_text, score_text_rect)
        pass
    
    def tick(self, game: Game) -> None:
        self.load_play_area(game)
        if game.score != self.last_score:
            self.load_score(game.score)
            self.last_score+=1
        