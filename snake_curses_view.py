class SnakeCursesView:

    def __init__(self, window):
	self.w = window
	self.snakes = []
	self.w.erase() # clear the window

    def add(self, snake):
	self.snakes += [snake]

    def draw(self, ch = '*'):
	for snake in self.snakes:
	    for cell in snake.get_cells():
		self.w.addch(cell[1], cell[0], ch)

    def undraw(self):
	self.draw(' ')
