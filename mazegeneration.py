from graphics import *
import random

# GRAPHICS Library Lines are produced from p1 to p2 (excluding p2)!

# The CELL class represents an (x,y) location in the maze. It contains
# pointers to the CELL objects that are to its north, south, west, and east.
# Initially, these are all set to NONE.
class Cell():
    def __init__(self, loc, width):
        self.x = loc[0]
        self.y = loc[1]
        self.width = width
        self.visited = False

        self.north = None
        self.south = None
        self.west = None
        self.east = None

    def get_location(self):
        return (self.x, self.y)

    def set_visited(self):
        self.visited = True

    def was_visited(self):
        return self.visited

    def get_north_wall(self):
        return ((self.x*self.width+1, self.y*self.width),
                ((self.x+1)*self.width, self.y*self.width))

    def get_south_wall(self):
        return ((self.x*self.width+1, (self.y+1)*self.width),
                ((self.x+1)*self.width, (self.y+1)*self.width))

    def get_west_wall(self):
        return ((self.x*self.width, self.y*self.width+1),
                (self.x*self.width, (self.y+1)*self.width))

    def get_east_wall(self):
        return (((self.x+1)*self.width, self.y*self.width+1),
                ((self.x+1)*self.width,(self.y+1)*self.width))

    def __str__(self):
        result = '({},{}) - neighbors: '.format(self.x,self.y)

        if self.north:
            result += 'north '
        if self.south:
            result += 'south '
        if self.west:
            result += 'west '
        if self.east:
            result += 'east '

        return result


# The MAZE_GENERATOR class will create a 2-D list of Cell objects.
# The only two functions required for this project are: CREATE_MAZE
# and DRAW_LINE.
class Maze_Generator():
    def __init__(self, size, width):
        self.size = size
        self.width = width
        self.fcolor = 'black'
        self.bcolor = 'yellow'
        self.vcolor = 'white'
        self.START = None
        self.END = None

        self.grid = [ [ Cell((x,y),width) for x in range(size) ] for y in range(size) ]

        self.win = GraphWin("Maze", size*width+1, size*width+1)
        self.win.setBackground(self.bcolor)

        # Point (column, row) or (x, y)
        # Draw Maze with all walls
        for i in range(size+1):
            l = Line(Point(i*width,0),Point(i*width,size*width+1))
            l.setFill(self.fcolor)
            l.draw(self.win)
        for i in range(size+1):
            l = Line(Point(0,i*width),Point(size*width,i*width))
            l.setFill(self.fcolor)
            l.draw(self.win)

    def break_wall(self, c1, c2):
        loc1, loc2 = c1.get_location(), c2.get_location()
        x1,y1,x2,y2 = loc1[0],loc1[1],loc2[0],loc2[1]
        tup = None

        if x1 == x2 and y1 == y2 + 1:
            tup = c1.get_north_wall()
            c1.north = c2
            c2.south = c1
        elif x1 == x2 and y1 == y2 - 1:
            tup = c1.get_south_wall()
            c1.south = c2
            c2.north = c1
        elif y1 == y2 and x1 == x2 + 1:
            tup = c1.get_west_wall()
            c1.west = c2
            c2.east = c1
        elif y1 == y2 and x1 == x2 - 1:
            tup = c1.get_east_wall()
            c1.east = c2
            c2.west = c1
        
        p1,p2 = tup[0],tup[1]
        x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]

        l = Line(Point(x1,y1),Point(x2,y2))
        l.setFill(self.vcolor)
        l.draw(self.win)

    def neighbor_locs(self, tup):
        x,y = tup[0],tup[1]
        n_list = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        result = []

        for loc in n_list:
            if loc[0] >= 0 and loc[0] < self.size and loc[1] >= 0 and loc[1] < self.size and not self.grid[loc[1]][loc[0]].was_visited():
                result.append(loc)

        return result

    def visited_color(self, cell):
        loc = cell.get_location()
        x1,y1 = loc[0]*self.width+1,loc[1]*self.width+1
        x2,y2 = x1+self.width-2,y1+self.width-2

        r = Rectangle(Point(x1,y1),Point(x2,y2))
        r.setFill(self.vcolor)
        r.setOutline(self.vcolor)
        r.draw(self.win)

    # This function takes no input. It creates the 2-D list of Cell objects
    # and draws the maze in a GRAPHICS window.
    def create_maze(self):
        stack = []

        self.START = self.grid[self.size-1][random.randint(0,self.size-1)]
        self.END = self.grid[random.randint(0,self.size-2)][random.randint(0,self.size-1)]
        init_loc = self.START.get_location()
        self.break_wall(self.START,Cell((init_loc[0],init_loc[1]+1),self.width))
        self.START.south = None

        self.START.set_visited()
        self.visited_color(self.START)
        stack.append(self.START)

        while len(stack) != 0:
            cur_cell = stack[-1]
            stack = stack[:-1]

            n_list = self.neighbor_locs(cur_cell.get_location())

            if len(n_list) > 0:
                stack.append(cur_cell)
                loc = random.choice(n_list)

                cho_cell = self.grid[loc[1]][loc[0]]

                self.break_wall(cur_cell,cho_cell)
                cho_cell.set_visited()
                self.visited_color(cho_cell)
                stack.append(cho_cell)

        cs = Circle(Point(self.START.x*self.width+self.width//2,self.START.y*self.width+self.width//2),self.width//3)
        cs.setFill('red')
        ce = Circle(Point(self.END.x*self.width+self.width//2,self.END.y*self.width+self.width//2),self.width//3)
        ce.setFill('black')

        cs.draw(self.win)
        ce.draw(self.win)

        for r in range(self.size):
            for c in range(self.size):
                self.grid[r][c].visited = False

    # This function takes 2 Cell objects as input (and an optional GRAPHICS
    # color) and draws a GRAPHICS Line object from the center of C1 to the
    # center of C2.
    def draw_line(self, c1, c2, col='green'):
        x1,y1,x2,y2 = c1.x,c1.y,c2.x,c2.y
        l = Line(Point(x1*self.width+self.width//2,y1*self.width+self.width//2),Point(x2*self.width+self.width//2,y2*self.width+self.width//2))
        l.setFill(col)
        l.draw(self.win)
