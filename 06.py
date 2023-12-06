import math


def ways_to_beat(best_distance, total_time):
    # The distance for a given charge time is equal to:
    # (total_time - charge_time) * charge_time
    # This is a quadratic function, so there is some point where we charge 
    # enough to beat the best distance, and some later point where we charged 
    # for too long. To find those points, subtract the distance and solve:
    # -1 * charge_time^2 + total_time * charge_time - best_distance
    a, b, c = -1, total_time, -best_distance
    sqrt = (b*b - 4*a*c)**0.5
    min_time, max_time = [int((-b+x)/(2*a)) for x in (sqrt, -sqrt)]
    return max_time - min_time


lines = list(open('06.txt'))

time_strings = lines[0].split()[1:]
dist_strings = lines[1].split()[1:]

times = [int(x) for x in time_strings]
dists = [int(x) for x in dist_strings]

assert math.prod(ways_to_beat(d, t) for t, d in zip(times, dists)) == 2269432

time = int(''.join(time_strings))
dist = int(''.join(dist_strings))

assert ways_to_beat(dist, time) == 35865985
