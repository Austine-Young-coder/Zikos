# PROBLEM: Find the last index of target in a sorted list with duplicates.
# INPUT: 6 2 / 1 2 2 2 4 5
# OUTPUT: 3

n, target = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, n - 1
answer = -1

while left <= right:
    middle = (left + right) // 2
    if numbers[middle] <= target:
        if numbers[middle] == target:
            answer = middle  # Save this match and continue right.
        left = middle + 1
    else:
        right = middle - 1

print(answer)
