# PROBLEM: Find the greatest common divisor of two integers.
# INPUT: 24 18
# OUTPUT: 6

a, b = map(int, input().split())

# Keep replacing the pair with (b, remainder) until remainder is zero.
while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(abs(a))
