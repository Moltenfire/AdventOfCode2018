import collections
import itertools
import helper
import re

values = helper.load_in_list('input_4.txt', str)
values.sort()

sleep_time = collections.defaultdict(int)
mins_sleep = collections.defaultdict(list)
g_id = None
start = None
for v in values:
    x = list(map(int, re.findall('\d+', v)))
    if "Guard" in v:
        g_id = x[-1]
    elif "falls" in v:
        start = x[4]
    elif "wakes" in v:
        end = x[4]
        time = end - start - 1
        sleep_time[g_id] += time
        mins_sleep[g_id] += list(range(start, end))

mins_sleep_counter = {g_id : collections.Counter(mins_sleep[g_id]).most_common(1)[0] for g_id in mins_sleep}

g_id = max(sleep_time.items(), key=lambda x : x[1])[0]
minute = mins_sleep_counter[g_id][0]
print(g_id * minute)

g_id = max(mins_sleep_counter.items(), key=lambda x : x[1][1])[0]
minute = mins_sleep_counter[g_id][0]
print(g_id * minute)
