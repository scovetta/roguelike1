__author__ = 'scovetta'
import curses

screen = None

# This starts up curses.
def start():
    global screen

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.nonl()
    screen.keypad(1)
    screen.timeout(0)
    screen.scrollok(False)

# This stops curses (resets)
def stop():
    global screen

    screen.timeout(-1)
    screen.keypad(0)
    screen.scrollok(True)
    curses.nocbreak()
    curses.curs_set(1)
    curses.nl()
    curses.echo()
    curses.endwin()

    screen = None

# Gets input from the user
def get_input():
    global screen, keymap
    if screen:
        c = screen.getch()
        #curses.flushinp()
        if c > 0 and c < 256: return "%c" % c
        elif c in keymap: return keymap[c]
    return None

# Clears the screen
def clear():
    global screen
    if screen:
        screen.erase()

# Draws a chacater at X, Y, including boundary checks
def draw(x, y, c):
    global screen
    if screen:
        h, w = screen.getmaxyx()
        if x >= 0 and x < w and y >= 0 and y < h and (x, y) != (w-1, h-1):
            screen.addch(y, x, c)

def scr():
    global screen
    return screen

def mode():
    global screen
    return "curses"

# Global key map for abstracting away curses key codes
keymap = {
    curses.KEY_BACKSPACE:   "backspace",
    curses.KEY_UP:          "up",
    curses.KEY_DOWN:        "down",
    curses.KEY_LEFT:        "left",
    curses.KEY_RIGHT:       "right",
    curses.KEY_ENTER:       "\n",
    curses.KEY_HOME:        "home",
    curses.KEY_RESIZE:      "resize",
    curses.KEY_PPAGE:       "page_up",
    curses.KEY_NPAGE:       "page_down",
    -1:                     None
}