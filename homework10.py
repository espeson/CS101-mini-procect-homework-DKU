import random

def populate(grid, rfactor):
    for ele in grid:
        a = 0
        for elem in ele:
            num=random.random()
            if num<rfactor:
                ele[a]="*"
            else:
                ele[a]="-"
            a+=1
    return grid

def make_grid(rows, cols):
    return [ ['-' for i in range(cols) ] for j in range(rows) ]

def to_string(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = ''
    for r in range(rows):
        for c in range(cols):
            result += grid[r][c]
        result += '\n'
    return result

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


def update_grid(grid):
    l=[]
    for ele in grid:
        l.append(ele[:])
    r=0
    while r<len(l):
        c=0
        while c<len(l[r]):
            if l[r][c]=="*":
                if num_neighbors(l, r, c)<2:
                    grid[r][c]="-"
                if num_neighbors(l, r, c)>3:
                    grid[r][c] = "-"
            if l[r][c]=="-":
                if num_neighbors(l, r, c)==3:
                    grid[r][c]="*"
            c+=1
        r+=1
random.seed(0)
g = make_grid(10,10)
populate(g,0.5)
print(to_string(g))
update_grid(g)
print(to_string(g))


