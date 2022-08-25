import pytest
import numpy as np

from week_1.sudoku.common_methods import *


@pytest.mark.parametrize("array",
                         [np.zeros((3, 4)), [], np.zeros((3, 3)), np.zeros((4, 6)), np.zeros((12, 12)), np.zeros(9),
                          np.zeros((9, 9, 9))])
def test_initial_checks_raises(array):
    with pytest.raises(Exception):
        assert initial_checks(array)


def test_initial_checks_does_not_raise():
    try:
        initial_checks(np.zeros((9, 9)))
    except Exception as exc:
        assert False, f"Correct input raised an exception {exc}"


@pytest.mark.parametrize("i, j, expected",
                         [(3, 4, [[3, 4, 5], [3, 4, 5]]), (0, 1, [[0, 1, 2], [0, 1, 2]]),
                          (7, 2, [[6, 7, 8], [0, 1, 2]]), (0, 8, [[0, 1, 2], [6, 7, 8]]),
                          (3, 7, [[3, 4, 5], [6, 7, 8]])])
def test_get_box_x_and_y(i, j, expected):
    np.testing.assert_array_equal(get_box_x_and_y(i, j), expected)


@pytest.mark.parametrize("possible_sol, row, col, expected",
                         [(6, 1, 0, True), (2, 1, 0, False), (2, 3, 4, True), (9, 3, 7, False)])
def test_row_is_valid(possible_sol, row, col, expected):
    grid = generate_test_grids()[2]
    assert (row_is_valid(grid, possible_sol, row, col) is expected)


@pytest.mark.parametrize("possible_sol, row, col, expected",
                         [(6, 1, 0, True), (2, 1, 0, True), (2, 3, 4, False), (9, 3, 7, False)])
def test_col_is_valid(possible_sol, row, col, expected):
    grid = generate_test_grids()[2]
    assert (column_is_valid(grid, possible_sol, row, col) is expected)


@pytest.mark.parametrize("possible_sol, row, col, expected",
                         [(6, 1, 0, True), (2, 1, 0, True), (2, 3, 4, False), (9, 3, 7, False), (1, 7, 4, False),
                          (2, 8, 1, True), (3, 4, 2, False)])
def test_box_is_valid(possible_sol, row, col, expected):
    grid = generate_test_grids()[2]
    assert (box_is_valid(grid, possible_sol, row, col) is expected)


@pytest.mark.parametrize("possible_sol, row, col, expected",
                         [(6, 1, 0, True), (2, 1, 0, False), (2, 3, 4, False), (7, 3, 7, True), (1, 7, 4, False),
                          (2, 8, 1, True), (3, 4, 2, False)])
def test_is_valid(possible_sol, row, col, expected):
    grid = generate_test_grids()[2]
    assert (is_valid(grid, possible_sol, row, col) is expected)


@pytest.mark.parametrize("to_check, number, expected",
                         [(100010, 1, False), (10111, 1000, False), (10010111, 10000, True), (1001, 100000, False),
                          (10110, 10, True)])
def test_has_number_possibility(to_check, number, expected):
    assert (has_number_possibility(to_check, number) == expected)


