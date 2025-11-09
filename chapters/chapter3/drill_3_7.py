"""
Write an algorithm that reads a set of 20 integers and displays the largest and smallest values ​​entered.
"""

N: int = 20

n = int(input("Enter a number: "))
bigger = n 
smaller = n 

for _ in range(N - 1):
    n = int(input("Enter a number: "))

    if n > bigger:
        bigger = n 

    if n < smaller:
        smaller = n

print(f'Bigger: {bigger}')
print(f'Smaller: {smaller}')