# PROBLEM: Print the prime factors of a positive integer, with repeats.
# INPUT: 60
# OUTPUT: 2 2 3 5

n = int(input())
factors = []
divisor = 2

# Try dividing by each possible divisor.
while divisor * divisor <= n:
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1

# Any remaining number greater than 1 is prime.
if n > 1:
    factors.append(n)

print(*factors)
