from week_1.sudoku.common_methods import *
from week_1.sudoku.LinkedList import LinkedList
from week_1.sudoku.simple_solver import simple_method


def complex_method(solved):
    print("Method not implemented yet...")
    print("This is how far we got")
    lists = generate_possible_lists(solved)
    possibilities_arrays = generate_possibilities_arrays(lists)
    reduction_factors = []
    queue = LinkedList()
    for possiblility in possibilities_arrays[1]:
        queue.__add__(possiblility)
        rf = reduction_factor(lists, possiblility)
        reduction_factors.append(rf)
    new_order = np.flip(np.argsort(reduction_factors))
    queue.reorder(new_order)
    solved = try_filling_possibility_and_simple_solving(solved, queue.get_first())


def try_filling_possibility_and_simple_solving(grid, possibility):
    row, col = possibility[0], possibility[1]
    number = binary_to_number(possibility[2])
    grid[row, col] = number
    solved = simple_method(grid)
    return solved


def reduction_factor(lists, possibiity):
    try_list = np.copy(lists)
    row, col = possibiity[0], possibiity[1]
    binary = possibiity[2]
    ones_before = count_ones_in_lists(try_list)
    fill_number(try_list, row, col, binary)
    ones_after = count_ones_in_lists(try_list)
    return ones_before - ones_after


def count_ones_in_lists(lists):
    count = 0
    for i in range(9):
        for j in range(9):
            count += count_ones(lists[i, j])
    return count


def split_possibility(possibility):
    x, y = possibility[0], possibility[1]
    ones = split_ones(possibility[2])
    possibilities = []
    for i in range(len(ones)):
        possibilities.append([x, y, ones[i]])

    return possibilities


def split_ones(binary):
    string_rep = str(binary)
    splits = []
    for i in range(len(string_rep)):
        if string_rep[len(string_rep) - i - 1] == '1':
            splits.append(number_to_9_digit_binary(i + 1))
    return splits

# TODO
#   dfs
#   put possibilities in q
#   get min out
#   split it and then put the second one in a new q
#
