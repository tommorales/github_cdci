# test_math_operations.py
import pytest
from math_operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 7) == -7
    assert subtract(-3, -3) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):  # Test for division by zero
        divide(5, 0)

