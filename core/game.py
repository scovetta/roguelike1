import curses
import traceback
import sys

from core import world
from core import gfx


# A Game rpresents a single instance of a game, including its maps,
# data, and everything else.
class Game(object):
    def __init__(self):
        self.world = world.World()

    def handle(self, c):
        if   c == "up":     self.world.player_y -= 1
        elif c == "down":   self.world.player_y += 1
        elif c == "left":   self.world.player_x -= 1
        elif c == "right":  self.world.player_x += 1

    # Starts an interactive session between our player and our game object.
    def play(self):
        gfx.start()

        try:
            running = True
            while running:
                c = gfx.get_input()
                self.handle(c)
                if c == "q": running = False
                self.world.draw()
        except:
            gfx.stop()
            print(traceback.format_exc())
            sys.exit(-1)

        gfx.stop()

