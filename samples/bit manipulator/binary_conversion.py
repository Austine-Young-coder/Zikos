# PROBLEM: Convert a non-negative integer to binary.
# INPUT: 13
# OUTPUT: 1101

n = int(input())
print(bin(n)[2:])  # Remove the leading '0b' from Python's result.
