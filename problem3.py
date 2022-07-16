# ----------------------------------------------------------------------------------------------------------------------

# problem 3 - Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# ----------------------------------------------------------------------------------------------------------------------

import math

x = 600851475143

while x % 2 == 0:
    x = x / 2

for i in range(3, int(math.sqrt(x)) + 1, 2):
    while x % i == 0:
        print(i, )
        x = x / i

if x > 2:
    print(x)

