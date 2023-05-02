from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3 


class Snake():
    def __init__(self, head: tuple[int, int], initial_size: int) -> None:
        self.head: tuple[int, int] = head
        self.tail: tuple[int, int] = (self.head[0],self.head[1]-initial_size)
        self.direction = Direction.UP 
        self.body: list[tuple[int, int]] = []
        for i in range(initial_size+1):
            self.body.append((self.head[0],self.head[1]-i))
        
    
    def tick(self) -> None:
        if self.direction == Direction.DOWN:
            self.head = (self.head[0],self.head[1]-1)
        elif self.direction == Direction.UP:
            self.head = (self.head[0],self.head[1]+1)
        elif self.direction == Direction.RIGHT:
            self.head = (self.head[0]+1,self.head[1])
        elif self.direction == Direction.LEFT:
            self.head = (self.head[0]-1,self.head[1])
        self.body.insert(0,(self.head[0],self.head[1]))
        self.tail = self.body[len(self.body)-2]
        self.body.pop()
        

