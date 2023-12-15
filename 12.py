import functools
import itertools


@functools.cache
def count(record, groups, in_group=False):
    if not record:
        return not groups
    if not groups:
        return '#' not in record
    if record[0] == '#':
        if groups[0] < 0:
            return 0
        return count(record[1:], tuple([groups[0]-1] + list(groups[1:])), True)
    if record[0] == '.':
        if in_group:
            if groups[0] != 0:
                return 0
            return count(record[1:], tuple(groups[1:]))
        return count(record[1:], groups)
    if record[0] == '?':
        return count('.' + record[1:], groups, in_group) + count('#' + record[1:], groups, in_group)
    assert False


lines = list(open('12.txt'))

rg = [(record+'.', tuple(int(x) for x in groups.split(','))) for line in lines for (record, groups) in [line.split()]]

assert sum(itertools.starmap(count, rg)) == 7084

rg = [('?'.join([record]*5)+'.', tuple(int(x) for x in ','.join([groups]*5).split(','))) for line in lines for (record, groups) in [line.split()]]

assert sum(itertools.starmap(lambda r, g: count.cache_clear() or count(r, g), rg)) == 8414003326821
