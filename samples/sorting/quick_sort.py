# PROBLEM: Sort a list using Quick Sort.
# INPUT: 5 then 4 2 5 1 3
# OUTPUT: 1 2 3 4 5
# This beginner version is easy to read but creates extra lists.

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]  # Choose the first value as the pivot.
    smaller = []
    equal = []
    larger = []

    # Divide values according to how they compare with the pivot.
    for number in numbers:
        if number < pivot:
            smaller.append(number)
        elif number > pivot:
            larger.append(number)
        else:
            equal.append(number)

    # Sort the smaller and larger groups, then join them.
    return quick_sort(smaller) + equal + quick_sort(larger)

n = int(input())
numbers = list(map(int, input().split()))
print(*quick_sort(numbers))
