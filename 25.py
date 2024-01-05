import collections
import random
import re

lines = [line.strip() for line in open('25.txt')]


def canonical_edge(src, dst):
    return tuple(sorted((src, dst)))


G = collections.defaultdict(set)
VALID_EDGES = set()
for line in lines:
    parts = re.findall(r'\w+', line)
    src, *dsts = parts
    for dst in dsts:
        G[src].add(dst)
        G[dst].add(src)
        VALID_EDGES.add(canonical_edge(src, dst))

# Pick two nodes at random and try to find a shortest path between them 4 times
# in a row, while using different edges each time. This is only possible if the
# nodes are in different components.
nodes = list(G)
while True:
    valid_edges = set(VALID_EDGES)
    src, dst = random.sample(nodes, 2)
    for _ in range(4):
        parent = {}
        Q = [src]
        for node in Q:
            if node == dst:
                while node != src:
                    prev_node = parent[node]
                    valid_edges.remove(canonical_edge(node, prev_node))
                    node = prev_node
                break
            for next_node in G[node]:
                if canonical_edge(node, next_node) not in valid_edges or next_node in parent:
                    continue
                parent[next_node] = node
                Q.append(next_node)
        else:
            print(len(parent)*(len(G)-len(parent)))
            exit(0)
