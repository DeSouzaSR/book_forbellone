"""
Docstring for chapters.chapter4.program_4_1
This program reads ten grades, calculates the average, and counts how many grades are above the average.
"""

# Vector with 10 positions
vet_class = [0.0] * 10

# Initialization of simple variables
sum_vec = 0
top_grade = 0

# Loop to read the vet_class vector.
for i in range(10):
    vet_class[i] = float(input(f'Nota{i+1}: '))

# Loop to sum the values.
for i in range(10):
    sum_vec = sum_vec + vet_class[i]

# Calculating the average
mean = sum_vec / 10

# Loop to count the values ​​that are above average in the vet_class vector.
for i in range(10):
    if vet_class[i] > mean:
        top_grade = top_grade + 1

print(f'Average: ', mean)
print("Number of grades above average: ", top_grade)