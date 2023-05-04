from Snake import Snake
import random

class Game():
    def __init__(self) -> None:
        self.grid_height = 20
        self.grid_width = 20
        self.initial_snake_size = 5
        self.score = 0
        self.grid: list[list[Tile]] = []
        self.apple_picked: bool = True
        self.speed = 3
        self.is_game_over = False

        for x in range(self.grid_width):
            self.grid.append([])
            for y in range(self.grid_height):
                self.grid[x].append(EmptyTile())
        
        self.snake = Snake(
            (int(self.grid_width/2),int(self.grid_height/2)),self.initial_snake_size
        )

        self.place_apple()
        
    def check_game_over(self) -> bool:
        is_game_over = False
        if (self.snake.head[0] < 0 or self.snake.head[1] < 0
            or self.snake.head[0] >= self.grid_width 
            or self.snake.head[1] >= self.grid_height):
            is_game_over = True
        elif self.snake.is_snake_looped() is True:
            is_game_over = True
        else:
            is_game_over = False
        return is_game_over
    
    def tick(self) -> None:
        if self.apple_picked is True:
            self.speed+=0.5
            self.snake.tick(True)
            self.score = self.snake.size - self.initial_snake_size
            self.place_apple()
        elif self.apple_picked is False:
            self.snake.tick(False)
        self.apple_picked = self.is_picking_up_apple()
        self.is_game_over = self.check_game_over()
        if self.is_game_over is False:
            self.update_snake()
    
    def is_picking_up_apple(self) -> bool:
        return (self.snake.head == self.apple.position)

    def place_apple(self) -> None:
        while self.apple_picked is True:
            x = random.randint(0, self.grid_width-1)
            y = random.randint(0, self.grid_height-1)
            if isinstance(self.grid[x][y], EmptyTile):
                self.grid[x][y] = Apple((x, y))
                self.apple: Apple = self.grid[x][y]
                self.apple_picked = False
        
        
    def update_snake(self) -> None:
        for snakeTile in self.snake.body:
            if snakeTile == self.snake.head:
                self.grid[snakeTile[0]][snakeTile[1]] = SnakePiece(True)
            elif snakeTile == self.snake.tail:
                self.grid[snakeTile[0]][snakeTile[1]] = EmptyTile()
            else:
                self.grid[snakeTile[0]][snakeTile[1]] = SnakePiece()
            
        
    

class Tile():
    def __init__(self,color: tuple[int, int, int], walkable: bool = True) -> None:
        self.walkable = walkable
        self.color = color

class EmptyTile(Tile):
    def __init__(self) -> None:
        super().__init__((50, 50, 50))

class Apple(Tile):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__((255, 0, 0))
        self.position = position

class SnakePiece(Tile):
    def __init__(self, isHead: bool = False) -> None:
        if isHead is True:
            color = (100, 255, 100)
        else:
            color = (0, 255, 0)
        super().__init__(color, False)
        

class Wall(Tile):
    def __init__(self) -> None:
        super().__init__((255, 255, 255),False)
        