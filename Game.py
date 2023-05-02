from Snake import Snake

class Game():
    def __init__(self) -> None:
        self.grid_height = 80
        self.grid_width = 80
        self.initial_snake_size = 5
        self.grid: list[list[Tile]] = []
        for x in range(self.grid_width):
            self.grid.append([])
            for y in range(self.grid_height):
                self.grid[x].append(Tile((50, 50, 50)))
        self.snake = Snake(
            (int(self.grid_width/2),int(self.grid_height/2)),self.initial_snake_size
        )
        
    def tick(self) -> None: 
        self.snake.tick()
        self.update_snake()

    def update_snake(self) -> None:
        for snakeTile in self.snake.body:
            if(snakeTile == self.snake.head):
                self.grid[snakeTile[0]][snakeTile[1]] = SnakePiece(True)
            else:
                self.grid[snakeTile[0]][snakeTile[1]] = SnakePiece()
            print(self.grid[snakeTile[0]][snakeTile[1]].color)
        
    

class Tile():
    def __init__(self,color: tuple[int, int, int], walkable: bool = True) -> None:
        self.walkable = walkable
        self.color = color

class Apple(Tile):
    def __init__(self) -> None:
        super().__init__((255, 0, 0))

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
        