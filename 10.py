grid = [list(line.strip()) for line in open('10.txt')]

start = None
for i, line in enumerate(grid):
    for j, val in enumerate(line):
        if val == 'S':
            start = (i, j)
            has_above = i-1 >= 0 and grid[i-1][j] in '|7F'
            has_below = i+1 < len(grid) and grid[i+1][j] in '|JL'
            has_left = j-1 >= 0 and grid[i][j-1] in '-LF'
            has_right = i+1 < len(grid[0]) and grid[i][j+1] in '-J7'
            grid[i][j] = {
                    has_above and has_left: 'J',
                    has_above and has_right: 'L',
                    has_below and has_left: '7',
                    has_below and has_right: 'F',
            }[True]
assert start is not None

distance = 0
i, j = start
di, dj = (0, -1) if grid[start[0]][start[1]] in 'FL' else (0, 1)
loop = {start}
while True:
    distance += 1
    if grid[i][j] in 'L7':
        di, dj = dj, di
    elif grid[i][j] in 'JF':
        di, dj = -dj, -di
    i, j = i+di, j+dj
    loop.add((i, j))
    if (i, j) == start:
        break

assert distance//2 == 6838


in_tiles = 0
for i, line in enumerate(grid):
    inside = False
    for j, val in enumerate(line):
        if (i, j) not in loop:
            in_tiles += inside
        elif val in '|JL':
            inside = not inside

assert in_tiles == 451
