import collections
import itertools
import helper
import re

v = [(x[5], x[36]) for x in helper.load_in_list('input_7.txt', str)]


steps = set()
wait = []
x = collections.defaultdict(set)
for a, b in v:
    steps.add(a)
    steps.add(b)
    x[a].add(b)
    wait.append(b)

# print(steps)
# print(x)
# print(wait)

out = ""

while len(steps) > 0:
    possible = list(steps - set(wait))
    possible.sort()
    c = possible[0]
    out += c
    steps.remove(c)
    for b in x[c]:
        wait.remove(b)

# print(steps)
# print(wait)

# print(b)
print(out)

