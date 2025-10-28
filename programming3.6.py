"""
Given three values, A, B, and C, determine whether they can be the lengths of
the sides of a triangle. If so, determine whether they constitute an
equilateral, isosceles, or scalene triangle.
"""

a = int(input("Value of A:"))
b = int(input("Value of B:"))
c = int(input("Value of C:"))

if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b) and (b == c):
        print("Equilateral")
    else:
        if (a == b) or (b == c) or (a == c):
            print("Isosceles")
        else:
            print("Scalene")
else:
    print("It's not a triangle")
