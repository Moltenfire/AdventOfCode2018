import collections
import itertools
import helper
import re

s = helper.load_in_list('input_8.txt', str)[0]
# s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
v = list(map(int, s.split()))

def parse_node(x):
    c = x[0]
    m = x[1]
    data = x[2:]
    totals = 0
    values = []
    for i in range(c):
        total, data, value= parse_node(data)
        totals += total
        values.append(value)

    meta_data = data[:m]
    totals += sum(meta_data)

    if c == 0:
        value = sum(meta_data)
    else:
        value = 0
        for i in meta_data:
            if i > 0 and i <= len(values):
                value += values[i-1]

    return totals, data[m:], value

res = parse_node(v)
print(res[0])
print(res[2])

