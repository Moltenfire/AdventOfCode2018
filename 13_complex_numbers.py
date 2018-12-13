import collections
import itertools
import helper
import copy
import numpy as np

dir2chars = {-1j:'^', 1:'>', 1j:'v', -1:'<'}
chars2dir = {'^':-1j, '>':1, 'v':1j, '<':-1}
intersections = [-1j, 1, 1j]

class Cart(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.pos = x + y * 1j
        self.direction = direction
        self.intersection_option = 0
        self.crashed = False

    def move(self):
        self.pos += self.direction

    def check_collision(self, other):
        return self.pos == other.pos

    def turn(self, corner):
        d = 1j if (self.direction.real == 0) == (corner == '/') else -1j
        self.direction *= d

    def intersection(self):
        self.direction *= intersections[self.intersection_option]
        self.intersection_option = (self.intersection_option + 1) % 3

    def __str__(self):
        return "({}, {}) d: {} i: {}".format(self.x, self.y, self.direction, self.intersection_option)

def print_track(track, carts):
    cart_pos = {(c.pos.real, c.pos.imag) : dir2chars[c.direction] for c in carts}
    for y in range(track.shape[1]):
        print(''.join(cart_pos[(x,y)] if (x,y) in cart_pos else c for x, c in enumerate(track[:,y])))

def load_track_carts():
    track = helper.load_grid('input_13.txt')
    carts = []
    for x in range(track.shape[0]):
        for y in range(track.shape[1]):
            c = track[x,y]
            if c in chars2dir:
                d = chars2dir[c]
                carts.append(Cart(x,y,d))
                track[x,y] = '|' if d.real == 0 else '-'
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
            if i != j and not cart2.crashed and cart.check_collision(cart2):
                collisions.append(cart)
                collisions.append(cart2)
                cart.crashed = True
                cart2.crashed = True
                break

        section = track[int(cart.pos.real), int(cart.pos.imag)]
        if section == '\\' or section == '/':
            cart.turn(section)
        elif section == '+':
            cart.intersection()

    return [cart for cart in carts if not cart.crashed], collisions

collisions = []
seen_first_collision = False
while True:
    carts.sort(key=lambda cart : (cart.pos.imag, cart.pos.real))
    carts, new_collisions = tick(track, carts)
    # print_track(track, carts)
    collisions.extend(new_collisions)
    if len(collisions) > 0 and not seen_first_collision:
        seen_first_collision = True
        print("{},{}".format(int(collisions[0].pos.real), int(collisions[0].pos.imag)))
    remaining = len(carts)
    if remaining == 1:
        print("{},{}".format(int(carts[0].pos.real), int(carts[0].pos.imag)))
        break
