# PROBLEM: Sort numbers by inserting each value into the sorted left side.
# INPUT: 5 then 5 2 4 1 3
# OUTPUT: 1 2 3 4 5

n = int(input())
numbers = list(map(int, input().split()))

for i in range(1, n):
    current = numbers[i]  # Value we want to insert in the correct place.
    j = i - 1

    # Move larger values one position to the right.
    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = current  # Insert the saved value.

print(*numbers)
