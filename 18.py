lines = list(open('18.txt'))


def lagoon_area(lines):
    row, col = 0, 0
    detsum = 0
    missed = 0
    previous_direction = None
    for line in lines:
        direction, count, _ = line.split()
        count = int(count)
        new_row, new_col = row, col
        if direction == 'R':
            new_col += count
        if direction == 'U':
            new_row -= count
        if direction == 'L':
            new_col -= count
            # count cells that will be missed by area calculation
            missed += count
            # if we just came down, count the corner: ┛
            if previous_direction == 'D':
                missed += 1
        if direction == 'D':
            new_row += count
            # count cells that will be missed by area calculation
            missed += count
            # if we just came from the left, remove the corner that was counted twice: ┏ 
            if previous_direction == 'L':
                missed -= 1
        # shoelace method
        detsum += row*new_col - col*new_row
        row, col = new_row, new_col
        previous_direction = direction
    return abs(detsum) // 2 + missed


def lagoon_area_hex(lines):
    new_lines = []
    for line in lines:
        _, hex_code = line.split('#')
        count = int(hex_code[:5], 16)
        direction = 'RDLU'[int(hex_code[5])]
        new_lines.append(f'{direction} {count} _')
    return lagoon_area(new_lines)


assert lagoon_area(lines) == 41019
assert lagoon_area_hex(lines) == 96116995735219
