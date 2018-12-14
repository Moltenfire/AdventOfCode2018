import collections
import itertools
import helper
import re

def num2list(x):
    return  [int(i) for i in str(x)]

def sim(n):
    recipes = num2list(37)
    p1 = 0
    p2 = 1
    while len(recipes) < n + 10:
        r1 = recipes[p1]
        r2 = recipes[p2]
        new = r1 + r2
        recipes.extend(num2list(new))
        p1 = (p1 + r1 + 1) % len(recipes)
        p2 = (p2 + r2 + 1) % len(recipes)
    print(''.join([str(i) for i in recipes[n:n+10]]))

def sim2(n):
    recipes = num2list(37)
    p1 = 0
    p2 = 1
    search = num2list(n)
    while True:
        r1 = recipes[p1]
        r2 = recipes[p2]
        new = r1 + r2
        recipes.extend(num2list(new))
        p1 = (p1 + r1 + 1) % len(recipes)
        p2 = (p2 + r2 + 1) % len(recipes)
        
        if search == recipes[-len(search):]:
            print(len(recipes) - len(search))
            break
        elif search == recipes[-len(search)-1:-1]:
            print(len(recipes) - len(search) - 1)
            break

sim1(894501)
sim2(894501)
