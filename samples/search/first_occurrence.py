# PROBLEM: Find the first index of target in a sorted list with duplicates.
# INPUT: 6 2 / 1 2 2 2 4 5
# OUTPUT: 1

n, target = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, n - 1
answer = -1

while left <= right:
    middle = (left + right) // 2
    if numbers[middle] >= target:
        if numbers[middle] == target:
            answer = middle  # Save this match and continue left.
        right = middle - 1
    else:
        left = middle + 1

print(answer)
