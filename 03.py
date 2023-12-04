import collections
import itertools
import math


def neighbors(grid, i, j):
    for ni, nj in itertools.product((i-1, i, i+1), (j-1, j, j+1)):
        if ni == i and nj == j:
            continue
        if not 0 <= ni < len(grid) or not 0 <= nj < len(grid[0]):
            continue
        yield (ni, nj)


SYMBOLS = set('#$%&*+-/=@')
def has_nearby_symbol(grid, i, j):
    return any(grid[ni][nj] in SYMBOLS for ni, nj in neighbors(grid, i, j))


def star_neighbor(grid, i, j):
    for ni, nj in neighbors(grid, i, j):
        if grid[ni][nj] == '*':
            return (ni, nj)


grid = list(open('03.txt'))

part_number_sum = 0
star_numbers = collections.defaultdict(list)
for i, row in enumerate(grid):
    number = is_part = star = 0
    for j, value in enumerate(row):
        if not value.isdigit():
            if is_part:
                part_number_sum += number
            if star and number:
                star_numbers[star].append(number)
            number = is_part = star = 0
            continue
        number = number*10 + int(value)
        is_part = is_part or has_nearby_symbol(grid, i, j)
        star = star or star_neighbor(grid, i, j)
gear_ratio_sum = sum(math.prod(numbers) for numbers in star_numbers.values() if len(numbers) == 2)

assert part_number_sum == 546563
assert gear_ratio_sum == 91031374
