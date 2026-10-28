# PROBLEM: Calculate N! modulo M.
# INPUT: 5 7
# OUTPUT: 1 because 5! = 120 and 120 % 7 = 1

n, m = map(int, input().split())
answer = 1

for number in range(1, n + 1):
    answer = (answer * number) % m  # Keep the value small each step.

print(answer)
