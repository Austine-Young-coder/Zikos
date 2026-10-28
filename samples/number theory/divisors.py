# PROBLEM: Print all positive divisors of N in increasing order.
# INPUT: 12
# OUTPUT: 1 2 3 4 6 12

n = int(input())
divisors = []

for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)

print(*divisors)
