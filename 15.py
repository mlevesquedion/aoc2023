data = open('15.txt').read().rstrip()


def HASH(step):
    value = 0
    for c in step:
        value += ord(c)
        value *= 17
        value %= 256
    return value

assert sum(HASH(step) for step in data.split(',')) == 495972


class Node:

    def __init__(self, val=None, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_


class HASHMAP:

    def __init__(self):
        self.start = self.last = Node()
        self.hash = {}

    def __setitem__(self, label, val):
        if label in self.hash:
            self.hash[label].val = val
            return
        n = Node(val, self.last)
        self.last.next = n
        self.last = n 
        self.hash[label] = n

    def __delitem__(self, label):
        if label not in self.hash:
            return
        n = self.hash[label]
        self.hash.pop(label)
        if n == self.last:
            self.last = n.prev
            n.prev.next = None
            return
        n.prev.next, n.next.prev = n.next, n.prev

    def __iter__(self):
        n = self.start.next
        while n != None:
            yield n.val
            n = n.next


boxes = [HASHMAP() for _ in range(256)]
for d in data.split(','):
    label, f = d.replace('-', '=').split('=')
    h = HASH(label)
    if not f:
        del boxes[h][label]
        continue
    boxes[h][label] = f

assert sum(sum(i*j*int(f) for j, f in enumerate(box, 1)) for i, box in enumerate(boxes, 1)) == 245223
