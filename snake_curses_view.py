import curses

from snake import Snake

class SnakeCursesView:

    KEY_MAP = {
	curses.KEY_UP: Snake.UP,
	curses.KEY_DOWN: Snake.DOWN,
	curses.KEY_LEFT: Snake.LEFT,
	curses.KEY_RIGHT: Snake.RIGHT
    }

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

    def got_key(self, ch):
	direction = SnakeCursesView.KEY_MAP[ch]
	for snake in self.snakes:
	    snake.turn(direction)
