import heapq

lines = [line.strip() for line in open('17.txt')]

UP, RIGHT, DOWN, LEFT = range(4)


def minimum_heat_loss(lines, min_straight, max_straight):
    Q = [(0, 0, 0, DOWN, 1), (0, 0, 0, RIGHT, 1)]
    visited = {(0, 0, DOWN, 1), (0, 0, RIGHT, 1)}

    while Q:
        cost, row, col, direction, straight = heapq.heappop(Q)

        if (row, col) == (len(lines)-1, len(lines[0])-1):
            if straight < min_straight + 1:
                continue
            return cost

        directions = []
        if straight >= min_straight:
            directions = [(direction-1)%4, (direction+1)%4]
        if straight < max_straight:
            directions.append(direction)

        for new_direction in directions:
            new_row = row + {UP: -1, DOWN: 1}.get(direction, 0)
            new_col = col + {LEFT: -1, RIGHT: 1}.get(direction, 0)
            if not 0 <= new_row < len(lines) or not 0 <= new_col < len(lines[0]):
                continue
            new_straight = 1 + straight * (new_direction == direction)
            if (new_row, new_col, new_direction, new_straight) in visited:
                continue
            visited.add((new_row, new_col, new_direction, new_straight))
            heapq.heappush(Q, (cost + int(lines[new_row][new_col]), new_row, new_col, new_direction, new_straight))
            

assert minimum_heat_loss(lines, 0, 3) == 635
assert minimum_heat_loss(lines, 4, 10) == 734
