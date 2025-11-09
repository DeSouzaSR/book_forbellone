"""
Write an algorithm that prints all the possibilities of getting a sum of 7 when rolling two dice.
"""
i: int = 0
j: int = 0

while i <= 5:

for i in range(6):
    while j in range(6):
        dice_sum = i + j

        if dice_sum == 7:
            print(dice_sum)

         