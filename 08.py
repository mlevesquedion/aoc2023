import math
import re

lines = list(open('08.txt'))

instructions = lines[0].strip()

graph = {}
for line in lines[2:]:
    src, left, right = re.findall(r'[0-9A-Z]{3}', line)
    graph[src] = (left, right)

node = 'AAA'
i = 0
while node != 'ZZZ':
    node = graph[node][instructions[i%len(instructions)] == 'R']
    i += 1
assert i == 18727

nodes = [n for n in graph if n[2] == 'A']
period = [0 for _ in range(len(nodes))]
i = 0
remaining = len(nodes)
while remaining > 0:
    follow = instructions[i%len(instructions)] == 'R'
    nodes = [graph[n][follow] for n in nodes]
    i += 1
    for j, n in enumerate(nodes):
        if n[2] == 'Z':
            period[j] = i 
            remaining -= 1
assert math.lcm(*period) == 18024643846273
