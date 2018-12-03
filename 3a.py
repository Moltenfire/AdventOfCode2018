import collections
import itertools
import helper
import re

values = list(map(lambda x : list(map(int, re.findall('\d+', x))), helper.load_in_list('input_3.txt', str)))

claims = []
for v in values:
    for i in range(v[1], v[1] + v[3]):
        for j in range(v[2], v[2] + v[4]):
            claims.append((i, j)) 

cc = collections.Counter(claims)

total = 0
single_claim = []
for key, value in cc.items():
    if value > 1:
        total += 1

print(total)

for v in values:
    claimed = False
    for i in range(v[1], v[1] + v[3]):
        for j in range(v[2], v[2] + v[4]):
            if cc[(i, j)] > 1:
                claimed = True

    if not claimed:
        print(v[0])
