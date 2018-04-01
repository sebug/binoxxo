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

def never_more_than_two_per_row(grid):
    for r in grid:
        if not no_more_than_two_per_row('X', r):
            return False
        if not no_more_than_two_per_row('O', r):
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

def no_row_with_more_than_half(grid):
    for r in grid:
        if not not_more_than_half_per_row(r):
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

def explore_prime(i, j, grid, flip_grid, l):
    if any_row_eq(grid):
        return False
    if any_row_eq(flip_grid):
        return False
    if not no_row_with_more_than_half(grid):
        return False
    if not never_more_than_two_per_row(grid):
        return False
    if not never_more_than_two_per_row(flip_grid):
        return False

    if j >= l:
        # at the end
        return grid

    next_j = j
    next_i = i + 1
    if next_i >= l:
        next_j = j + 1
        next_i = 0

    c = grid[i][j]
    if c != ' ':
        # already set at this position
        return explore_prime(next_i, next_j, grid, flip_grid, l)
    else:
        grid[i][j] = 'X'
        flip_grid[j][i] = 'X'
        res_x = explore_prime(next_i, next_j, grid, flip_grid, l)
        if res_x != False:
            return res_x
        else:
            grid[i][j] = 'O'
            flip_grid[j][i] = 'O'
            res_after = explore_prime(next_i, next_j, grid, flip_grid, l)
            if res_after == False:
                print "Did not manage to get a result"
                return grid
            else:
                return res_after


def explore(i, j, grid):
    return explore_prime(i, j, grid, flip(grid), len(grid))

if __name__ == '__main__':
    # print no_more_than_two_per_row('X', [' ', 'X', ' ']) # true
    # print no_more_than_two_per_row('X', ['X', 'X', ' ']) # true
    # print no_more_than_two_per_row('X', ['X', 'X', 'X']) # false
    # print no_more_than_two_per_row('X', [' ', 'X', 'X', 'X']) # false
    # print no_more_than_two_per_row('X', ['X', 'O', 'X']) # true
    # print not_more_than_half_per_row(['X','X','X','O']) # false
    # print not_more_than_half_per_row(['X','X','O','O']) # true
    # print not_more_than_half_per_row(['O','X','O', ' ']) # true
    # print row_eq(['X'],['O']) # false
    # print row_eq(['X'],['X']) # true
    # print row_eq([' '],[' ']) # false
    # print any_row_eq(grid_1) # false

    pretty_print(explore(0, 0, grid_1))


