from mazegeneration import *

MG = Maze_Generator(40, 10)
MG.create_maze()
class Queue():
    def __init__(self):
        self.path = []

    def enqueue(self, n):
        self.path.append(n)

    def dequeue(self):
        n = self.path[0]
        self.path = self.path[1:]
        return n

def neighbour(step):
    neighbour = []
    if step.north != None:
        neighbour.append(step.north)
    if step.south != None:
        neighbour.append(step.south)
    if step.east != None:
        neighbour.append(step.east)
    if step.west != None:
        neighbour.append(step.west)
    return neighbour


def BFS(graph, start, end):
    Q = Queue()

    path = [start]
    Q.enqueue(path)

    while True:
        cur_path = Q.dequeue()
        last_step = cur_path[-1]

        if last_step == end:
            return cur_path

        for point in neighbour(last_step):
            if point not in cur_path:
                Q.enqueue(cur_path + [point])
    return None


index=0
while index <len(BFS(MG, MG.START, MG.END))-1:
    MG.draw_line(BFS(MG, MG.START, MG.END)[index], BFS(MG, MG.START, MG.END)[index + 1])
    index+=1

