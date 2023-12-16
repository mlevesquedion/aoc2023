import itertools

lines = [line.strip() for line in open('16.txt')]

RIGHT, DOWN, LEFT, UP = range(4)


def energized_count(start_row, start_col, direction):
    beams = [(start_row, start_col, direction)]
    seen = set()
    while beams:
        next_beams = []
        for row, col, direction in beams:
            if (row, col, direction) in seen or not 0 <= row < len(lines) or not 0 <= col < len(lines[0]):
                continue
            seen.add((row, col, direction))
            directions = []
            if lines[row][col] == '.' or (lines[row][col] == '|' and direction in (DOWN, UP)) or (lines[row][col] == '-' and direction in (LEFT, RIGHT)):
                directions.append(direction)
            elif lines[row][col] == '|':
                directions = [DOWN, UP]
            elif lines[row][col] == '-':
                directions = [RIGHT, LEFT]
            elif lines[row][col] == '/':
                # 0 <--> 3, 1 <--> 2
                directions.append(3-direction)
            elif lines[row][col] == '\\':
                # 0 <--> 1, 2 <--> 3
                directions.append((1-direction)%4)
            next_beams += [(row+{DOWN: 1, UP: -1}.get(d, 0), col+{RIGHT: 1, LEFT: -1}.get(d, 0), d) for d in directions]
        beams = next_beams
    return len({(x, y) for x, y, _ in seen})


rows, cols = len(lines), len(lines[0])
starts = []
for row in range(rows):
    starts += [(row, 0, RIGHT), (row, cols-1, LEFT)]
for col in range(cols):
    starts += [(0, col, DOWN), (rows-1, col, UP)]
assert max(itertools.starmap(energized_count, starts)) == 7793
