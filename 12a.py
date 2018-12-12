import collections
import itertools
import helper
import re
import matplotlib.pyplot as plt
import copy

values = helper.load_in_list('input_12.txt', str)

p = values[0].split()[2]
m = { x : y for x , y in map(lambda x : x.split(' => '), values[2:])}

p = '.' * 5 + p + '.' * 2000
# print(m)

def plant_count(p):
    t = 0
    for i, x in enumerate(p):
        if x == '#':
            t += i - 5
    return t

def next_gen(p, m):
    q = list(copy.copy(p))
    for i in range(len(p) - 4):
        s = p[i:i+5]
        # print(s)
        if s in m:
            q[i+2] = m[s]
        else:
            q[i+2] = '.'
    return ''.join(q)


prev = plant_count(p)
for i in range(500):
    p = next_gen(p, m)
    c = plant_count(p)
    print(i, c, c - prev)
    prev = c

# Hard coded for now
res = 17011 + ((50000000000 - 500) * 34)
print(res)




