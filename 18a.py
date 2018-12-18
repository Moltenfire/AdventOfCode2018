import collections
import itertools
import helper
import copy
import numpy as np

def print_grid(grid):
    print()
    for y in range(grid.shape[1]):
        print(''.join(c for x, c in enumerate(grid[:,y])))

def tick(g):
    g2 = g.copy()
    max_x = g.shape[0]
    max_y = g.shape[1]

    for i in range(max_x):
        for j in range(max_y):
            s = g[max(0, i-1):i+2, max(0, j-1):j+2]
            c = g[i,j]
            if c == '.':
                trees = np.count_nonzero(s == '|')
                if trees >= 3:
                    g2[i,j] = '|'
            elif c == '|':
                lumber = np.count_nonzero(s == '#')
                if lumber >= 3:
                    g2[i,j] = '#'
            else:
                trees = np.count_nonzero(s == '|')
                lumber = np.count_nonzero(s == '#')
                if trees == 0 or lumber == 1:
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
            m = ((1000000000 - last_i - 1) % r)
            print(scores[m])
            break
        else:
            scores.append(score(grid))
