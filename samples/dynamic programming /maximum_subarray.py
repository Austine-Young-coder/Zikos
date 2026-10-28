# PROBLEM: Find the largest sum of a non-empty contiguous subarray.
# INPUT: 5 / -2 3 -1 4 -5
# OUTPUT: 6

n = int(input())
numbers = list(map(int, input().split()))

current = numbers[0]  # Best subarray ending at the first value.
best = numbers[0]     # Best answer seen so far.

for number in numbers[1:]:
    # Start fresh, or extend the previous subarray.
    current = max(number, current + number)
    best = max(best, current)

print(best)
