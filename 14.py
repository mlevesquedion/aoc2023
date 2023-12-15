def reversed_rows(grid):
    return [''.join(reversed(row)) for row in grid]


def cols(grid):
    return [''.join(col) for col in zip(*grid)]


def reversed_cols(grid):
    return [''.join(reversed(col)) for col in cols(grid)]


def move(rows):
    return ['#'.join(''.join(sorted(chunk, reverse=True)) for chunk in row.split('#')) for row in rows]


def north_load(grid):
    return sum((len(grid) - i) * row.count('O') for i, row in enumerate(grid))


def run_cycle(grid):
    grid = cols(move(cols(grid)))
    grid = move(grid)
    grid = list(reversed(cols(move(reversed_cols(grid)))))
    grid = reversed_rows(move(reversed_rows(grid)))
    return grid


def hashable(grid):
    return '\n'.join(map(''.join, grid))


grid = [list(line.strip()) for line in open('14.txt')]

assert north_load(cols(move(cols(grid)))) == 109833

seen = {}
i = 0
while True:
    seen[hashable(grid)] = i
    grid = run_cycle(grid)
    i += 1
    if hashable(grid) in seen:
        first = seen[hashable(grid)]
        period = i - first
        break

target = (1_000_000_000 - first) % period + first
assert north_load(list(seen)[target].splitlines()) == 99875
