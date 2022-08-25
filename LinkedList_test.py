from week_1.sudoku.LinkedList import *
import pytest
import numpy as np


@pytest.mark.parametrize("e",
                         [(2, 4, 1001001), (1, 0, 100000), (2, 3, 1000), (4, 6, 111111111), (6, 8, 111001011)])
def test_linked_list_init(e):
    linked_list = LinkedList(e)
    assert (linked_list is not None and linked_list.__sizeof__() == 1)


def test_empty_linked_list_constructor():
    linked_list = LinkedList()
    assert (linked_list is not None and linked_list.__sizeof__() == 0)


@pytest.mark.parametrize("elements, expected_size",
                         [([[2, 4, 1001001]], 1), ([[1, 0, 100000], [2, 3, 1000], [4, 6, 111111111]], 3),
                          ([[1, 2]], 0)])
def test_linked_list_add(elements, expected_size):
    linked_list = LinkedList()
    if len(elements[0]) != 3:
        with pytest.raises(Exception):
            assert linked_list.__add__(elements[0])
    else:
        for e in elements:
            linked_list.__add__(e)
        assert (linked_list.__sizeof__() == expected_size)


@pytest.mark.parametrize("elements, expected",
                         [([(2, 4, 1001001)], (2, 4, 1001001)),
                          ([(1, 0, 100000), (2, 3, 1000), (4, 6, 111111111)], (1, 0, 100000)), ([], None)])
def test_linked_list_get_first(elements, expected):
    linked_list = LinkedList()
    for e in elements:
        linked_list.__add__(e)
    if len(elements) > 0:
        assert (linked_list.get_first() == elements[0])
    else:
        with pytest.raises(Exception):
            assert linked_list.get_first()


@pytest.mark.parametrize("elements",
                         [[(2, 4, 1001001)],
                          [(1, 0, 100000), (2, 3, 1000), (4, 6, 111111111)], []])
def test_linked_list_remove_first(elements):
    linked_list = LinkedList()
    for e in elements:
        linked_list.__add__(e)

    for e in elements:
        removed = linked_list.remove_first()
        assert (e.__str__() == removed.__str__())

    assert linked_list.__sizeof__() == 0
    with pytest.raises(Exception):
        assert linked_list.get_first()


@pytest.mark.parametrize("elements, order, expected",
                         [([[2, 4, 1001001], [4, 2, 10100101]], [1, 0], [[4, 2, 10100101], [2, 4, 1001001]]),
                          ([(1, 0, 100000), (2, 3, 1000), (4, 6, 111111111)], [2, 1, 0],
                           [(4, 6, 111111111), (2, 3, 1000), (1, 0, 100000)])])
def test_linked_list_reorder(elements, order, expected):
    linked_list = LinkedList()
    for e in elements:
        linked_list.__add__(e)

    linked_list.reorder(order)
    print("----------- here _--------------- ")
    print(linked_list.__str__())
    np.testing.assert_array_equal(expected, linked_list.get__all())
