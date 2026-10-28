# PROBLEM: Calculate N factorial using recursion.
# INPUT: 5
# OUTPUT: 120

def factorial(n):
    if n == 0:  # Base case: 0! is 1.
        return 1
    return n * factorial(n - 1)  # Solve a smaller factorial first.

n = int(input())
print(factorial(n))
