import itertools
import functools


backward = forward = 0
for s in ([int(x) for x in line.split()] for line in open('09.txt')):
    seqs = [s]
    while not all(s == 0 for s in seqs[-1]):
        seqs.append([b-a for a, b in itertools.pairwise(seqs[-1])])
    forward += sum(s[-1] for s in seqs)
    backward += functools.reduce(lambda acc, s: s[0] - acc, reversed(seqs), 0)

assert forward == 1901217887
assert backward == 905
