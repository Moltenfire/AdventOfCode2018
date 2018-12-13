import collections
import itertools
import helper
import copy
import numpy as np

dir_chars = ['^', '>', 'v', '<']
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
intersections = [3, 0, 1]

class Cart(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersection_option = 0
        self.crashed = False

    def move(self):
        self.x += directions[self.direction][0]
        self.y += directions[self.direction][1]

    def check(self, c):
        return self.x == c.x and self.y == c.y

    def turn(self, corner):
        d = 1 if (self.direction % 2 == 0) == (corner == '/') else -1
        self.direction = (self.direction + d) % 4

    def intersection(self):
        self.direction = (self.direction + intersections[self.intersection_option]) % 4
        self.intersection_option = (self.intersection_option + 1) % 3

    def __str__(self):
        return "({}, {}) d: {} i: {}".format(self.x, self.y, self.direction, self.intersection_option)

    def __lt__(self, other):
        return self.x < other.x if self.y == other.y else self.y < other.y

def print_track(track, carts):
    cart_pos = {(c.x, c.y) : dir_chars[c.direction] for c in carts}
    for y in range(track.shape[1]):
        print(''.join(cart_pos[(x,y)] if (x,y) in cart_pos else c for x, c in enumerate(track[:,y])))

def load_track_carts():
    track = helper.load_grid('input_13.txt')
    carts = []
    for x in range(track.shape[0]):
        for y in range(track.shape[1]):
            c = track[x,y]
            if c in dir_chars:
                d = dir_chars.index(c)
                carts.append(Cart(x,y,d))
                track[x,y] = '|' if d % 2 == 0 else '-'
    return track, carts

track, carts = load_track_carts()

# move, collision check, turn
def tick(track, carts):
    collisions = []
    for i, cart in enumerate(carts):
        if cart.crashed:
            continue

        cart.move()

        for j, cart2 in enumerate(carts):
            if i != j and not cart2.crashed and cart.check(cart2):
                collisions.append(cart)
                collisions.append(cart2)
                cart.crashed = True
                cart2.crashed = True
                break

        section = track[cart.x, cart.y]
        if section == '\\' or section == '/':
            cart.turn(section)
        elif section == '+':
            cart.intersection()

    return sorted([cart for cart in carts if not cart.crashed]), collisions

collisions = []
seen_first_collision = False
while True:
    carts, new_collisions = tick(track, carts)
    collisions.extend(new_collisions)
    if len(collisions) > 0 and not seen_first_collision:
        seen_first_collision = True
        print("{},{}".format(collisions[0].x, collisions[0].y))
    remaining = len(carts)
    if remaining == 1:
        print("{},{}".format(carts[0].y, carts[0].x))
        break
