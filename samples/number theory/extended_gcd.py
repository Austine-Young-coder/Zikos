# PROBLEM: Find gcd(a,b) and integers x,y where a*x + b*y = gcd(a,b).
# INPUT: 30 18
# OUTPUT: gcd and coefficients x y

a, b = map(int, input().split())
original_a, original_b = a, b
old_r, r = a, b
old_x, x = 1, 0
old_y, y = 0, 1

# Update the remainders and coefficients together.
while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_x, x = x, old_x - quotient * x
    old_y, y = y, old_y - quotient * y

print(old_r, old_x, old_y)
