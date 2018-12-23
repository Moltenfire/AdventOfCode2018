import collections
import itertools
import helper
import re
import math

file = "23.txt"
# file = "input_23.txt"

values = list(map(lambda x : list(map(int, re.findall("-?\d+", x))), helper.load_in_list(file, str)))#

def calc_dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def mid(a, b, r1, r2):
    ratio1 = r2/(r1+r2)
    ratio2 = r1/(r1+r2)
    return (
        int((a[0] * ratio1 + b[0] * ratio2)),
        int((a[1] * ratio1 + b[1] * ratio2)),
        int((a[2] * ratio1 + b[2] * ratio2)))

def in_range(p, c):
    return len([0 for q, r in c.items() if calc_dist(p, q) <= r])

def get_most_near(minx, maxx, miny, maxy, minz, maxz, c, dist):
    most_near = 0
    most_near_points = []
    for x in range(minx, maxx+1, dist):
        for y in range(miny, maxy+1, dist):
            for z in range(minz, maxz+1, dist):
                p = (x,y,z)
                i = len([0 for q, r in c.items() if calc_dist(p, q) <= (r + dist)])
                if i > most_near:
                    most_near = i
                    most_near_points = [p]
                elif i == most_near:
                    most_near_points.append(p)

    return most_near, most_near_points


def func(minx, maxx, miny, maxy, minz, maxz, c, dist):
    
    while True:
        most_near, most_near_points = get_most_near(minx, maxx, miny, maxy, minz, maxz, c, dist)

        # print(most_near)
        # print(most_near_points)
        # print(dist)

        if dist == 1:
            p = most_near_points[0]
            # print(p)
            # print(calc_dist((0,0,0), p))
            return { p : in_range(p,c) for p in most_near_points }

        possible = {}
        for p in most_near_points:
            
            ndist = int(dist / 2)
            minx = p[0] - dist
            maxx = p[0] + dist
            miny = p[1] - dist
            maxy = p[1] + dist
            minz = p[2] - dist
            maxz = p[2] + dist

            res = func(minx, maxx, miny, maxy, minz, maxz, c, ndist)
            for p, n in res.items():
                possible[p] = n

        return possible
        # print()

c = { (x,y,z) : r for x,y,z,r in values }

minx = min(x for x, y, z in c)
maxx = max(x for x, y, z in c)
miny = min(y for x, y, z in c)
maxy = max(y for x, y, z in c)
minz = min(z for x, y, z in c)
maxz = max(z for x, y, z in c)

max_dimension = max(abs(maxx - minx), abs(maxy - minz), abs(maxz - minz))
print((abs(maxx - minx), abs(maxy - minz), abs(maxz - minz)))


# print(max_dimension)
dist = 2**int(math.log(max_dimension, 2))

res = func(minx, maxx, miny, maxy, minz, maxz, c, dist)

most = max(res.values())
# print(most)

origin = (0,0,0)
points_dist = {p : calc_dist(p, origin) for p in res if res[p] == most}
print(points_dist)
