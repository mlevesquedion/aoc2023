import re 

import sympy


# From Wikipedia: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersect2d(s1, s2):
    x1, y1, _, dx1, dy1, _ = s1
    x2, y2, _, dx2, dy2, _ = s2
    denom = -dx1*-dy2 - -dy1*-dx2
    top_left_det = (x1*(y1+dy1) - y1*(x1+dx1))
    bot_left_det = (x2*(y2+dy2) - y2*(x2+dx2))
    x = (top_left_det*-dx2 - -dx1*bot_left_det) / denom
    y = (top_left_det*-dy2 - -dy1*bot_left_det) / denom
    return x, y


stones = [[int(x) for x in re.findall(r'-?\d+', line)] for line in open('24.txt')]

min_x = min_y = 200000000000000
max_x = max_y = 400000000000000
count = 0
for i in range(len(stones)):
    for j in range(i+1, len(stones)):
        si, sj = stones[i], stones[j]
        try:
            x, y = intersect2d(si, sj)
            if not (min_x <= x <= max_x and min_y <= y <= max_y):
                continue
            xi, yi, _, dxi, dyi, _ = si
            xj, yj, _, dxj, dyj, _ = sj
            # only keep intersection if it's in the future
            count += all((0 < d1) == (0 < d2) for d1, d2 in ((x - xi, dxi), (x - xj, dxj), (y - yi, dyi), (y - yj, dyj)))
        except ZeroDivisionError:
            continue
assert count == 17244

# Since there is a line going through each stone at times t0, t1, t2, etc.,
# parallel vectors go from stone 0 at t0 to stone 1 at t1, stone 2 at t2, and 
# stone 3 at t3, with different scales.
s = stones
t0, t1, t2, t3, k1, k2 = syms = sympy.symbols("t0 t1 t2 t3 k1 k2")

t = (t0, t1, t2, t3)
p0 = [s[0][i] + t0*s[0][i+3] for i in range(3)]
vectors = [[s[j][i] + t[j]*s[j][i+3] - p0[i] for i in range(3)] for j in range(1, 4)]

k = (k1, k2)
eqs = [sympy.Eq(dim[0]*k[j], dim[1]) for j in range(2) for dim in zip(vectors[0], vectors[j+1])]

t0_, t1_, *_ = sympy.solve(eqs, syms)[0]
norm = [vectors[0][i].subs({t0: t0_, t1: t1_})/(t1_-t0_) for i in range(3)]
start = [p0[i].subs({t0: t0_}) - norm[i] * t0_ for i in range(3)]
assert sum(start) == 1025019997186820
