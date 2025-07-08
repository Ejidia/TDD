
#Ejidia and Patience, Linda
# factorial.py
# This module provides a function to calculate the factorial of a non-negative integer.
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)