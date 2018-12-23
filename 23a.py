import collections
import itertools
import helper
import re

values = list(map(lambda x : list(map(int, re.findall("-?\d+", x))), helper.load_in_list('input_23.txt', str)))#

def dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

c = {}
for x,y,z,r in values:
    p = (x,y,z)
    c[p] = r

k = max(c, key = lambda p : c[p])
r = c[k]

near = [p for p in c if dist(k, p) <= r]
print(len(near))

