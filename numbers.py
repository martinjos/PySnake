import random

class Numbers:

    def __init__(self, w, h, checker):
	self.number = 0
	self.top = 9
	self.w = w
	self.h = h
	self.x = self.y = -1
	self.checker = checker
	self.valid = False

    def next(self):
	if self.number == self.top:
	    #self.valid = False
	    #return False
	    self.number = 0 # DEBUG: start over
	self.number += 1
	self.rand_pos()
	while not self.checker.check_space_empty(self.x, self.y):
	    self.rand_pos()
	self.valid = True
	return True

    def rand_pos(self):
	self.x = random.randint(0, self.w - 1)
	self.y = random.randint(0, self.h - 1)

    def get_x(self): return self.x
    def get_y(self): return self.y
    def get_number(self): return self.number
    def is_valid(self): return self.valid
