"""
Calculates the factorial of a non-negative integer N using an iterative approach.
"""

import sys


def calculate_factorial_iterative(N: int) -> int:
    """
    Computes N! (N factorial) for a non-negative integer N.

    Raises:
        ValueError: If N is a negative integer.
    """
    # Base case for invalid input (non-negative constraint)
    if N < 0:
        raise ValueError("Factorial is not defined for negative numbers (N must be >= 0).")

    # Base case for 0! = 1 and 1! = 1
    if N == 0 or N == 1:
        return 1

    result = 1
    # Iterating from 2 up to N (inclusive) is clearer and standard.
    # range(2, N + 1) replaces the descending range(N, 1, -1).
    for i in range(2, N + 1):
        result *= i

    return result

# Example Execution
N_INPUT = int(sys.argv[1])

try:
    result = calculate_factorial_iterative(N_INPUT)
    print(f"The factorial of {N_INPUT} ({N_INPUT}!) is: {result}")
except ValueError as e:
    print(f"Error: {e}")