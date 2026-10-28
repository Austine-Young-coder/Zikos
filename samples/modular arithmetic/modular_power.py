# PROBLEM: Calculate A raised to B modulo M.
# INPUT: 2 10 1000
# OUTPUT: 24

a, b, m = map(int, input().split())

# Three-argument pow calculates the modular power efficiently.
print(pow(a, b, m))
