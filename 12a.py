import collections
import itertools
import helper
import copy

values = helper.load_in_list('input_12.txt', str)

p = values[0].split()[2]
pots = set(i for i, x in enumerate(p) if x == '#')
recipes = set(x for x , y in map(lambda x : x.split(' => '), values[2:]) if y == '#')

def next_gen(pots, recipes):
    new_pots = set()
    for i in range(-5, max(pots) + 4):
        s = ''.join('#' if j + i in pots else '.' for j in range(-2, 3))
        if s in recipes:
            new_pots.add(i)
    return new_pots

def p1(pots, n=20):
    for i in range(n):
        pots = next_gen(pots, recipes)
    print(sum(pots))

def p2(pots):
    prev = sum(pots)
    last_diff = 0
    n = 0
    for i in itertools.count():
        pots = next_gen(pots, recipes)
        c = sum(pots)
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

p1(pots)
p2(pots)
