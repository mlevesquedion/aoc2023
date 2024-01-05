import collections

lines = [line.strip() for line in open('23.txt')]

start_row, start_col = start = (0, 1)

end_row, end_col = end = (len(lines)-1, len(lines[0])-2)
nodes = {start, end}
for row, line in enumerate(lines):
    for col, val in enumerate(line):
        if not (1 <= row < len(lines) - 1 and 1 <= col < len(lines) - 1) or lines[row][col] != '.':
            continue
        if sum(lines[nr][nc] in '^>v<' for nr, nc in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]) >= 3:
            nodes.add((row, col))

dag = collections.defaultdict(dict)
graph = collections.defaultdict(dict)
for node in nodes:
    if node == end:
        continue
    Q = []
    visited = {node}
    r, c = node
    for nr, nc, direction in [(r-1, c, '^'), (r, c+1, '>'), (r+1, c, 'v'), (r, c-1, '<')]:
        if not 0 <= nr < len(lines) or not 0 <= nc < len(lines[0]) or lines[nr][nc] == '#':
            continue
        Q.append((nr, nc, lines[nr][nc] in direction + '.'))
        visited.add((nr, nc))
    steps = 0
    while Q:
        next_Q = []
        for r, c, dag_legal in Q:
            if (r, c) in nodes:
                graph[node][(r, c)] = steps + 1
                if dag_legal:
                    dag[node][(r, c)] = steps + 1
                continue
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if not 0 <= nr < len(lines) or not 0 <= nc < len(lines[0]) or lines[nr][nc] == '#' or (nr, nc) in visited:
                    continue
                next_Q.append((nr, nc, dag_legal))
                visited.add((nr, nc))
        steps += 1
        Q = next_Q


def solve(G):
    nodes = set()
    for src, dsts in G.items():
        nodes.add(src)
        nodes |= set(dsts)
    node_ids = {node: i for i, node in enumerate(nodes)}
    G = {node_ids[src]: {node_ids[dst]: distance for dst, distance in dsts.items()} for src, dsts in G.items()}
    paths = [(node_ids[start], 1<<node_ids[start], 0)]
    max_steps = 0
    for (src, visited, steps) in paths:
        if src == node_ids[end]:
            max_steps = max(steps, max_steps)
            continue
        for dst in G[src]:
            if 1<<dst & visited:
                continue
            paths.append((dst, visited | 1<<dst, steps + G[src][dst]))
    return max_steps


# This is completely excessive since part 1 terminates quickly even with a brute 
# force approach, but I didn't know this algorithm so I wanted to implement it.
def solve_dag(G):
    Gt = collections.defaultdict(dict)
    for src, dsts in G.items():
        for dst, dist in dsts.items():
            Gt[dst][src] = dist

    indegree = {src: len(dsts) for src, dsts in Gt.items()}
    indegree[start] = 0
    todo = [src for src, d in indegree.items() if d == 0]
    distance = {start: 0}

    for node in todo:
        if node != start:
            distance[node] = max(distance[src] + cost for src, cost in Gt[node].items())
        for dst in G[node]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                todo.append(dst)
    return distance[end]


assert solve_dag(dag) == 2254
assert solve(graph) == 6394
