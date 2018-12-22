import collections
import helper
import numpy as np
import operator

def get_type(x):
    if x == 0:
        return '.'
    if x == 1:
        return '='
    return '|'

def print_region_type(grid):
    for y in range(grid.shape[1]):
        print(''.join(get_type(c) for c in grid[:,y]))

def get_erosion(target_x, target_y, depth):
    
    max_x = target_x + 50
    max_y = target_y + 50

    E = np.zeros((max_x + 1, max_y + 1), dtype=np.uint64)

    for y in range(max_y+1):
        for x in range(max_x+1):

            if (x == 0 and y == 0) or (x == target_x and y == target_y):
                geo = 0
            elif x == 0:
                geo = y * 48271
            elif y == 0:
                geo = x * 16807
            else:
                geo = E[x-1,y] * E[x,y-1]

            er = (geo + depth) % 20183
            E[x,y] = er

    return E

def get_adjacent(x,y, max_x, max_y):
        a = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]
        return [(x,y) for x,y in a if x >= 0 and y >= 0 and x < max_x and y < max_y]

rock, wet, narrow = 0, 1, 2
torch, climb, neither = 0, 1, 2
valid = { rock : { climb, torch }, wet : { climb, neither }, narrow : {torch, neither} }

def shortest(region_type, target_x, target_y):
    max_x = region_type.shape[0]
    max_y = region_type.shape[1]
    E = collections.defaultdict(set)

    for x in range(max_x):
        for y in range(max_y):
            xy_type = region_type[x,y]
            i1, i2 = list(valid[xy_type])
            p1 = (x,y,i1)
            p2 = (x,y,i2)
            E[p1].add((p2,7))
            E[p2].add((p1,7))

            next_points = get_adjacent(x,y,max_x,max_y)
            for new_x, new_y in next_points:
                n_type = region_type[new_x, new_y]
                possible_items = valid[xy_type].intersection(valid[n_type])
                for i in possible_items:
                    p1 = (x,y,i)
                    p2 = (new_x,new_y,i)
                    E[p1].add((p2,1))
                    E[p2].add((p1,1))
                    
    start = (0, 0, torch)
    end = (target_x, target_y, torch)
    queue = {start}
    complete = set()
    distances = { n : float('inf') for n in E }
    distances[start] = 0
    while queue:
        node = min(queue, key=lambda n : distances[n])
        queue.remove(node)
        complete.add(node)
        time = distances[node]

        if node == end:
            return time

        adjacent = E[node]

        for n, cost in adjacent:
            if n in complete:
                continue
            queue.add(n)
            new_time = cost + time

            if new_time < distances[n]:
                distances[n] = new_time

def main(depth, target_x, target_y):

    erosion_lvl = get_erosion(target_x, target_y, depth)

    cal_risk = lambda x : x % 3
    region_type = cal_risk(erosion_lvl)

    print(region_type[:target_x+1,:target_y+1].sum())
    print(shortest(region_type, target_x, target_y))

if __name__ == '__main__':
    # main(510, 10, 10)
    main(10647, 7,770)
