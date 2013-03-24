#!/usr/bin/env python

from snake import Snake
from snake_curses_view import SnakeCursesView

import curses
import time

class SnakeGame:

    def __init__(self):
	self.snake = Snake()

	self.w = curses.initscr()
	self.w.nodelay(True)
	self.w.keypad(True)
	curses.curs_set(0) # hide cursor

	self.view = SnakeCursesView(self.w)
	self.view.add(self.snake)

    def run(self):
	while True:
	    self.view.draw()
	    self.w.refresh()
	    time.sleep(1)
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
	curses.endwin() # ensure that exceptions display correctly

if __name__ == '__main__':
    main()
