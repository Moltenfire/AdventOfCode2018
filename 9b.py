import collections
import itertools
import helper
import re

players = [9, 10, 13, 17, 21, 30, 493, 493]
count = [25, 1618, 7999, 1104, 6111, 5807, 71863, 71863 * 100]

def game(p, c):
    circle = collections.deque([0])
    current_player = 0
    current_marble = 0
    scores = collections.defaultdict(int)
    for i in range(1, c+1):
        if i % 23 != 0:
            circle.rotate(-1)
            circle.append(i)
        else:
            circle.rotate(7)
            x = circle.pop()
            scores[current_player] += i + x
            circle.rotate(-1)

        current_player = (current_player + 1) % p
    return max(scores.values())

for p, c in zip(players, count):
    res = game(p, c)
    print(p, c, res)
