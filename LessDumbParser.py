import networkx as nx
import numpy as np


def parse_input(filename):
    with open(filename, 'r') as f:
        setup = {k: int(i) for k, i in zip('DISVF', f.readline().rstrip().split())}
        edges, paths = [], []
        for line in f:
            line = line.rstrip().split()
            if all([s.isnumeric() for s in line[:2]]):
                snode, enode, street_name, L = int(line[0]), int(line[1]), line[2], int(line[3])
                snode, enode, L = int(snode), int(enode), int(L)
                edges.append([snode, enode, {'name': street_name, 'length': L}])

            else:
                paths.append((int(line[0]), line[1:]))

        print('total simulation time: {}\n')
    return nx.DiGraph(edges), paths, setup