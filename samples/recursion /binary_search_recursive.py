# PROBLEM: Find target in a sorted list using recursive binary search.
# INPUT: 5 7 / 1 3 5 7 9
# OUTPUT: 3

def search(numbers, target, left, right):
    if left > right:
        return -1  # The search range is empty.

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle
    if numbers[middle] < target:
        return search(numbers, target, middle + 1, right)
    return search(numbers, target, left, middle - 1)

n, target = map(int, input().split())
numbers = list(map(int, input().split()))
print(search(numbers, target, 0, n - 1))
