# can not initialize grid using outer multiplication
# careful when dealing with pointer head / tail
# using set instead of grid to use less memory
# !! Snake can move its head into tail! circular! key !

class node(object):
    def __init__(self, x, y, pre=None):
        self.x = x
        self.y = y
        self.pre = pre

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        #self.grid = [[''] * width for _ in xrange(height)]
        #self.grid[0][0] = 'S'
        self.snake = set([])
        self.head = self.tail = node(0, 0)
        self.dirs = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D':(1, 0)}
        self.width = width
        self.height = height
        self.eaten = 0
        self.food = food
        self.cur_food = None
        if food:
            self.cur_food = food.pop(0)
            #self.grid[f[0]][f[1]] = 'F'

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        i, j = [x + y for x, y in zip([self.head.x, self.head.y], self.dirs[direction])]

        if (not (0 <= i < self.height and 0 <= j < self.width)) or \
            ((i,j) in self.snake and (self.tail.x != i or self.tail.y != j)):
                return -1

        if [i, j] == self.cur_food:
            self.eaten += 1
            self.snake.add((i,j))
            self.head.pre = node(i, j)
            self.head = self.head.pre
            if self.food:
                self.cur_food = self.food.pop(0)
            else:
                self.cur_food = None
            return self.eaten

        #self.grid[self.tail.x][self.tail.y] = ''
        self.snake.discard((self.tail.x, self.tail.y))
        self.snake.add((i,j))

        self.head.pre = node(i, j)
        self.head = self.head.pre

        self.tail = self.tail.pre
 
        return self.eaten


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
