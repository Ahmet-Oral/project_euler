# ----------------------------------------------------------------------------------------------------------------------

# Problem 9 - Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# ----------------------------------------------------------------------------------------------------------------------


for a in range(1,1000):
    for b in range(a, 1000):
        if a+b > 1000:
            break
        c = (a**2 + b**2) ** 0.5

        if c % 1 == 0:
            if a + b + c == 1000:
                print("a: ", a, " - b: ", b, " - c: ", c)
                print("Product: ", a * b * c)

