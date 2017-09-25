# -*- coding: utf-8 -*-

import pytest
from Q1 import is_a_permutation


def test_given_cases():
    assert is_a_permutation('Listen', 'Silent')
    assert is_a_permutation('Triangle', 'Integral')
    assert is_a_permutation('Apple', 'Pabble') == False


def test_new_cases():
    with pytest.raises(ValueError) as excinfo:
        is_a_permutation(123, 231)
    assert str(excinfo.value) == 'Input must be string!'

    assert is_a_permutation('', '')
    assert is_a_permutation('Purr', 'Purrr') == False
    assert is_a_permutation('I am Lord Voldemort', 'Tom Marvolo Riddle ')
