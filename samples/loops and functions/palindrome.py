# PROBLEM: Check whether a word reads the same forwards and backwards.
# INPUT: level
# OUTPUT: YES

word = input().strip()

# Reversing with [::-1] gives the characters in reverse order.
if word == word[::-1]:
    print("YES")
else:
    print("NO")
