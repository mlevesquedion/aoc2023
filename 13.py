text = open('13.txt').read()

# This is completely unnecessary since the performance is just fine with string 
# comparisons, but I think it's neat and it enables using XOR in the 2nd part.
def line2int(line):
    return int(''.join(line).translate(str.maketrans('.#', '01')), 2)


chunks = text.split('\n\n')
patterns = [c.split('\n') for c in chunks]

rows_cols = [([line2int(r) for r in rows], [line2int(col) for col in list(zip(*rows))]) for rows in patterns]


def reflection(lines):
    for i in range(0, len(lines)-1):
        j = 0
        while i-j >= 0 and i+j+1 < len(lines) and lines[i-j] == lines[i+j+1]:
            j += 1
        if i-j == -1 or i+j+1 == len(lines):
            return i+1
    return 0


row_col_reflections = [(reflection(rows), reflection(cols)) for rows, cols in rows_cols]

assert sum(row*100 + col for row, col in row_col_reflections) == 43614


def smudged_reflection(lines, avoid):
    for i in range(0, len(lines)-1):
        j = 0
        smudged = False
        while i-j >= 0 and i+j+1 < len(lines):
            if lines[i-j] != lines[i+j+1]:
                if smudged:
                    break
                if (lines[i-j] ^ lines[i+j+1]).bit_count() == 1:
                    smudged = True
                else:
                    break
            j += 1
        if (i-j == -1 or i+j+1 == len(lines)) and i+1 != avoid and smudged:
            return i+1
    return 0


assert sum(smudged_reflection(rows, row)*100 + \
           smudged_reflection(cols, col) \
           for (rows, cols), (row, col) in zip(rows_cols, row_col_reflections)) == 36771
