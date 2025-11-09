"""
Exercise 3.4 - page 87

Calculate the N-th harmonic number H_N, where H_N = 1 + 1/2 + 1/3 + ... + 1/N.
"""

def calculate_harmonic_series(N: int) -> float:
    """
    Calculates the N-th harmonic number H_N.

    Args:
        N: The number of terms to sum (N >= 1).

    Returns:
        The sum of the series as a floating-point number.
    """
    # The sum is initialized to 0.0 to ensure calculations use floating-point precision.
    harmonic_sum = 0.0

    # The loop correctly iterates from i = 1 (inclusive) up to N (inclusive).
    for i in range(1, N + 1):
        # Adds the reciprocal of i to the sum.
        harmonic_sum += 1 / i

    return harmonic_sum

N = 10
result = calculate_harmonic_series(N)

# Displaying the result with four decimal places for clarity.
print(f"The number of terms (N): {N}")
print(f"The Harmonic number H_{N} is: {result:.4f}")