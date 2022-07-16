# ----------------------------------------------------------------------------------------------------------------------

# Problem 10 - Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# ----------------------------------------------------------------------------------------------------------------------

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


sum_of_primes = 2
number = 1
while number < 2000000:
    # Increment by 2. Saving time by not checking even numbers
    number = number + 2

    if is_prime(number):
        sum_of_primes = sum_of_primes + number

print(sum_of_primes)