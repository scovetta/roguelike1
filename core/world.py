__author__ = 'scovetta'

from core import gfx

def ring(x, y, r):
    report = []
    odd_row = y % 2 == 1

    # starting point, right, 0 degrees
    x += r
    report.append((x, y))
    for i in range(r):  # going up-left
        if not odd_row: x -= 1
        y -= 1
        report.append((x, y))
        odd_row = not odd_row

    for i in range(r): # going left
        x -= 1
        report.append((x, y))

    for i in range(r): #going down-left
        if not odd_row: x -= 1
        y += 1
        odd_row = not odd_row
        report.append((x, y))

    for i in range(r): # going down-right
        if odd_row: x += 1
        y += 1
        odd_row = not odd_row
        report.append((x, y))

    for i in range(r):  # going right
        x += 1
        report.append((x, y))

    for i in range(r):  # going up-right
        if odd_row: x += 1
        y -= 1
        report.append((x, y))
        odd_row = not odd_row

    return report

def view(x, y, r):
    report = []
    for i in range(r):
        report += ring(x, y, i)

    return report

class World(object):
    def __init__(self):
        self.w = 20
        self.h = 20
        self.player_x = 4
        self.player_y = 4

    # Draws the world
    def draw(self):
        gfx.clear()

        my_neighbors = view(self.player_x, self.player_y, 3)

        for y in range(self.h):
            for x in range(self.w):
                x_coord = 2 * x + (y % 2)

                if (self.player_x, self.player_y) == (x, y):
                    gfx.draw(x_coord, y, "@")
                elif (x, y) in my_neighbors:
                    gfx.draw(x_coord, y, ".")

