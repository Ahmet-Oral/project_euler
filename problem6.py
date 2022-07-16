# ----------------------------------------------------------------------------------------------------------------------

# problem 6 - Sum square difference
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# ----------------------------------------------------------------------------------------------------------------------

sum_of_squares = sum([x ** 2 for x in range(1, 101)])

square_of_sum = sum([x for x in range(1, 101)]) ** 2

print(square_of_sum - sum_of_squares)
