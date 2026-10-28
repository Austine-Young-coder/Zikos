# PROBLEM: Maximize total value without exceeding a weight limit.
# INPUT: 3 / weights: 2 3 4 / values: 4 5 6 / capacity: 5
# OUTPUT: 9
# Input format: N, then N weights, then N values, then capacity.

n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())

# dp[w] is the best value possible with capacity w.
dp = [0] * (capacity + 1)

for i in range(n):
    # Go backwards so the same item is not used more than once.
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

print(dp[capacity])
