# This file contains test cases for the fibonacci() function using pytest

# Ejidia and Patience, Linda
import pytest
from fibanocci import fibonacci

def test_fibonacci_0(): 
    assert fibonacci(0) == 0  # Base case

def test_fibonacci_1():
    assert fibonacci(1) == 1  # Base case

def test_fibonacci_2():
    assert fibonacci(2) == 1  # 0, 1, 1

def test_fibonacci_3():
    assert fibonacci(3) == 2  # 0, 1, 1, 2

def test_fibonacci_5():
    assert fibonacci(5) == 5  # 0, 1, 1, 2, 3, 5

def test_fibonacci_10():
    assert fibonacci(10) == 55  # Known value

def test_fibonacci_15():
    assert fibonacci(15) == 610  # Known value



def test_fibonacci_negative():
    try:
        fibonacci(-1)
    except ValueError as e:
        assert str(e) == "Input must be a non-negative integer"
    else:
        assert False, "Expected ValueError for negative input"
def test_fibonacci_non_integer():
    try:
        fibonacci(3.5)
    except ValueError as e:
        assert str(e) == "Input must be a non-negative integer"
    else:
        assert False, "Expected ValueError for non-integer input"

