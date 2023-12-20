import itertools
import math


def make_func(cases):
    def f(part):
        for case in cases:
            if ':' in case:
                cond, dest = case.split(':')
                if eval(cond, dict(part)):
                    return dest
            else:
                return case
    return f


text = open('19.txt').read()

workflows, parts = text.split('\n\n')
workflow_lines = workflows.split('\n')
part_lines = parts.split('\n')

workflows = {}
for line in workflow_lines:
    name_end = line.index('{')
    name = line[:name_end]
    line = line[name_end+1:-1]
    workflows[name] = line.split(',')

workflow_funcs = {name: make_func(cases) for name, cases in workflows.items()}

parts = [eval('dict('+line[1:-1]+')') for line in part_lines]

result = 0
for p in parts:
    w = 'in'
    while w not in 'AR':
        w = workflow_funcs[w](p)
    if w == 'A':
        result += sum(p.values())
assert result == 432434


def combinations(ranges, name):
    if name == 'A':
        return math.prod((b-a+1) for a, b in ranges.values())
    if name == 'R':
        return 0
    total = 0
    for case in workflows[name]:
        if ':' not in case:
            total += combinations(ranges, case)
            continue
        cond, dest = case.split(':')
        target, sign, *number = cond
        number = int(''.join(number))
        match, non_match = dict(ranges), dict(ranges)
        a, b = ranges[target]
        match[target] = (a if sign == '<' else number+1, b if sign == '>' else number-1)
        non_match[target] = (number if sign == '<' else a, number if sign == '>' else b)
        total += combinations(match, dest)
        ranges = non_match
    return total


ranges = dict(zip('xmas', itertools.repeat((1, 4000))))
assert combinations(ranges, 'in') == 132557544578569
