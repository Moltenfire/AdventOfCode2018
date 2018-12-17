import collections
import itertools
import helper
import re

def setup():
    lines = helper.load_in_list('input_17.txt', str)
    clay = set()
    for line in lines:
        v = list(map(int, re.findall("-?\d+", line)))
        if line[0] == 'y':
            for x in range(v[1],v[2]+1):
                clay.add((x,v[0]))
        else:
            for y in range(v[1],v[2]+1):
                clay.add((v[0],y))
    return clay

def print_clay(clay, still_water, moving_water):
    min_x = min(clay, key=lambda x : x[0])[0] - 1
    max_x = max(clay, key=lambda x : x[0])[0] + 1
    min_y = 0
    max_y = max(clay, key=lambda x : x[1])[1] + 1

    print()
    for y in range(max_y + 1):
        a = []
        for x in range(min_x, max_x+1):
            p = (x,y)
            if p in clay:
                a.append('#')
            elif p == spring:
                a.append('+')
            elif p in still_water:
                a.append('~')
            elif p in moving_water:
                a.append('|')
            else:
                a.append('.')
        print(''.join(a))

def fall(p, max_y, clay, moving_water):
    x = p[0]
    # Add all points down to moving water until we hit clay
    # Return the last moving water point
    # If we reach max_y the return None
    for y in range(p[1]+1, max_y + 1):
        new_point = (x,y)
        if new_point not in clay:
            moving_water.add(new_point)
        else:
            return (x,y-1)
    return None

def spread(p, clay, still_water, moving_water):
    # Find points to the left & right
    # End points are None if clay blocks water else 
    end_point_l, spl = spead_left(p, clay, still_water)
    end_point_r, spr = spead_right(p, clay, still_water)
    # If both are clay all the water is still
    # Otherwise it is moving and the 1 or 2 points will be falling 
    if not end_point_l and not end_point_r:
        still_water.update(spl)
        still_water.update(spr)
    else:
        moving_water.update(spl)
        moving_water.update(spr)
    return end_point_l, end_point_r

def spead_left(p, clay, still_water):
    return spread_side(p, clay, still_water, False)

def spead_right(p, clay, still_water):
    return spread_side(p, clay, still_water, True)

def spread_side(p, clay, still_water, right):
    spread_points = set()
    while p not in clay:
        spread_points.add(p)
        pd = (p[0], p[1] + 1)
        if pd not in clay and pd not in still_water:
            return p, spread_points
        if right:
            p = (p[0] + 1, p[1])
        else:
            p = (p[0] - 1, p[1])
    return None, spread_points

def tick(clay, max_y, still_water, moving_water, falling, spreading):
    for f in falling:
        # print_clay(clay, still_water, moving_water)
        p = fall(f, max_y, clay, moving_water)
        if p:
            spreading.add(p)
    falling.clear()

    while spreading:
        # print_clay(clay, still_water, moving_water)
        s = spreading.pop()
        pl, pr = spread(s, clay, still_water, moving_water)
        # If both points are clay (None) spread from point above
        # Otherwise fall from the none clay points
        if not pr and not pl:
            spreading.add((s[0], s[1]-1))
        else:
            if pl:
                falling.add(pl)
            if pr:
                falling.add(pr)

def main():
    clay = setup()
    max_y = max(clay, key=lambda x : x[1])[1]
    spring = (500, 0)
    still_water = set()
    moving_water = set()
    falling = set([spring])
    spreading = set()

    while True:
        tick(clay, max_y, still_water, moving_water, falling, spreading)
        if not falling and not spreading:
            break

    total = len([p for p in moving_water.union(still_water) if p[1] < max_y])
    print(total)
    total = len([p for p in still_water if p[1] < max_y])
    print(total)

if __name__ == '__main__':
    main()
