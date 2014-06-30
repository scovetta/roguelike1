import curses
import traceback
import sys

from core import gfx


# A Game rpresents a single instance of a game, including its maps,
# data, and everything else.
class Game(object):
    def __init__(self):
        pass

    def step(self):
        running = True
        x, y = 5, 5
        while running:
            c = gfx.scr().getch()

            if c == curses.KEY_UP:      y -= 1
            elif c == curses.KEY_DOWN:  y += 1
            elif c == curses.KEY_LEFT:  x -= 1
            elif c == curses.KEY_RIGHT: x += 1
            elif c == ord('q'): running = False
            if c != -1:
                gfx.scr().clear()
                gfx.scr().addch(y, x, "@")

    # Starts an interactive session between our player and our game object.
    def play(self):
        gfx.start()

        try:
            self.step()
        except:
            gfx.stop()
            print(traceback.format_exc())
            sys.exit(-1)

        gfx.stop()

