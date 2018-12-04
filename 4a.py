import collections
import itertools
import helper
import re
import operator

values = helper.load_in_list('input_4.txt', str)
values.sort()

guards = collections.defaultdict(int)
guard2 = collections.defaultdict(list)
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
        start = s[4]
        end = x[4]
        time = end - start - 1
        guards[curent_guard] += time
        guard2[curent_guard] += list(range(start, end))

g_id = max(guards.items(), key=operator.itemgetter(1))[0]
minute = collections.Counter(guard2[g_id]).most_common(1)[0][0]
# print(g_id)
# print(minute)
# print(g_id * minute)

for g in guard2:
    minute = collections.Counter(guard2[g]).most_common(1)[0]
    print(g, minute, g * minute[0])