# -*- coding: utf-8 -*-

import pytest
from Q2 import Node, LinkedList


def test1():
    linked_list = LinkedList()
    linked_list.add_item(11)
    linked_list.add_item(18)
    linked_list.add_item(24)
    linked_list.add_item(118)
    linked_list.add_item(58)

    assert linked_list.search_for_kth_element(0) == 58
    assert linked_list.search_for_kth_element(1) == 118
    assert linked_list.search_for_kth_element(2) == 24
    assert linked_list.search_for_kth_element(3) == 18
    assert linked_list.search_for_kth_element(4) == 11
