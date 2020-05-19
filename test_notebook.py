import pytest
from Lesson_5 import *


def test_is_number_simple():
    assert is_number_simple(7) == True


def test_simple_dividers():
    assert simple_dividers(7) == [7]


def test_max_divider():
    d = 2
    number = 10
    while d * d <= number:
        if number % d == 0:
            number //= d
        else:
            d += 1
    print(number)
    return number


def test_use_dividers():
    assert use_dividers(7) == [7]


def test_max_any_dividers():
    assert max_any_dividers(7) == 7
