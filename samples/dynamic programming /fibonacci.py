# PROBLEM: Print the Nth Fibonacci number: 0, 1, 1, 2, 3, 5...
# INPUT: 7
# OUTPUT: 13

n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a, b = 0, 1  # The two previous Fibonacci values.
    for i in range(2, n + 1):
        a, b = b, a + b  # Move forward one position.
    print(b)
