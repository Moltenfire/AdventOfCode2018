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

t = 0
total_workers = 5
extra_time = 60
workers = {}
while True:
    # print(workers)
    for c in list(workers.keys()):
        if workers[c] == 0:
            workers.pop(c)
            for b in x[c]:
                wait.remove(b)

    for i in range(len(workers), total_workers):
        possible = list(steps - set(wait))
        possible.sort()
        if len(possible) > 0:
            c = possible[0]
            steps.remove(c)
            workers[c] = ord(c) - 64 + extra_time

    for c in workers:
        workers[c] -= 1

    if len(workers) == 0:
        break
    t += 1

print(t)

    