import numpy as np

def load_in_list(file, t=int):
    with open(file, 'r') as f:
        return list(map(lambda x : t(x.strip()), f.readlines()))

def load_grid(file):
    with open(file, 'r') as f:
        values = list(map(lambda x : str(x).replace('\n',''), f.readlines()))
        width = len(values[0])
        height = len(values)
        grid = np.zeros((width, height), dtype=str)
        for i, line in enumerate(values):
            for j, c in enumerate(line):
                grid[j,i] = c
        return grid
