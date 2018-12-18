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

    for i in range(g.shape[0]):
        for j in range(g.shape[1]):
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

def get_score(grid):
    return np.count_nonzero(grid == '|') * np.count_nonzero(grid == '#')

grid = helper.load_grid('input_18.txt')
seen_grids = collections.defaultdict(int)
scores = []

for i in range(1000000000):
    grid = tick(grid)
    score = get_score(grid)
    scores.append(score)

    if i == 9:
        print(score)

    t = ''.join(grid.flatten())
    
    if t in seen_grids:
        prev_i = seen_grids[t]
        r = i - prev_i
        m = ((1000000000 - prev_i - 1) % r)
        print(scores[m-r-1])
        break
    else:
        seen_grids[t] = i
