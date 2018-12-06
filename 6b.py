import collections
import itertools
import helper
import re

coords = {x : i for i, x in enumerate(list(map(lambda x : tuple(map(int, re.findall('\d+', x))), helper.load_in_list('input_6.txt', str))))}

min_x = min(coords.keys(), key=lambda x : x[0])[0]
max_x = max(coords.keys(), key=lambda x : x[0])[0]
min_y = min(coords.keys(), key=lambda x : x[1])[1]
max_y = max(coords.keys(), key=lambda x : x[1])[1]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

max_dist = 10000
# max_dist = 32

t = 0
for y in range(min_y, max_y):
    for x in range(min_x, max_x):
        k = (x,y)
        dists = [dist(c, k) for c in coords]
        s = sum(dists)
        if s < max_dist:
            t += 1

print(t)
