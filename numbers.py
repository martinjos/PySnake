class Numbers:

    def __init__(self, w, h):
	self.number = 0
	self.top = 9
	self.w = w
	self.h = h
	self.x = self.y = -1

    def next():
	if self.number == self.top:
	    return False
	self.number += 1
	rand_pos()
	while not self.checker.check(self.x, self.y):
	    rand_pos()
	return True

    def rand_pos():
	self.x = random.randint(0, self.w)
	self.y = random.randint(0, self.h)

    def get_x(): return x
    def get_y(): return y
    def get_number(): return number
