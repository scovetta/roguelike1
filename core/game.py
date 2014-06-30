import curses
import traceback
import sys

stdscr = None

# A Game rpresents a single instance of a game, including its maps,
# data, and everything else.
class Game(object):
    def __init__(self):
        pass

    def step(self):
        running = True
        x, y = 5, 5
        while running:
            c = stdscr.getch()

            if c == curses.KEY_UP:      y -= 1
            elif c == curses.KEY_DOWN:  y += 1
            elif c == curses.KEY_LEFT:  x -= 1
            elif c == curses.KEY_RIGHT: x += 1
            elif c == ord('q'): running = False
            if c != -1:
                stdscr.clear()
                stdscr.addch(y, x, "@")

    # Starts an interactive session between our player and our game object.
    def play(self):
        global stdscr

        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        stdscr.keypad(1)
        stdscr.timeout(0)


        try:
            self.step()
        except:
            curses.nocbreak()
            stdscr.timeout(-1)
            stdscr.keypad(0)
            curses.echo()
            curses.endwin()

            print(traceback.format_exc())

            sys.exit(-1)

        curses.nocbreak()
        curses.curs_set(1)
        stdscr.timeout(-1)
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()
