import collections
import itertools
import helper
import copy

values = helper.load_in_list('input_12.txt', str)

p = values[0].split()[2]
m = { x : y for x , y in map(lambda x : x.split(' => '), values[2:])}

p = '.' * 5 + p + '.' * 2000

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
        if s in m:
            q[i+2] = m[s]
        else:
            q[i+2] = '.'
    return ''.join(q)

def p1(p):
    for i in range(20):
        p = next_gen(p, m)
    print(plant_count(p))

def p2(p):
    prev = plant_count(p)
    last_diff = 0
    n = 0
    for i in itertools.count():
        p = next_gen(p, m)
        c = plant_count(p)
        diff = c - prev
        if diff == last_diff:
            if n > 5:
                res = c + ((50000000000 - i + 1) * diff)
                print(res)
                break
            n += 1
        else:
            last_diff = diff
            n = 0
        prev = c

p1(p)
p2(p)




