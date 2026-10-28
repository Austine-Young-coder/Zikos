# PROBLEM: Calculate the number of ways to choose R items from N, modulo M.
# INPUT: 5 2 1000
# OUTPUT: 10
# This beginner version uses exact integer combinations first.

import math

n, r, m = map(int, input().split())

if r < 0 or r > n:
    print(0)
else:
    print(math.comb(n, r) % m)
