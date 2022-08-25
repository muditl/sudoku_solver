import pytest
import numpy as np

from week_1.sudoku.complex_solver import *


@pytest.mark.parametrize("binary, expected",
                         [(1010110, [1000000, 10000, 100, 10]), (11, [10, 1]), (0, []), (100000000, [100000000])])
def test_split_ones(binary, expected):
    ones = split_ones(binary)
    ones.sort()
    expected.sort()
    np.testing.assert_array_equal(ones, expected)


@pytest.mark.parametrize("possibility, expected",
                         [((1, 2, 1010110), [(1, 2, 1000000), (1, 2, 10000), (1, 2, 100), (1, 2, 10)]),
                          ((0, 0, 11), [(0, 0, 10), (0, 0, 1)]),
                          ((4, 0, 100000000), [(4, 0, 100000000)])])
def test_split_possibility(possibility, expected):
    possibilities = split_possibility(possibility)
    possibilities.sort()
    expected.sort()
    np.testing.assert_array_equal(possibilities, expected)
