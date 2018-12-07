import collections
import itertools
import helper
import re

v = [(x[5], x[36]) for x in helper.load_in_list('input_7.txt', str)]

steps = set()
edges = collections.defaultdict(list)
blocked = collections.defaultdict(int)
for a, b in v:
    steps.add(a)
    steps.add(b)
    edges[a].append(b)
    blocked[b] += 1

time = 0
total_workers = 5
extra_time = 60
workers = {}
while True:
    for c in list(workers.keys()):
        if workers[c] == 0:
            workers.pop(c)
            for b in edges[c]:
                blocked[b] -= 1

    for i in range(len(workers), total_workers):
        possible = list(filter(lambda x : blocked[x] == 0, steps))
        possible.sort()
        if len(possible) > 0:
            c = possible[0]
            steps.remove(c)
            workers[c] = ord(c) - 64 + extra_time

    if len(workers) == 0:
        break
    
    if workers:
        min_time = min(workers.values())
        for c in workers:
            workers[c] -= min_time
        time += min_time

print(time)
