from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3 


class Snake():
    def __init__(self, head: tuple[int, int], initial_size: int) -> None:
        self.head: tuple[int, int] = head
        self.direction = Direction.DOWN 
        self.body: list[tuple[int, int]] = []
        for i in range(initial_size):
            self.body.append((self.head[0],self.head[1]-i))
    
    def tick(self) -> None:
        pass
