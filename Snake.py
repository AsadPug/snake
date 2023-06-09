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
        self.size = initial_size
        for i in range(initial_size+1):
            self.body.append((self.head[0],self.head[1]-i))
        
    def change_direction(self, direction: Direction) -> None:
        if ((self.direction == Direction.UP and direction != Direction.DOWN) 
            or (self.direction == Direction.DOWN and direction != Direction.UP)
            or (self.direction == Direction.RIGHT and direction != Direction.LEFT)
            or (self.direction == Direction.LEFT and direction != Direction.RIGHT)):
            self.direction = direction


    def is_snake_looped(self) -> bool:
        looped = False
        for i in range (1,len(self.body)-1):
            if(self.body[i] == self.head):
                looped = True
        return looped
            
        
    def tick(self, is_growing: bool) -> None:
        if self.direction == Direction.DOWN:
            self.head = (self.head[0],self.head[1]-1)
        elif self.direction == Direction.UP:
            self.head = (self.head[0],self.head[1]+1)
        elif self.direction == Direction.RIGHT:
            self.head = (self.head[0]+1,self.head[1])
        elif self.direction == Direction.LEFT:
            self.head = (self.head[0]-1,self.head[1])
        self.body.insert(0,(self.head[0],self.head[1]))

        if is_growing is False:        
            self.body.pop()
            self.tail = self.body[len(self.body)-1]
        elif is_growing is True:
            self.size+=1

   
        

