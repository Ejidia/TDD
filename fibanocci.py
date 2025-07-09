# This function calculates the nth Fibonacci number.
# The Fibonacci sequence starts with 0, 1 and each number after is the sum of the previous two.
# Example: 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(n):
    # If n is 0, return 0 as the first Fibonacci number
    if n == 0:
        return 0

    # If n is 1, return 1 as the second Fibonacci number
    elif n == 1:
        return 1

    # For n >= 2, calculate the value using iteration
    a, b = 0, 1  # a = fib(0), b = fib(1)
    for _ in range(2, n + 1):
        a, b = b, a + b  # Move one step ahead in the sequence

    return b  # Return the nth Fibonacci number