@pytest.mark.parametrize("expected, test_number",
                         [([[[0, 0, 100], [0, 1, 1], [0, 2, 100000], [0, 3, 1000], [0, 4, 100000000], [0, 5, 10000],
                             [0, 6, 10], [0, 7, 1000000], [0, 8, 10000000], [1, 0, 10000], [1, 1, 1000000], [1, 2, 10],
                             [1, 3, 100], [1, 4, 100000], [1, 5, 10000000], [1, 6, 100000000], [1, 7, 1000], [1, 8, 1],
                             [2, 0, 100000000], [2, 1, 1000], [2, 2, 10000000], [2, 3, 1], [2, 4, 1000000], [2, 5, 10],
                             [2, 6, 100], [2, 7, 10000], [2, 8, 100000], [3, 0, 1], [3, 1, 100000], [3, 2, 10000],
                             [3, 3, 10], [3, 4, 100], [3, 5, 1000], [3, 6, 1000000], [3, 7, 10000000],
                             [3, 8, 100000000], [4, 0, 1000], [4, 1, 10000000], [4, 2, 100000000], [4, 3, 10000],
                             [4, 4, 1], [4, 5, 1000000], [4, 6, 100000], [4, 7, 10], [4, 8, 100], [5, 0, 10],
                             [5, 1, 100], [5, 2, 1000000], [5, 3, 100000], [5, 4, 10000000], [5, 5, 100000000],
                             [5, 6, 10000], [5, 7, 1], [5, 8, 1000], [6, 0, 100000], [6, 1, 10], [6, 2, 100],
                             [6, 3, 1000000], [6, 4, 1000], [6, 5, 1], [6, 6, 10000000], [6, 7, 100000000],
                             [6, 8, 10000], [7, 0, 1000000], [7, 1, 100000000], [7, 2, 1], [7, 3, 10000000],
                             [7, 4, 10000], [7, 5, 100000], [7, 6, 1000], [7, 7, 100], [7, 8, 10], [8, 0, 10000000],
                             [8, 1, 10000], [8, 2, 1000], [8, 3, 100000000], [8, 4, 10], [8, 5, 100], [8, 6, 1],
                             [8, 7, 100000], [8, 8, 1000000]], [], [], [], [], [], [], [], []], 0),
                          ([[[0, 1, 10000], [0, 6, 1], [0, 7, 100000000], [0, 8, 1000000], [1, 0, 100000],
                             [1, 7, 1000], [1, 8, 10], [2, 0, 100000000], [2, 1, 1], [2, 3, 1000], [2, 4, 10],
                             [2, 5, 1000000], [2, 6, 10000], [2, 7, 100000], [2, 8, 10000000], [3, 0, 100],
                             [3, 1, 1000], [3, 2, 10000], [3, 3, 10000000], [3, 5, 1], [3, 6, 100000000],
                             [3, 8, 100000], [4, 0, 1000000], [4, 1, 10], [4, 3, 100], [4, 4, 1000],
                             [4, 6, 10000000], [4, 8, 1], [5, 0, 10000000], [5, 1, 100000000], [5, 2, 1], [5, 3, 10],
                             [5, 5, 100000], [5, 8, 100], [6, 1, 100], [6, 2, 10000000], [6, 3, 1000000], [6, 6, 10],
                             [6, 7, 1], [6, 8, 100000000], [7, 0, 1], [7, 1, 100000], [7, 5, 10000000], [7, 8, 1000],
                             [8, 3, 1], [8, 6, 100000], [8, 7, 10000000], [8, 8, 10000]],
                            [[0, 5, 1100], [1, 6, 1000100], [2, 2, 1100], [3, 4, 11000000], [3, 7, 1000010],
                             [4, 5, 100010000], [4, 7, 10010], [5, 4, 1010000], [5, 6, 1001000], [5, 7, 1010000],
                             [6, 0, 11000], [7, 3, 100010000], [7, 6, 1000100], [7, 7, 1000100], [8, 0, 1010],
                             [8, 4, 100000100]],
                            [[0, 0, 101010], [0, 3, 10101000], [0, 4, 10100100], [1, 1, 11000100], [1, 2, 1100100],
                             [1, 5, 100010100], [4, 2, 100011], [7, 4, 100010100], [8, 1, 1000110]],
                            [[1, 3, 110110000], [6, 4, 100110100], [6, 5, 100011100], [7, 2, 101000110],
                             [8, 5, 100001110]], [[0, 2, 1101110], [8, 2, 101001110]],
                            [[1, 4, 110110101]], [], [], []], 2)])
