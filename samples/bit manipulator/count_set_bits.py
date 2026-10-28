# PROBLEM: Count how many 1 bits are in a non-negative integer.
# INPUT: 13
# OUTPUT: 3

n = int(input())
binary_text = bin(n)[2:]
count = 0

for bit in binary_text:
    if bit == "1":
        count += 1

print(count)
