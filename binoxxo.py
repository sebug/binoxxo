#!/usr/local/bin/python

grid_1 = [
    [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O', ' ', 'X'],
    [' ', 'X', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
    [' ', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'O', ' '],
    [' ', 'X', ' ', 'O', ' ', ' ', ' ', 'O', 'X', ' '],
    [' ', ' ', ' ', ' ', ' ', 'O', 'O', ' ', ' ', ' '],
    [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
    ['O', ' ', 'O', ' ', ' ', 'X', ' ', ' ', 'X', 'X']
]

def get_line(l):
    return "".join(l)

def get_rows(grid):
    return "\n".join([get_line(l) for l in grid])

def pretty_print(grid):
    print get_rows(grid)

def nth_column_as_line(n, grid):
    return [r[n] for r in grid]

def flip(grid):
    return [nth_column_as_line(n, grid) for n in range(0, len(grid))]

def no_more_than_two_per_row(character, row):
    for i in range(0, len(row) - 2):
        if row[i] == character and row[i + 1] == character and row[i + 2] == character:
            return False
    return True

def not_more_than_half_per_row(row):
    l = len(row)
    xcount = 0
    ocount = 0
    for c in row:
        if c == 'X':
            xcount += 1
        elif c == 'O':
            ocount += 1

        if xcount > l / 2 or ocount > l / 2:
            return False
    return True

def row_eq(r1, r2):
    for i in range(0, len(r1)):
        if r1[i] == ' ' or r2[i] == ' ':
            return False
        elif r1[i] != r2[i]:
            return False
    return True

def any_row_eq(grid):
    for i in range(0, len(grid) - 1):
        for j in range(i + 1, len(grid)):
            if row_eq(grid[i], grid[j]):
                return True
    return False

if __name__ == '__main__':
    pretty_print(grid_1)

    pretty_print(flip(grid_1))

    print no_more_than_two_per_row('X', [' ', 'X', ' ']) # true
    print no_more_than_two_per_row('X', ['X', 'X', ' ']) # true
    print no_more_than_two_per_row('X', ['X', 'X', 'X']) # false
    print no_more_than_two_per_row('X', [' ', 'X', 'X', 'X']) # false
    print no_more_than_two_per_row('X', ['X', 'O', 'X']) # true
    print not_more_than_half_per_row(['X','X','X','O']) # false
    print not_more_than_half_per_row(['X','X','O','O']) # true
    print not_more_than_half_per_row(['O','X','O', ' ']) # true
    print row_eq(['X'],['O']) # false
    print row_eq(['X'],['X']) # true
    print row_eq([' '],[' ']) # false
    print any_row_eq(grid_1) # false


