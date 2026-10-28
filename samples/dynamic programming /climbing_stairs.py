# PROBLEM: Count ways to climb n stairs if each move is 1 or 2 steps.
# INPUT: 4
# OUTPUT: 5

n = int(input())

# There is one way to climb zero stairs and one way to climb one stair.
ways = [0] * (n + 1)
ways[0] = 1

for step in range(1, n + 1):
    ways[step] += ways[step - 1]  # Arrive from one step below.
    if step >= 2:
        ways[step] += ways[step - 2]  # Or arrive from two steps below.

print(ways[n])
