import numpy as np


def initial_checks(grid):
    shape = np.shape(grid)
    if len(shape) != 2 or shape[0] != 9 or shape[1] != 9:
        raise Exception("invalid array")


# use binary to represent possible values
# 000000001 -> 1; 010001001 -> 1,4,8; 100100100-> 3,6,9; 000010000 ->5
def generate_possible_lists(grid):
    lists = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            # if square is empty
            if grid[i, j] == 0:
                for possible_sol in range(1, 10):
                    if is_valid(grid, possible_sol, i, j):
                        binary = number_to_9_digit_binary(possible_sol)
                        lists[i, j] += binary
            else:
                lists[i, j] = number_to_9_digit_binary(grid[i, j])
    return lists


def generate_possibilities_arrays(lists):
    rows, cols = lists.shape
    possibilities_arrays = np.zeros(rows, dtype=object)
    for i in range(rows):
        possibilities_arrays[i] = []

    for i in range(rows):
        for j in range(cols):
            ones = count_ones(lists[i, j])
            possibilities_arrays[ones - 1].append([i, j, lists[i, j]])
    return possibilities_arrays


def fill_number(lists, row, col, binary):
    update_lists_for_filling(lists, row, col, binary)


def update_lists_for_filling(lists, row, col, binary):
    update_row(lists, row, col, binary)
    update_col(lists, row, col, binary)
    update_box(lists, row, col, binary)


def update_row(lists, row, col, binary):
    for y in range(9):
        if y != col and has_number_possibility(lists[row, y], binary):
            lists[row, y] -= binary


def update_col(lists, row, col, binary):
    for x in range(9):
        if x != row and has_number_possibility(lists[x, col], binary):
            lists[x, col] -= binary


def update_box(lists, row, col, binary):
    box_x_and_y = get_box_x_and_y(row, col)
    rows, cols = box_x_and_y[0], box_x_and_y[1]
    for x in rows:
        for y in cols:
            if x != row and y != col and has_number_possibility(lists[x, y], binary):
                lists[x, y] -= binary


def has_number_possibility(to_check, binary):
    if binary > to_check:
        return False
    if binary == to_check:
        raise Exception("Invalid Puzzle")
    str_to_check = str(to_check)
    str_binary = str(binary)
    if str_to_check[len(str_to_check) - len(str_binary)] == '1':
        return True
    return False


def is_valid(grid, possible_sol, row, col):
    if row_is_valid(grid, possible_sol, row, col) and column_is_valid(grid, possible_sol, row, col) and \
            box_is_valid(grid, possible_sol, row, col):
        return True
    else:
        return False


def row_is_valid(grid, possible_sol, row, col):
    for x in range(9):
        if grid[row, x] == possible_sol:
            return False
    return True


def column_is_valid(grid, possible_sol, row, col):
    for y in range(9):
        if grid[y, col] == possible_sol:
            return False
    return True


def box_is_valid(grid, possible_sol, row, col):
    box_x_and_y = get_box_x_and_y(row, col)
    for x in box_x_and_y[0]:
        for y in box_x_and_y[1]:
            if grid[x, y] == possible_sol:
                return False
    return True


def get_box_x_and_y(row, col):
    if row < 3 and col < 3:
        return [[0, 1, 2], [0, 1, 2]]
    if row < 3 and 2 < col < 6:
        return [[0, 1, 2], [3, 4, 5]]
    if row < 3 and 5 < col < 9:
        return [[0, 1, 2], [6, 7, 8]]
    if 2 < row < 6 and col < 3:
        return [[3, 4, 5], [0, 1, 2]]
    if 2 < row < 6 and 2 < col < 6:
        return [[3, 4, 5], [3, 4, 5]]
    if 2 < row < 6 and 5 < col < 9:
        return [[3, 4, 5], [6, 7, 8]]
    if 5 < row < 9 and col < 3:
        return [[6, 7, 8], [0, 1, 2]]
    if 5 < row < 9 and 2 < col < 6:
        return [[6, 7, 8], [3, 4, 5]]
    if 5 < row < 9 and 5 < col < 9:
        return [[6, 7, 8], [6, 7, 8]]


def number_to_9_digit_binary(digit):
    # converts digit into the number that we want to convert to binary
    number = 2 ** (digit - 1)
    # converts the number into binary, but in a string
    binary_string = bin(number).replace("0b", "")
    # converts the string into an int
    binary = int(binary_string)
    return binary


def binary_to_number(binary):
    # converts the 9 digit binary number to a digit to fill in.
    # should only be used for binary number with a single 1.
    return len(str(binary))


def count_ones(binary):
    string_rep = str(binary)
    count = 0
    for i in string_rep:
        if int(i) == 1:
            count += 1
    return count


def fill_all_numbers(lists, singles):
    for row_col_binary in singles:
        row, col = row_col_binary[0], row_col_binary[1]
        binary = row_col_binary[2]
        fill_number(lists, row, col, binary)


def make_grid_from_string(sudoku_str):
    sudoku = np.zeros((9, 9), dtype=int)
    if len(sudoku_str) != 81:
        raise Exception("Expected 81 characters, got {}.".format(str(len(sudoku_str))))
    for i in range(81):
        sudoku[int(i / 9), i % 9] = sudoku_str[i]
    return sudoku


def ordered_list_of_ones(lists):
    rows, cols = lists.shape
    ones_list = np.zeros(9, dtype=object)
    for row in range(rows):
        for col in range(cols):
            count = count_ones(lists[row, col])
            if count > 0:
                ones_list[count - 1] = (row, col, lists[row, col])
    print(ones_list)


def generate_grid_from_list(lists):
    grid = np.zeros((9, 9), int)
    for i in range(9):
        for j in range(9):
            if count_ones(lists[i, j]) == 1:
                grid[i, j] = binary_to_number(lists[i, j])
            else:
                grid[i, j] = 0
    return grid


def is_solved(grid):
    for i in range(9):
        for j in range(9):
            if grid[i, j] == 0:
                return False
    return True
