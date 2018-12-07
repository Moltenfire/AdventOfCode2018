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

out = ""

while len(steps) > 0:
    possible = list(filter(lambda x : blocked[x] == 0, steps))
    possible.sort()
    c = possible[0]
    out += c
    steps.remove(c)
    for b in edges[c]:
        blocked[b] -= 1

print(out)

