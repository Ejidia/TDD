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



# fibonacci.py

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using iteration.
    Accepts only non-negative integers.

    Args:
        n (int): Fibonacci index

    Returns:
        int: Fibonacci number at index n

    Raises:
        ValueError: If n is not a non-negative integer
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
