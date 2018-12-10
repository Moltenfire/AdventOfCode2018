import collections
import itertools
import helper
import re
import matplotlib.pyplot as plt

values = helper.load_in_list('input_10.txt', str)
values = list(map(lambda x : list(map(int, re.findall("-?\d+", x))), helper.load_in_list('input_10.txt', str)))

points = []
velocities = []
for x,y,i,j in values:
    points.append([x,y])
    velocities.append((i,j))

def max_dist(p):
    minx = min(x for x, y in points)
    maxx = max(x for x, y in points)
    miny = min(y for x, y in points)
    maxy = max(y for x, y in points)
    return abs(maxx - minx) + abs(maxy - miny)

def forwards(p):
    for i in range(len(p)):
        p[i][0] += velocities[i][0]
        p[i][1] += velocities[i][1]
    return p

def backwards(p):
    for i in range(len(p)):
        p[i][0] -= velocities[i][0]
        p[i][1] -= velocities[i][1]
    return p

def get_message(p):
    last_dist = max_dist(p)
    i = 0
    while True:
        p = forwards(p)
        new_d = max_dist(p)
        if new_d > last_dist:
            return backwards(p), i
        i += 1
        last_dist = new_d

def plot_message(points):
    x, y = zip(*[(x,-y) for x, y in points])
    plt.scatter(x, y)
    plt.show()

res, i = get_message(points)
print(i)
plot_message(res)