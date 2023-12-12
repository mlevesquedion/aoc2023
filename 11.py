import collections

grid = [line.strip() for line in open('11.txt')]

galaxies = set()
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == '#':
            galaxies.add((i, j))

expanded_rows = set()
for i, row in enumerate(grid):
    if len(set(row)) == 1:
        expanded_rows.add(i)

expanded_cols = set()
for j, col in enumerate(zip(*grid)):
    if len(set(col)) == 1:
        expanded_cols.add(j)

galaxies_by_row = collections.Counter((g[0] for g in galaxies))
galaxies_by_col = collections.Counter((g[1] for g in galaxies))


def slicewise_cost(slice_count, galaxies_by_slice, expanded_slices, expanded_cost):
    total_cost = 0
    running_galaxies = running_cost = 0
    for i in range(slice_count):
        running_cost += (expanded_cost if i in expanded_slices else 1) * running_galaxies
        total_cost += running_cost * galaxies_by_slice[i]
        running_galaxies += galaxies_by_slice[i]
    return total_cost


def cost(expanded_cost):
    row_cost = slicewise_cost(len(grid), galaxies_by_row, expanded_rows, expanded_cost)
    col_cost = slicewise_cost(len(grid[0]), galaxies_by_col, expanded_cols, expanded_cost)
    return row_cost + col_cost


assert cost(2) == 10165598
assert cost(1_000_000) == 678728808158
