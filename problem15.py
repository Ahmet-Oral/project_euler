# ----------------------------------------------------------------------------------------------------------------------
# Problem 15 - Lattice Paths - 'https://projecteuler.net/problem=15'
# ----------------------------------------------------------------------------------------------------------------------



def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    return prod


def binomial(n):
    b = factorial(2 * n) / (factorial(n) ** 2)
    return b


print(binomial(20))
