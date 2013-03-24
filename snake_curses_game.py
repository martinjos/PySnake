#!/usr/bin/env python

from snake import Snake
from snake_curses_view import SnakeCursesView
from game import Game

import curses
import time

class SnakeCursesGame:

    def __init__(self):
	self.snake = Snake()

	self.game = Game(80, 24)
	self.game.add_snake(self.snake)
	self.game.start()

	self.w = curses.initscr()
	self.w.nodelay(True)
	self.w.keypad(True)
	curses.curs_set(0) # hide cursor

	self.view = SnakeCursesView(self.w, self.game)
	self.view.add_action_listener(self)

    def turn_action(self, direction):
	self.snake.turn(direction)

    def run(self):
	while True:
	    self.view.draw()
	    self.w.refresh()
	    time.sleep(0.1)
	    self.view.undraw()

	    ch = self.w.getch()
	    if ch in [curses.KEY_UP, curses.KEY_DOWN,
		      curses.KEY_LEFT, curses.KEY_RIGHT]:
		self.view.got_key(ch)
	    elif ch != -1:
		break

	    self.game.tick()

def main():
    try:
	game = SnakeCursesGame()
	game.run()
    finally:
	try:
	    curses.endwin() # ensure that exceptions display correctly
	except:
	    pass

if __name__ == '__main__':
    main()
