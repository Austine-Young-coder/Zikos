# PROBLEM: Find x such that (a*x) % m == 1, if an inverse exists.
# INPUT: 3 7
# OUTPUT: 5
# This simple version checks every possible x and is for learning.

a, m = map(int, input().split())
answer = -1

for x in range(1, m):
    if (a * x) % m == 1:
        answer = x
        break

print(answer)  # -1 means no inverse was found.
