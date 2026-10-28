# PROBLEM: Determine whether an integer is odd or even using its last bit.
# INPUT: 7
# OUTPUT: ODD

n = int(input())

# An odd number has a last binary bit of 1.
if n & 1:
    print("ODD")
else:
    print("EVEN")