def test_generate_possibilities_arrays(expected, test_number):
    lists = generate_possible_lists(generate_test_grids()[test_number])
    actual = generate_possibilities_arrays(lists)
    np.testing.assert_array_equal(actual, expected)


@pytest.mark.parametrize("digit, expected",
                         [(1, 1), (4, 1000), (7, 1000000), (9, 100000000)])
def test_number_to_9_digit_binary(digit, expected):
    assert (expected == number_to_9_digit_binary(digit))


@pytest.mark.parametrize("binary, expected",
                         [(1, 1), (1000, 4), (1000000, 7), (100000000, 9)])
def test_binary_to_number(binary, expected):
    assert (expected == binary_to_number(binary))


@pytest.mark.parametrize("number, expected",
                         [(1010110, 4), (11, 2), (0, 0), (100000000, 1)])
def test_count_ones(number, expected):
    assert (expected == count_ones(number))


@pytest.mark.parametrize("coordinates_and_numbers, test_number",
                         [([(0, 0, 100), (0, 1, 1), (0, 2, 100000), (0, 3, 1000), (0, 4, 100000000), (0, 5, 10000),
                            (0, 6, 10), (0, 7, 1000000), (0, 8, 10000000), (1, 0, 10000), (1, 1, 1000000), (1, 2, 10),
                            (1, 3, 100), (1, 4, 100000), (1, 5, 10000000), (1, 6, 100000000), (1, 7, 1000), (1, 8, 1),
                            (2, 0, 100000000), (2, 1, 1000), (2, 2, 10000000), (2, 3, 1), (2, 4, 1000000), (2, 5, 10),
                            (2, 6, 100), (2, 7, 10000), (2, 8, 100000), (3, 0, 1), (3, 1, 100000), (3, 2, 10000),
                            (3, 3, 10), (3, 4, 100), (3, 5, 1000), (3, 6, 1000000), (3, 7, 10000000),
                            (3, 8, 100000000), (4, 0, 1000), (4, 1, 10000000), (4, 2, 100000000), (4, 3, 10000),
                            (4, 4, 1), (4, 5, 1000000), (4, 6, 100000), (4, 7, 10), (4, 8, 100), (5, 0, 10),
                            (5, 1, 100), (5, 2, 1000000), (5, 3, 100000), (5, 4, 10000000), (5, 5, 100000000),
                            (5, 6, 10000), (5, 7, 1), (5, 8, 1000), (6, 0, 100000), (6, 1, 10), (6, 2, 100),
                            (6, 3, 1000000), (6, 4, 1000), (6, 5, 1), (6, 6, 10000000), (6, 7, 100000000),
                            (6, 8, 10000), (7, 0, 1000000), (7, 1, 100000000), (7, 2, 1), (7, 3, 10000000),
                            (7, 4, 10000), (7, 5, 100000), (7, 6, 1000), (7, 7, 100), (7, 8, 10), (8, 0, 10000000),
                            (8, 1, 10000), (8, 2, 1000), (8, 3, 100000000), (8, 4, 10), (8, 5, 100), (8, 6, 1),
                            (8, 7, 100000), (8, 8, 1000000)], 0),
                          ([(0, 0, 100), (0, 1, 1), (0, 2, 100000), (0, 3, 1000), (0, 4, 100000000), (0, 5, 10000),
                            (0, 6, 10), (0, 7, 1000000), (0, 8, 10000000), (1, 0, 10000), (1, 1, 1000000), (1, 2, 10),
                            (1, 3, 100), (1, 4, 100000), (1, 5, 10000000), (1, 6, 100000000), (1, 7, 1000), (1, 8, 1),
                            (2, 0, 100000000), (2, 1, 1000), (2, 2, 10000000), (2, 3, 1), (2, 4, 1000000), (2, 5, 10),
                            (2, 6, 100), (2, 7, 10000), (2, 8, 100000), (3, 0, 1), (3, 1, 100000), (3, 2, 10000),
                            (3, 3, 10), (3, 4, 100), (3, 5, 1000), (3, 6, 1000000), (3, 7, 10000000), (3, 8, 100000000),
                            (4, 0, 1000), (4, 1, 10000000), (4, 2, 100000000), (4, 3, 10000), (4, 4, 1),
                            (4, 5, 1000000), (4, 6, 100000), (4, 7, 10), (4, 8, 100), (5, 0, 10), (5, 1, 100),
                            (5, 2, 1000000), (5, 3, 100000), (5, 4, 10000000), (5, 5, 100000000), (5, 6, 10000),
                            (5, 7, 1), (5, 8, 1000), (6, 0, 100000), (6, 1, 10), (6, 2, 100), (6, 3, 1000000),
                            (6, 4, 1000), (6, 5, 1), (6, 6, 10000000), (6, 7, 100000000), (6, 8, 10000),
                            (7, 0, 1000000), (7, 1, 100000000), (7, 2, 1), (7, 3, 10000000), (7, 4, 10000),
                            (7, 5, 100000), (7, 6, 1000), (7, 7, 100), (7, 8, 10), (8, 0, 10000000), (8, 1, 10000),
                            (8, 2, 1000), (8, 3, 100000000), (8, 4, 10), (8, 5, 100), (8, 6, 1), (8, 7, 100000),
                            (8, 8, 1000000)], 1)])
