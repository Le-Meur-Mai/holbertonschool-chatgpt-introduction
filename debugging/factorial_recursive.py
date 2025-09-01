#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read input from command line argument and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
