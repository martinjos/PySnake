Simple "snake" game

The game may not be much to look at at the moment, but I think you may find
some aspects of the code interesting.

* An example of Object-Oriented Python code (& the only example of this so far
in my Git repository).
* An example of the Observable design pattern.
* An example of the use of basic MVC concepts.
    * The two alternative versions of the program (Curses and Tkinter) both use
    the same model code (game.py, snake.py & numbers.py).

Further work

* Make the controller (_game.py) shared between versions?
* Implement walls & collisions.
* Improve graphics & efficiency of Tkinter version.
