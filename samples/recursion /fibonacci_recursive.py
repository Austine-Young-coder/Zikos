# PROBLEM: Find the Nth Fibonacci number using recursion.
# INPUT: 6
# OUTPUT: 8
# This simple version is slow for large N because it repeats work.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))
