import collections

lines = list(open('05.txt'))

steps = []
i = 3
while i < len(lines):
    mapping = []
    while i < len(lines) and lines[i].strip():
        dst_start, src_start, length = map(int, lines[i].split(' '))
        mapping.append((src_start, src_start + length - 1, dst_start))
        i += 1
    steps.append(mapping)
    i += 2

seeds = [int(x) for x in lines[0].split(' ')[1:]]

values = seeds[:]
for mapping in steps:
    next_values = []
    for v in values:
        for src_start, src_end, dst_start in mapping:
            if src_start <= v <= src_end:
                next_values.append(v - src_start + dst_start)
                break
        else:
            next_values.append(v)
    values = next_values

assert min(values) == 31599214


def map_ranges(value_ranges, mappings):
    value_ranges = collections.deque(sorted(value_ranges))
    mappings = collections.deque(sorted(mappings))

    next_value_ranges = []
    while value_ranges and mappings:
        range_start, range_end = value_range = value_ranges.popleft()
        src_start, src_end, dst_start = mapping = mappings.popleft()

        # if the range is fully before the mapping, keep the range as is
        # and try applying the mapping to the next range
        if range_end < src_start:
            next_value_ranges.append(value_range)
            mappings.appendleft(mapping)
            continue

        # in theory some mappings could be before all ranges, but
        # in practice on my input this doesn't happen
        # if range_start > src_end:
        #     value_ranges.appendleft(vr)
        #     continue

        # in theory some part of the range could be before the mapping, but
        # in practice on my input this doesn't happen
        # before = (range_start, min(src_start-1, range_end))
        # if before[0] <= before[1]:
        #     next_value_ranges.append(before)

        overlap = (max(range_start, src_start), min(range_end, src_end))
        if overlap[0] <= overlap[1]:
            next_range_start = dst_start + (overlap[0]-src_start)
            next_value_ranges.append((next_range_start, next_range_start + (overlap[1]-overlap[0])))
            if overlap[1] < src_end:
                mappings.appendleft((overlap[1], src_end, dst_start + (overlap[1]-src_start)))

        after = (max(src_end+1, range_start), range_end)
        if after[0] <= after[1]:
            value_ranges.appendleft(after)

    # in theory there could be some ranges left that are after the mappings, but
    # in practice on my input this doesn't happen
    # if value_ranges and not mapping:
    #     next_value_ranges += list(value_ranges)

    return next_value_ranges


value_ranges = [(start, start+length-1) for start, length in zip(seeds[::2], seeds[1::2])]
for mapping in steps:
    value_ranges = map_ranges(value_ranges, mapping)

assert min(value_ranges)[0] == 20358599
