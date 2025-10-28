"""
Given three values, A, B, and C, determine whether they can be the lengths of
the sides of a triangle. If so, determine whether they constitute an
equilateral, isosceles, or scalene triangle.
"""

from sys import argv

a = int(argv[1])
b = int(argv[2])
c = int(argv[3])

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
