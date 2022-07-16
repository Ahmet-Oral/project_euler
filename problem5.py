# ----------------------------------------------------------------------------------------------------------------------

# Problem 5 - Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# ----------------------------------------------------------------------------------------------------------------------

number = 20

while number:
    number = number + 20
    for i in range(20, 0, -1):
        if number % i != 0:
            break
        if i == 1:
            print(number)

            # break the loop
            number = 0
