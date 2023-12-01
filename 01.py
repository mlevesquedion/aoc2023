INPUT = list(open('01.txt'))
DIGITS = dict(zip('one two three four five six seven eight nine'.split(), '123456789'))


def calibration_value(line, patterns):
    left_indices = {line.find(p) if p in line else len(line): p for p in patterns}
    left = left_indices[min(left_indices)]
    right_indices = {line.rfind(p): p for p in patterns}
    right = right_indices[max(right_indices)]
    return int(DIGITS.get(left, left) + DIGITS.get(right, right))


def calibration_sum(lines, patterns):
    return sum(calibration_value(line, patterns) for line in lines)


assert calibration_sum(INPUT, '123456789') == 54304
assert calibration_sum(INPUT, '1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine'.split()) == 54418
