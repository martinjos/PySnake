from numbers import Numbers

class Game:

    def __init__(self, w, h):
	self.snakes = []
	self.numbers = Numbers(w, h)

    def add_snake(self, snake):
	self.snakes.append(snake)

    def tick(self):
	for snake in self.snakes:
	    snake.tick()
    
    def get_snakes(self): return self.snakes
