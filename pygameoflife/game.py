from pygameoflife import seeds
import curses
from time import sleep

HEIGHT = 10
WIDTH = 10
SLEEP_TIME = 0
CELL_CHAR='.'


class Game(object):
    def __init__(self, height=HEIGHT, width=WIDTH, sleep_time=SLEEP_TIME, debug=False):
        self.debug = debug
        self.sleep_time = sleep_time
        self.grid = []
        self.height = height
        self.width = width
        for y in xrange(0, height):
            self.grid.append([])
            for x in xrange(0, width):
                self.grid[y].append(Cell(self.grid, y, x))

    def tick(self):
        for row in self.grid:
            for cell in row:
                if cell.alive:
                    if cell.neighbors < 2:
                        cell.to_destroy = True
                    elif 2 <= cell.neighbors <= 3:
                        pass
                    elif cell.neighbors > 3:
                        cell.to_destroy = True
                else:
                    if cell.neighbors == 3:
                        cell.to_create = True
        for row in self.grid:
            for cell in row:
                if cell.to_create:
                    cell.create()
                elif cell.to_destroy:
                    cell.destroy()

    def seed(self, pattern):
        seed_function = getattr(seeds, pattern)
        seed_function(self.grid)
        
    def draw(self, screen):
        self.screen = screen
        self.window = curses.newwin(self.height, self.width, 0, 0)
        while True:
            for y in xrange(0, self.height):
                for x in xrange(0, self.width):
                    try:
                        if self.grid[y][x].alive:
                            if self.debug:
                                self.window.addch(y, x, str(self.grid[y][x].neighbors))
                            else:
                                self.window.addch(y, x, str(CELL_CHAR))
                        else:
                            self.window.addch(y, x, str(' '))
                    except curses.error:
                        pass
            self.window.refresh()
            sleep(self.sleep_time)
            self.tick()



class Cell(object):
    def __init__(self, parent, y, x):
        self.grid = parent
        self.y = y
        self.x = x
        self.alive = False
        self.neighbors = 0
        self.to_destroy = False
        self.to_create = False

    def destroy(self):
        self.alive = False
        self.to_destroy = False
        self.notify_neighbors(self.alive)

    def create(self):
        self.alive = True
        self.to_create = False
        self.notify_neighbors(self.alive)

    def notify_neighbors(self, cell_alive):
        if cell_alive:
            operand = 1
        else:
             operand = -1
        try:
            self.grid[self.y][self.x+1].neighbors += operand
            self.grid[self.y-1][self.x+1].neighbors += operand
            self.grid[self.y-1][self.x].neighbors += operand
            self.grid[self.y-1][self.x-1].neighbors += operand
            self.grid[self.y][self.x-1].neighbors += operand
            self.grid[self.y+1][self.x-1].neighbors += operand
            self.grid[self.y+1][self.x].neighbors += operand
            self.grid[self.y+1][self.x+1].neighbors += operand
        except:
            pass
