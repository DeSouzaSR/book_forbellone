"""
Exercise 3.2 - page 87

Develop an algorithm that calculates the integer closest to the square root of a number provided by the user
"""

# --- Original implementation ---

# import math


# def f(n, i):
#     """Returns the absolute value of the difference between the square root of a number and a given integer. """
#     return(abs(math.sqrt(n) - i))



# def smaller(f, n):
#     smaller = f(n, 1)

#     for i in range(2,n+1):
#         ans = f(n, i)

#         if smaller > ans:
#             smaller = ans
#     return smaller


# def main():
#     n = 5

#     small = smaller(f, n)

#     print(small)
#     print("Finish program!")

# if __name__ == "__main__":
#     main()


# --- Second attempt (Refactored) ---

import math
import sys

def integer_closest_to_sqrt(n: int) -> int:
    """
    Calculates and returns the integer closest to the square root of a number 'n'.
    Utilizes the native round() function for rounding.
    """
    if n < 0:
        raise ValueError("O número deve ser não-negativo.")
    
    square_root = math.sqrt(n)
    return round(square_root)

def main():
    n = float(sys.argv[1])
    result = integer_closest_to_sqrt(n)
    
    print(f"O inteiro mais próximo à raiz quadrada de {n} é: {result}")
    print("Finish program!")

if __name__ == "__main__":
    main()
