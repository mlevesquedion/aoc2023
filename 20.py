import collections
import itertools
import math

lines = [line.strip() for line in open('20.txt').readlines()]

destinations = {}
flipflops = {}
inputs = collections.defaultdict(dict)

for line in lines:
    module, outputs = line.split(' -> ')
    outputs = outputs.split(', ')
    name = module
    if module[0] in '%&':
        name = module[1:]
        if module[0] == '%':
            flipflops[name] = 0
    for d in outputs:
        inputs[d][name] = 0
    destinations[name] = outputs

destinations['button'] = ['broadcaster']

# I used graphviz to render the graph and observed that there are 4 independent
# substructures each of which has a conjunction with many inputs that outputs to 
# another conjunction which outputs to rx.
cycles = {d: 0 for d, i in inputs.items() if len(i) > 5}

counts = collections.Counter()
for i in itertools.count():
    if i == 1000:
        # part 1
        assert counts[0] * counts[1] == 666795063
    pulses = [('button', 0, 'broadcaster')]
    for src, pulse, dst in pulses:
        if not pulse and src in cycles and not cycles[src]:
            cycles[src] = i + 1
            if all(cycles.values()):
                # part 2
                assert math.lcm(*cycles.values()) == 253302889093151
                exit(0)
        counts[pulse] += 1
        if dst not in destinations:
            continue
        if dst == 'broadcaster':
            next_pulse = 0
        elif dst in flipflops:
            if pulse == 0:
                next_pulse = flipflops[dst] = 1 - flipflops[dst]
            else:
                continue
        else:
            inputs[dst][src] = pulse
            next_pulse = not all(inputs[dst].values())
        pulses += [(dst, next_pulse, next_dst) for next_dst in destinations[dst]]
