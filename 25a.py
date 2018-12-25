import collections
import itertools
import helper
import re
import networkx as nx
import matplotlib.pyplot as plt

def get_values():
    return list(map(lambda x : tuple(map(int, re.findall("-?\d+", x))), helper.load_in_list('input_25.txt', str)))

def dist(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])

def main():
    values = get_values()

    G = G=nx.Graph()
    for i, a in enumerate(values):
        for j, b in enumerate(values):
            if b <= a:
                continue
            d = dist(a,b)
            if d <= 3:
                G.add_edge(a, b)
            else:
                G.add_node(a)
                G.add_node(b)

    res = nx.number_connected_components(G)
    print(res)

    # nx.draw(G)
    # plt.show()
        


if __name__ == '__main__':
    main()