def test_generate_possible_lists(coordinates_and_numbers, test_number):
    grids = generate_test_grids()
    expected = make_lists_from_coordinates_and_numbers(coordinates_and_numbers)
    actual = generate_possible_lists(grids[test_number])
    np.testing.assert_array_equal(expected, actual)


@pytest.mark.parametrize("row, col, binary",
                         [(0, 8, 1000000), (1, 0, 100000), (2, 3, 1000), (3, 3, 10000000), (4, 1, 10), (4, 6, 10000000),
                          (4, 8, 1), (5, 2, 1), (6, 1, 100), (6, 8, 100000000)])
def test_fill_number(row, col, binary):
    actual = generate_test_grids()[2]
    expected = actual.copy()
    expected[row, col] = binary_to_number(binary)
    lists = generate_possible_lists(actual)
    fill_number(actual, lists, row, col, binary)
    np.testing.assert_array_equal(actual, expected)


@pytest.mark.parametrize("row, col, number",
                         [(0, 8, 1000000), (1, 0, 100000), (2, 3, 1000), (3, 3, 10000000), (4, 1, 10), (4, 6, 10000000),
                          (4, 8, 1), (5, 2, 1), (6, 1, 100), (6, 8, 100000000)])
def test_update_row(row, col, number):
    grid = generate_test_grids()[2]
    lists = generate_possible_lists(grid)
    update_row(lists, row, col, number)
    success = True
    for x in range(9):
        if x != col:
            if has_number_possibility(lists[row, x], number):
                success = False
    assert (success is True)


@pytest.mark.parametrize("row, col, number",
                         [(0, 8, 1000000), (1, 0, 100000), (2, 3, 1000), (3, 3, 10000000), (4, 1, 10), (4, 6, 10000000),
                          (4, 8, 1), (5, 2, 1), (6, 1, 100), (6, 8, 100000000)])
def test_update_col(row, col, number):
    grid = generate_test_grids()[2]
    lists = generate_possible_lists(grid)
    update_col(lists, row, col, number)
    success = True
    for y in range(9):
        if y != row:
            if has_number_possibility(lists[y, col], number):
                success = False
    assert (success is True)


@pytest.mark.parametrize("row, col, number",
                         [(0, 8, 1000000), (1, 0, 100000), (2, 3, 1000), (3, 3, 10000000), (4, 1, 10), (4, 6, 10000000),
                          (4, 8, 1), (5, 2, 1), (6, 1, 100), (6, 8, 100000000)])
