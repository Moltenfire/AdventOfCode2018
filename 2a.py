import collections
import itertools
import helper

values = helper.load_in_list('input_3.txt', str)

two = 0
three = 0

for s in values:
    counter = collections.Counter(s)
    times = set(counter.values())
    if 2 in times:
        two += 1
    if 3 in times:
        three += 1

print(two * three)