"""
Write an algorithm that reads three different integers and displays them in descending order.
"""

from sys import argv

a = int(argv[1])
b = int(argv[2])
c = int(argv[3])

# if (a > b) and (b > c):
#     print(a, b, c)
# if (a > c) and (c > b):
#     print(a, c, b)
# if (b > a) and (a > c):
#     print(b, a, c) 
# if (b > c) and (c > a):
#     print(b, c, a)
# if (c > a) and (a > b):
#     print(c, a, b)
# if (c > b) and (b > c):
#     print(c, b, a)   

# Optimized version
nums = [a, b, c]
nums.sort(reverse=True)
print(*nums)  