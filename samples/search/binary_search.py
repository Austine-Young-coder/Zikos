# PROBLEM: Find target in a sorted list; print its index or -1.
# INPUT: 5 7 / 1 3 5 7 9
# OUTPUT: 3
# IMPORTANT: The list must already be sorted.

n, target = map(int, input().split())
numbers = list(map(int, input().split()))
left = 0
right = n - 1
answer = -1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        answer = middle
        break
    elif numbers[middle] < target:
        left = middle + 1  # Target can only be in the right half.
    else:
        right = middle - 1  # Target can only be in the left half.

print(answer)
