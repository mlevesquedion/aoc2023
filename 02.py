import collections
import math
import re


MAX_COUNT = dict(zip('red green blue'.split(), range(12, 15)))

count_color_re = re.compile(r'(\d+) (red|green|blue)')

p1_total = p2_total = 0
for game_id, line in enumerate(open('02.txt'), 1):
    color_counts = [(color, int(count)) for count, color in count_color_re.findall(line)]
    possible = True
    min_needed = collections.defaultdict(int)
    for color, count in color_counts:
        min_needed[color] = max(min_needed[color], count)
        if count > MAX_COUNT[color]:
            possible = False
    p2_total += math.prod(min_needed.values())
    if possible:
        p1_total += game_id

assert p1_total == 2528
assert p2_total == 67363
