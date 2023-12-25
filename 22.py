import collections
import itertools

lines = [line.strip() for line in open('22.txt')]

bricks = [[[int(x) for x in chunk.split(',')] for chunk in line.split('~')] for line in lines]

max_x, max_y, max_z = map(max, zip(*(p2 for _, p2 in bricks)))

settled = [[[None for _ in range(max_x+1)] for _ in range(max_y+1)] for _ in range(max_z+2)]
for y, x in itertools.product(range(max_y+1), range(max_x+1)):
    settled[0][y][x] = 0 

highest_z = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

for brick_id, ((x1, y1, z1), (x2, y2, z2)) in enumerate(sorted(bricks, key=lambda b: b[0][2]), 1):
    settle_z = max(highest_z[y][x] for y, x in itertools.product(range(y1, y2+1), range(x1, x2+1))) + 1
    for y, x in itertools.product(range(y1, y2+1), range(x1, x2+1)):
        highest_z[y][x] = settle_z + z2-z1
    for z, y, x in itertools.product(range(settle_z, settle_z + z2-z1 + 1), range(y1, y2+1), range(x1, x2+1)): 
       settled[z][y][x] = brick_id

supported_blocks = {i: set() for i in range(1, brick_id+1)}
for z, y, x in itertools.product(range(1, max_z+1), range(max_y+1), range(max_x+1)): 
    if (supporting := settled[z][y][x]) is not None and (supported := settled[z+1][y][x]) is not None and supporting != supported:
        supported_blocks[supporting].add(supported)

supporting_blocks = collections.defaultdict(set)
for supporting, supported in supported_blocks.items():
    for supp in supported:
        supporting_blocks[supp].add(supporting)

disintegratable = 0
would_fall = 0
for supporting, supported in supported_blocks.items():
    falling_blocks = {supp for supp in supported if len(supporting_blocks[supp]) == 1}
    if len(falling_blocks) == 0:
        disintegratable += 1
        continue
    for f in set(falling_blocks):
        Q = supporting_blocks[f]
        while Q:
            supporting = Q.pop()
            for supp in supported_blocks[supporting]:
                if supporting_blocks[supp] - falling_blocks:
                    continue
                falling_blocks.add(supp)
                Q.add(supp)
    would_fall += len(falling_blocks)

assert disintegratable == 509
assert would_fall == 102770
