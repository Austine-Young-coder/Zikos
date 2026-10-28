# PROBLEM: Sort numbers by repeatedly selecting the smallest remaining value.
# INPUT: 5 then 9 2 7 1 5
# OUTPUT: 1 2 5 7 9

n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    smallest_index = i  # Assume the current position has the smallest value.

    # Look through the remaining unsorted values.
    for j in range(i + 1, n):
        if numbers[j] < numbers[smallest_index]:
            smallest_index = j

    # Put the smallest value at position i.
    numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

print(*numbers)
