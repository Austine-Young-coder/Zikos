# PROBLEM: Print every prime number from 2 through N.
# INPUT: 10
# OUTPUT: 2 3 5 7

n = int(input())
is_prime = [True] * (n + 1)

if n >= 0:
    is_prime[0] = False
if n >= 1:
    is_prime[1] = False

p = 2
while p * p <= n:
    if is_prime[p]:
        # Mark multiples of p as not prime.
        multiple = p * p
        while multiple <= n:
            is_prime[multiple] = False
            multiple += p
    p += 1

answer = []
for number in range(2, n + 1):
    if is_prime[number]:
        answer.append(number)

print(*answer)
