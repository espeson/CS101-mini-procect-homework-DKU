def make_grid(r, c):
    return [["-" for j in range(c)] for i in range(r)]


def to_string(grid):
    list = ""
    i=0
    while i<=len(grid):
        list+="\n"
        if i<len(grid):
            for ele in grid[0]:
                list += "-"
        i+=1
    return list[1:]

g = make_grid(5,5)
g[0][2] = '*'
g[0][3] = '*'
g[1][0] = '*'
g[1][2] = '*'
g[1][3] = '*'
g[2][2] = '*'
g[3][0] = '*'
g[4][0] = '*'
g[4][4] = '*'
g[0][2] = '*'
g[0][3] = '*'
g[1][0] = '*'
g[1][2] = '*'
g[1][3] = '*'
g[2][2] = '*'
g[3][0] = '*'
g[4][0] = '*'
g[4][4] = '*'
def num_neighbors(grid, r, c):
    list=""
    count=0
    if c-1>=0:
        list+=grid[r][c-1]
    if c+1<=4:
        list+=grid[r][c+1]
    if r-1>=0:
        list+=grid[r-1][c]
    if r+1<=4:
        list+=grid[r+1][c]
    if c-1>=0 and r-1>=0:
        list+=grid[r-1][c-1]
    if c-1>=0 and r+1<=4:
        list+=grid[r+1][c-1]
    if c+1<=4 and r-1>=0:
        list+=grid[r-1][c+1]
    if c+1<=4 and r+1<=4:
        list+=grid[r+1][c+1]
    for ele in list:
        if ele=="*" :
            count+=1
    return count
    # if (c-1>=0 and c+1<=r) and (r-1>=0 and r+1<=c):
    # for n in range(-1,2):
    #     if r+n>=0 and r+n<=c:
    #         item=grid[r-n][c]
    #         list+=item
    #     list[1]="-"
    #     if r+n>=0 and r+n<=c:
    #         item=grid[r-n][c-1]
    #         list+=item
    #     if r+n>=0 and r+n<=c:
    #         item=grid[r-n][c+1]
    #         list+=item
    #     for ele in list:
    #         if ele=="*":
    #             count+=1
    #             return count
    # if c-1<0 or c+1>r or r-1<0 or r+1>c:
    #     if c-1<0 and c+1<=r and (r-1>=0 and r+1<=c):
    #         item=grid[c][r-1]
    #         list+=item
    #         item = grid[c][ r - 1]
    #         list += item
    #         item = grid[c][ r + 1]
    #         list += item
    #         item = grid[c+1][ r-1]
    #         list += item
    #         item = grid[c+1][ r ]
    #         list += item
    #         item = grid[c+1][r+1]
    #         list += item
    #         for ele in list:
    #             if ele == "*":
    #                 count += 1
    #                 return count
    #     if c-1<0 and r-1<0:
    #         item = grid[c][ r + 1]
    #         list += item
    #         item = grid[c+1][ r ]
    #         list += item
    #         item = grid[c+1][ r+1]
    #         list += item
    #         for ele in list:
    #             if ele == "*":
    #                 count += 1
    #                 return count
    #     if c - 1 < 0 or c + 1 > r or r - 1 < 0 or r + 1 > c:
    #         if c - 1 < 0 and c + 1 <= r and (r - 1 >= 0 and r + 1 <= c):
    #             item = grid[c][ r - 1]
    #             list += item
    #             item = grid[c][ r - 1]
    #             list += item
    #             item = grid[c][ r + 1]
    #             list += item
    #             item = grid[c + 1][ r - 1]
    #             list += item
    #             item = grid[c + 1][ r]
    #             list += item
    #             item = grid[c + 1][r + 1]
    #             list += item
    #             for ele in list:
    #                 if ele == "*":
    #                     count += 1
    #                     return count
print(num_neighbors(g,2,2))




