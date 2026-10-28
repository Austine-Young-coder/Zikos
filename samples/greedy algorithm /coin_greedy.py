# PROBLEM: Make an amount using the largest coin first.
# INPUT: 3 / coins 1 5 10 / amount 28
# OUTPUT: 6 coins (10+10+5+1+1+1)
# NOTE: This greedy method is not optimal for every coin system.

n = int(input())
coins = list(map(int, input().split()))
amount = int(input())
coins.sort(reverse=True)
count = 0

for coin in coins:
    # Use as many coins of this value as possible.
    count += amount // coin
    amount = amount % coin

if amount == 0:
    print(count)
else:
    print(-1)  # The coins could not make the exact amount.
