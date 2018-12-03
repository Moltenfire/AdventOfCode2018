import collections
import itertools
import helper

values = helper.load_in_list('input_2.txt', str)

str_len = 26

def check_if_common(s1, s2):
    if s1 == s2:
        return
    diff = 0
    index = 0
    for i in range(str_len):
        if s1[i] != s2[i]:
            diff += 1
            index = i
    if diff == 1:
        print(s1[:index] + s1[index+1:])

for i, s1 in enumerate(values):
    for s2 in values[i:]:
        check_if_common(s1, s2)