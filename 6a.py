import collections
import itertools
import helper
import re

coords = {x : i for i, x in enumerate(list(map(lambda x : tuple(map(int, re.findall('\d+', x))), helper.load_in_list('input_6.txt', str))))}

min_x = min(coords.keys(), key=lambda x : x[0])[0]
max_x = max(coords.keys(), key=lambda x : x[0])[0]
min_y = min(coords.keys(), key=lambda x : x[1])[1]
max_y = max(coords.keys(), key=lambda x : x[1])[1]
print(min_x, min_y, max_x, max_y)

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

l = []
for y in range(min_y, max_y):
    for x in range(min_x, max_x):
        k = (x,y)
        dists = [dist(c, k) for c in coords]
        min_d = min(dists)
        if dists.count(min_d) == 1:
            l.append(dists.index(min_d))

r = []
for y in range(min_y - 1, max_y + 1):
    for x in [min_x - 1, max_x + 1]:
        k = (x,y)
        dists = [dist(c, k) for c in coords]
        min_d = min(dists)
        if dists.count(min_d) == 1:
            r.append(dists.index(min_d))

for x in range(min_x - 1, max_x + 1):
    for y in [min_y - 1, max_y + 1]:
        k = (x,y)
        dists = [dist(c, k) for c in coords]
        min_d = min(dists)
        if dists.count(min_d) == 1:
            r.append(dists.index(min_d))

r = set(r)

for i, count in collections.Counter(l).most_common():
    if i not in r:
        print(i, count)
