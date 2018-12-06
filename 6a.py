import collections
import itertools
import helper
import re

coords = {x : i for i, x in enumerate(list(map(lambda x : tuple(map(int, re.findall('\d+', x))), helper.load_in_list('input_6.txt', str))))}

min_x = min(coords.keys(), key=lambda x : x[0])[0]
max_x = max(coords.keys(), key=lambda x : x[0])[0]
min_y = min(coords.keys(), key=lambda x : x[1])[1]
max_y = max(coords.keys(), key=lambda x : x[1])[1]

max_dist = 10000

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

l = []
edge = set()
total = 0
for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        k = (x,y)
        dists = [dist(c, k) for c in coords]
        min_d = min(dists)
        # Part 1
        if dists.count(min_d) == 1:
            l.append(dists.index(min_d))
            if x == min_x or x == max_x or y == min_y or y == max_y:
                edge.add(dists.index(min_d))
        # Part 2
        if sum(dists) < max_dist:
            total += 1

area = [count for i, count in collections.Counter(l).most_common() if i not in edge][0]
print(area)
print(total)
