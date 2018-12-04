import collections
import itertools
import helper
import re
import operator

values = helper.load_in_list('input_4.txt', str)
values.sort()

guards = collections.defaultdict(int)
curent_guard = None
s = None
for v in values:
    x = list(map(int, re.findall('\d+', v)))
    l = v[19]
    if l == "G":
        curent_guard = x[-1]
    elif l == "f":
        s = x
    elif l == "w":
        start = 60*s[3] + s[4]
        end = 60*x[3] + x[4]
        time = end - start - 1
        guards[curent_guard] += time

res = max(guards.items(), key=operator.itemgetter(1))[0]
print(res)