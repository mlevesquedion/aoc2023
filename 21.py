import numpy as np

lines = [line.rstrip() for line in open('21.txt')]

width = len(lines)
half_width = width//2
start = (start_row, start_col) = (half_width, half_width)

Q = {start}
for i in range(64):
    next_Q = set()
    for row, col in Q:
        for next_row, next_col in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
            if 0 <= next_row < len(lines) and 0 <= next_col < len(lines[0]) and lines[next_row][next_col] != '#':
                next_Q.add((next_row, next_col))
    Q = next_Q
assert len(Q) == 3646

Q = {start}
ys = []
for i in range(half_width + width*2 + 1):
    if (i - half_width) % width == 0:
        ys.append(len(Q))
    next_Q = set()
    for row, col in Q:
        for next_row, next_col in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
            if lines[next_row%len(lines)][next_col%len(lines[0])] != '#':
                next_Q.add((next_row, next_col))
    Q = next_Q

a, b, c = map(round, np.polyfit(range(len(ys)), ys, 2))
x = (26501365 - half_width) // width
assert a*x**2 + b*x + c == 606188414811259
