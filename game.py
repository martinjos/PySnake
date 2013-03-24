from numbers import Numbers

class Game:

    def __init__(self, w, h):
	self.snakes = []
	self.numbers = Numbers(w, h, self)

    # for the time being, only has to check for snakes
    def check_space_empty(x, y):
	for snake in self.snakes:
	    for cell in snake.get_cells():
		if cell[0] == x and cell[1] == y:
		    return False
	return True

    def add_snake(self, snake):
	self.snakes.append(snake)

    def tick(self):
	for snake in self.snakes:
	    snake.tick()
    
    def get_snakes(self): return self.snakes
