#!/usr/bin/env python

from snake import Snake
from snake_tkinter_view import SnakeTkinterView
from game import Game

import Tkinter
import time

class SnakeTkinterGame:

    def __init__(self):
	cols = 50
	rows = 50
	side = 10

	self.snake = Snake()

	self.game = Game(cols, rows)
	self.game.add_snake(self.snake)
	self.game.start()

	self.w = Tkinter.Tk()
	self.c = Tkinter.Canvas(self.w,
				width=side*cols,
				height=side*rows,
				background='black')
	self.c.pack()

	self.view = SnakeTkinterView(self.c, side, self.game)
	self.view.add_action_listener(self)

	for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
	    self.w.bind(key, self.view.got_key)

    def turn_action(self, direction):
	self.snake.turn(direction)

    def tick(self):
	self.game.tick()
	self.view.draw()
	self.c.after(100, self.tick) # keep going

    def run(self):
	self.view.draw()
	self.c.after(100, self.tick)
	self.c.mainloop()

def main():
    game = SnakeTkinterGame()
    game.run()

if __name__ == '__main__':
    main()
