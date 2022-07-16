# ----------------------------------------------------------------------------------------------------------------------

# Problem 7 - 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# ----------------------------------------------------------------------------------------------------------------------


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


number = 1
counter = 1
while counter != 10001:
    # Increment by 2. Saving time by not checking even numbers
    number = number + 2

    if is_prime(number):
        counter += 1

print(number)
