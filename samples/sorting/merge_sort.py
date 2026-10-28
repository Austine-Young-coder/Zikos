# PROBLEM: Sort a list using Merge Sort, which splits and merges lists.
# INPUT: 5 then 4 2 5 1 3
# OUTPUT: 1 2 3 4 5

def merge_sort(numbers):
    # A list with zero or one value is already sorted.
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])   # Sort the left half.
    right = merge_sort(numbers[middle:])  # Sort the right half.

    result = []
    i = 0
    j = 0

    # Take the smaller next value from either half.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any values left over in either half.
    result.extend(left[i:])
    result.extend(right[j:])
    return result

n = int(input())
numbers = list(map(int, input().split()))
print(*merge_sort(numbers))
