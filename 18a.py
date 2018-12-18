import collections
import itertools
import helper
import copy
import re

def print_grid(grid):
    print()
    for y in range(grid.shape[1]):
        print(''.join(c for x, c in enumerate(grid[:,y])))

def tick(g):
    g2 = copy.deepcopy(g)
    max_x = g.shape[0]
    max_y = g.shape[1]

    for i in range(max_x):
        for j in range(max_y):
            space = 0
            trees = 0
            lumber = 0
            for x in range(i-1, i+2):
                
                if x < 0 or x > max_x-1:
                    continue
                for y in range(j-1, j+2):
                    if y < 0 or y > max_y-1:
                        continue
                    if x == i and y == j:
                        continue
                    c = g[x,y]
                    if c == '.':
                        space += 1
                    elif c == '|':
                        trees += 1
                    else:
                        lumber += 1
                
            # print(i,j, space, trees, lumber, g[i,j])
            c = g[i,j]
            if c == '.':
                if trees >= 3:
                    g2[i,j] = '|'
            elif c == '|':
                if lumber >= 3:
                    g2[i,j] = '#'
            else:
                if trees == 0 or lumber == 0:
                    g2[i,j] = '.'

    return g2

def score(grid):
    flat = list(grid.flatten())
    wooded = flat.count('|')
    lumberyards = flat.count('#')
    res = wooded * lumberyards
    return res


grid = helper.load_grid('input_18.txt')

seen_grids = {''.join(grid.flatten())}
scores = []
last_i = 0
start = None

for i in range(1000000000):
    grid = tick(grid)

    if i == 9:
        print(score(grid))

    t = ''.join(grid.flatten())
    if start is None:
        if t in seen_grids:
            start = t
            last_i = i
            scores.append(score(grid))
        else:
            seen_grids.add(t)
    else:
        if t == start:
            r = i - last_i
            m = ((1000000000 - last_i) % r) - 1
            print(scores[m])
            break
        else:
            scores.append(score(grid))
