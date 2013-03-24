class Snake:

    UP    = ( 0, -1)
    DOWN  = ( 0,  1)
    LEFT  = (-1,  0)
    RIGHT = ( 1,  0)

    def __init__(self):
	self.cells = [(5,5), (6,5), (7,5), (8,5)]
	self.direction = Snake.RIGHT
	self.last_direction = Snake.RIGHT

    def tick(self, grow = False):
	if not grow:
	    self.cells.pop(0)
	self.cells.append(tuple(map(lambda x, y: x + y, self.cells[-1],
						        self.direction)))
	self.last_direction = self.direction

    def turn(self, direction):
	if direction != tuple(map(lambda x: -x, self.last_direction)):
	    self.direction = direction
	    return True
	return False

    def get_cells(self):
	return self.cells
