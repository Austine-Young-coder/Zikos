# PROBLEM: Find the fewest coins needed to make amount using given coin values.
# INPUT: 3 / 1 2 5 / 11
# OUTPUT: 3 (11 = 5 + 5 + 1)
# Input format: number of coin types, coin values, target amount.

n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

# dp[value] stores the minimum coins needed for that value.
dp = [amount + 1] * (amount + 1)
dp[0] = 0

for value in range(1, amount + 1):
    for coin in coins:
        if coin <= value:
            dp[value] = min(dp[value], dp[value - coin] + 1)

if dp[amount] == amount + 1:
    print(-1)  # The amount cannot be made from these coins.
else:
    print(dp[amount])
