import numpy as np
from week_1.sudoku.common_methods import *


def solve_sudoku_only_singles(grid):
    lists = generate_possible_lists(grid)
    possibilities_arrays = generate_possibilities_arrays(lists)
    stuck = False
    while not stuck:
        cur = possibilities_arrays[0]
        fill_all_numbers(lists, possibilities_arrays[0])
        possibilities_arrays = generate_possibilities_arrays(lists)
        if cur == possibilities_arrays[0]:
            stuck = True
    fill_all_numbers(lists, possibilities_arrays[0])
    return lists


def simple_method(unsolved):
    lists = solve_sudoku_only_singles(unsolved)
    solved = generate_grid_from_list(lists)
    return solved
