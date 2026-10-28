# PROBLEM: Sort a list from smallest to largest using Bubble Sort.
# INPUT: 5 followed by 5 numbers, for example: 5 / 4 2 5 1 3
# OUTPUT: 1 2 3 4 5

n = int(input())                         # Read how many numbers there are.
numbers = list(map(int, input().split()))  # Read the numbers.

# Compare neighbours repeatedly. Large values move to the right.
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap the two values when they are in the wrong order.
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(*numbers)  # Print the sorted numbers on one line.
