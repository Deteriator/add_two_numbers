import pytest
from add_two_numbers import *


def test_add_two_numbers():
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)

    l2 = Node(1)
    l2.next = Node(1)
    l2.next.next = Node(1)

    sum_list = add_two_numbers(l1, l2)

    assert sum_list.data == 4
    assert sum_list.next.data == 3
    assert sum_list.next.next.data == 2

def test_add_with_carry():
    l1 = Node(7)
    l1.next = Node(2)
    l1.next.next = Node(1)

    l2 = Node(4)
    l2.next = Node(7)

    sum_list = add_two_numbers(l1, l2)

    assert sum_list.data == 1
    assert sum_list.next.data == 0
    assert sum_list.next.next.data == 2
