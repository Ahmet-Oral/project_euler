# ----------------------------------------------------------------------------------------------------------------------

# Problem 16 - Power digit sum

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?


# ----------------------------------------------------------------------------------------------------------------------

number = 2**1000
sum_of_digits = 0

for digit in str(number):
    sum_of_digits += int(digit)

print(sum_of_digits)

