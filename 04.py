import re

number_re = re.compile(r'\d+')

points = 0
lines = list(open('04.txt'))
counts = [1 for _ in lines]
for i, line in enumerate(lines):
    winning, got = [number_re.findall(part) for part in line[line.index(':')+1:].split('|')]
    worth_points = set(winning) & set(got)
    for j in range(len(worth_points)):
        counts[i+1+j] += counts[i]
    if worth_points:
        points += 2**(len(worth_points)-1)

assert points == 20407
assert sum(counts) == 23806951
