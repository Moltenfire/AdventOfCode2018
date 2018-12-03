import itertools
import helper

values = helper.load_in_list('input_1.txt')

freq = 0
freq_reached = set([freq])
for f in itertools.cycle(values):
    freq += f
    if freq in freq_reached:
        print(freq)
        break
    freq_reached.add(freq)