def test_update_box(row, col, number):
    grid = generate_test_grids()[2]
    lists = generate_possible_lists(grid)
    update_box(lists, row, col, number)
    box_x_and_y = get_box_x_and_y(row, col)
    success = True
    for x in box_x_and_y[0]:
        for y in box_x_and_y[1]:
            if x != row and y != col:
                if has_number_possibility(lists[x, y], number):
                    success = False
    assert (success is True)


@pytest.mark.parametrize("sudoku_str, test_number",
                         [('050000190000000042910027568345001906700340000890206003008700210160008004000100685', 2),
                          ('000940000008070100069020005450600008036805020082000000004280003010000057000001980', 3)])
def test_make_sudoku(sudoku_str, test_number):
    print(len(sudoku_str))
    expected = generate_test_grids()[test_number]
    actual = make_grid_from_string(sudoku_str)
    np.testing.assert_array_equal(expected, actual)


def generate_test_grids():
    return [np.array([[3, 1, 6, 4, 9, 5, 2, 7, 8], [5, 0, 2, 3, 6, 8, 9, 0, 1], [9, 4, 8, 1, 7, 2, 3, 5, 6],
                      [1, 6, 5, 2, 3, 0, 7, 8, 9], [4, 8, 9, 0, 1, 7, 6, 2, 3], [2, 3, 7, 6, 8, 9, 5, 1, 4],
                      [6, 2, 3, 7, 4, 1, 8, 9, 5], [7, 9, 1, 8, 5, 6, 4, 3, 2], [8, 5, 4, 9, 2, 3, 1, 6, 7]]),
            np.array([[0, 0, 0, 4, 9, 5, 2, 7, 8], [0, 0, 0, 3, 6, 8, 9, 4, 1], [0, 0, 0, 1, 7, 2, 3, 5, 6],
                      [1, 6, 5, 2, 3, 4, 7, 8, 9], [4, 8, 9, 5, 1, 7, 6, 2, 3], [2, 3, 7, 6, 8, 9, 5, 1, 4],
                      [6, 2, 3, 7, 4, 1, 8, 9, 5], [7, 9, 1, 8, 5, 6, 4, 3, 2], [8, 5, 4, 9, 2, 3, 1, 6, 7]]),
            np.array([[0, 5, 0, 0, 0, 0, 1, 9, 0], [0, 0, 0, 0, 0, 0, 0, 4, 2], [9, 1, 0, 0, 2, 7, 5, 6, 8],
                      [3, 4, 5, 0, 0, 1, 9, 0, 6], [7, 0, 0, 3, 4, 0, 0, 0, 0], [8, 9, 0, 2, 0, 6, 0, 0, 3],
                      [0, 0, 8, 7, 0, 0, 2, 1, 0], [1, 6, 0, 0, 0, 8, 0, 0, 4], [0, 0, 0, 1, 0, 0, 6, 8, 5]]),
            np.array([[0, 0, 0, 9, 4, 0, 0, 0, 0], [0, 0, 8, 0, 7, 0, 1, 0, 0], [0, 6, 9, 0, 2, 0, 0, 0, 5],
                      [4, 5, 0, 6, 0, 0, 0, 0, 8], [0, 3, 6, 8, 0, 5, 0, 2, 0], [0, 8, 2, 0, 0, 0, 0, 0, 0],
                      [0, 0, 4, 2, 8, 0, 0, 0, 3], [0, 1, 0, 0, 0, 0, 0, 5, 7], [0, 0, 0, 0, 0, 1, 9, 8, 0]])]


def make_lists_from_coordinates_and_numbers(coordinates_and_numbers):
    lists = np.zeros((9, 9), dtype=int)
    for coordinate_and_number in coordinates_and_numbers:
        row, col = coordinate_and_number[0], coordinate_and_number[1]
        number = coordinate_and_number[2]
        lists[row, col] = number
    return lists
