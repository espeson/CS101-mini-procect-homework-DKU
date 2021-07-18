from graphics import *
import random
import time
win = GraphWin('Game of Life', 500, 500, autoflush=False)


def make_grid(r, c):
    return [["-" for j in range(c)] for i in range(r)]


def populate(grid, rfactor):
    for ele in grid:
        a = 0
        for elem in ele:
            num = random.random()
            if num < rfactor:
                ele[a] = "*"
            else:
                ele[a] = "-"
            a += 1
    return grid

def num_neighbors(grid, r, c):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(-1,2):
        if c+i < 0 or c+i >= cols:
            continue
        for j in range(-1,2):
            if r+j < 0 or r+j >= rows:
                continue
            if i == 0 and j == 0:
                continue
            if grid[r+j][c+i] == '*':
                count += 1
    return count

def to_string(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = ''
    for r in range(rows):
        for c in range(cols):
            result += grid[r][c]
        result += '\n'
    return result


def update_grid(grid):
    l = []
    for ele in grid:
        l.append(ele[:])
    r = 0
    while r < len(l):
        c = 0
        while c < len(l[r]):
            if l[r][c] == "*":
                if num_neighbors(l, r, c) < 2:
                    grid[r][c] = "-"
                if num_neighbors(l, r, c) > 3:
                    grid[r][c] = "-"
            if l[r][c] == "-":
                if num_neighbors(l, r, c) == 3:
                    grid[r][c] = "*"
            c += 1
        r += 1




def make_display_grid(rows, cols):
    Total = []
    for r in range(rows):
        row=[]
        for c in range(cols):
            Rectangle(Point(c * 10, r * 10), Point(c * 10 + 10, r * 10 + 10)).draw(win)
            R = Rectangle(Point(c * 10, r * 10), Point(c * 10 + 10, r * 10 + 10)).draw(win)
            R.setFill("black")
            row.append(R)
        Total.append(row)
    update()
    return Total


def display(grid, display_grid):
    r=0

    while r<len(grid):
        c = 0
        while c<len(grid[r]):
            if grid[r][c] == "*":
                d=display_grid[r][c]
                d.setFill("green")
            c+=1
        r+=1
    update()



# create a 2-D list of string ('-', '*')
grid = make_grid(50,50)

# create a 2-D list of corresponding Rectangles
display_grid = make_display_grid(50,50)

# populate grid with 50% random live cells
populate(grid,0.5)
# infinite loop that simulates the Game of Life
while True:
    display(grid,display_grid)
    update_grid(grid)

