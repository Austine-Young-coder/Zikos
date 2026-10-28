# PROBLEM: Find the least common multiple of two positive integers.
# INPUT: 4 6
# OUTPUT: 12

a, b = map(int, input().split())
first = a
second = b

# Find the GCD using the Euclidean algorithm.
while second != 0:
    first, second = second, first % second

gcd = first

# LCM is the product divided by the GCD.
print(abs(a * b) // gcd if gcd != 0 else 0)
