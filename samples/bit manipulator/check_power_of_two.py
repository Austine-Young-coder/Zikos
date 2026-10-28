# PROBLEM: Check whether a positive integer is a power of two.
# INPUT: 16
# OUTPUT: YES

n = int(input())

# A power of two has exactly one set bit.
if n > 0 and (n & (n - 1)) == 0:
    print("YES")
else:
    print("NO")
