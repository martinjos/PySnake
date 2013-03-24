from numbers import Numbers

class Game:

    def __init__(self, w, h):
	self.snakes = []
	self.numbers = Numbers(w, h, self)

    # for the time being, only has to check for snakes
    def check_space_empty(self, x, y):
	for snake in self.snakes:
	    for cell in snake.get_cells():
		if cell[0] == x and cell[1] == y:
		    return False
	return True

    def add_snake(self, snake):
	self.snakes.append(snake)

    # called after all snakes have been added
    def start(self):
	self.numbers.next()

    def tick(self):
	for snake in self.snakes:
	    snake.tick()
	    cells = snake.get_cells()
	    if self.numbers.is_valid() and \
	       cells[-1][0] == self.numbers.get_x() and \
	       cells[-1][1] == self.numbers.get_y():
		self.numbers.next()
    
    def get_snakes(self): return self.snakes
    def get_numbers(self): return self.numbers
