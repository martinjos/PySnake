from numbers import Numbers

class Game:

    class SnakeInfo:
	def __init__(self, snake):
	    self.snake = snake
	    self.grow_num = 0

	def grow(self, num):
	    self.grow_num += num

	def do_growth(self):
	    growing = self.grow_num != 0
	    if growing:
		self.grow_num -= 1
	    return growing

	def get_snake(self): return self.snake
	def get_cells(self): return self.snake.get_cells()

    def __init__(self, w, h):
	self.snakes = []
	self.numbers = Numbers(w, h, self)

    # for the time being, only has to check for snakes
    def check_space_empty(self, x, y):
	for snake_info in self.snakes:
	    snake = snake_info.get_snake()
	    for cell in snake.get_cells():
		if cell[0] == x and cell[1] == y:
		    return False
	return True

    def add_snake(self, snake):
	self.snakes.append(Game.SnakeInfo(snake))

    # called after all snakes have been added
    def start(self):
	self.numbers.next()

    def tick(self):
	for snake_info in self.snakes:
	    snake = snake_info.get_snake()
	    snake.tick(snake_info.do_growth())
	    cells = snake.get_cells()
	    if self.numbers.is_valid() and \
	       cells[-1][0] == self.numbers.get_x() and \
	       cells[-1][1] == self.numbers.get_y():
		self.numbers.next()
		snake_info.grow(4)
    
    def get_snakes(self): return self.snakes
    def get_numbers(self): return self.numbers
