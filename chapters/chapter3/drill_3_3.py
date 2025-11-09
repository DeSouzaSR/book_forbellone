"""
Exercise 3.3 - page 87

Write an algorithm that checks whether a number provided by the user is prime or not.
"""

import sys
import math

# --- 1. Refactored Predicate Function ---

def is_prime(n: int) -> bool:
    """
    Checks if an integer 'n' is a prime number.
    Uses optimized trial division up to the square root of n.
    """
    if n <= 1:
        return False
    
    # Handle 2 (the only even prime)
    if n == 2:
        return True
    
    # Exclude all other even numbers immediately
    if n % 2 == 0:
        return False
    
    # Iterate through odd numbers from 3 up to the integer part of sqrt(n)
    # The 'stop' argument of range must be an integer. We add 1 because 
    # range() excludes the stop value, and we need to include the square root limit.
    limit = int(math.sqrt(n)) + 1
    
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
        
    return True

# --- 2. Main Execution Function with Argument Validation ---

def main():
    # Argument Check
    if len(sys.argv) < 2:
        print("Warning: No argument provided.")
        print(f"Usage: python {sys.argv[0]} <positive_integer>")
        sys.exit(1)

    argument = sys.argv[1]

    try:
        # Tries to convert the string to an integer
        integer_value = int(argument)

        # Check for positivity constraint (> 0)
        if integer_value <= 0:
            raise ValueError("The input must be a positive integer (greater than 0).")
        
        # Determine and print the result
        if is_prime(integer_value):
            print(f'{integer_value} is prime.')
        else:
            print(f'{integer_value} is not prime.')

    except ValueError as e:
        # Catches the error if the string cannot be converted OR if the number is not positive.
        print(f"Warning: The value '{argument}' is invalid.")
        # If the error is from the positivity check, the message will be specific.
        print(f"Constraint failure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()