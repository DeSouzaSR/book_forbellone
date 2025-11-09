"""
Generate the Fibonacci sequence up to the 20th term.
"""

def fibonacci(n: int) -> int:
    """
    Calculate Fibonacci term
    """

    if n == 0:
        return n
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    N = 20

    for i in range(N+1):
        print(fibonacci(i), end=", ")
    print("\n")