#!/usr/bin/env python

from snake import Snake
from snake_curses_view import SnakeCursesView
from numbers import Numbers

import curses
import time

class SnakeGame:

    def __init__(self):
	self.snake = Snake()
	self.numbers = Numbers(80, 24)

	self.w = curses.initscr()
	self.w.nodelay(True)
	self.w.keypad(True)
	curses.curs_set(0) # hide cursor

	self.view = SnakeCursesView(self.w)
	self.view.add(self.snake)
	self.view.add_action_listener(self)

    def turn_action(self, direction):
	self.snake.turn(direction)

    def run(self):
	while True:
	    self.view.draw()
	    self.w.refresh()
	    time.sleep(0.5)
	    self.view.undraw()

	    ch = self.w.getch()
	    if ch in [curses.KEY_UP, curses.KEY_DOWN,
		      curses.KEY_LEFT, curses.KEY_RIGHT]:
		self.view.got_key(ch)
	    elif ch != -1:
		break

	    self.snake.tick()

def main():
    try:
	game = SnakeGame()
	game.run()
    finally:
	try:
	    curses.endwin() # ensure that exceptions display correctly
	except:
	    pass

if __name__ == '__main__':
    main()
