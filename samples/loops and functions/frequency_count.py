# PROBLEM: Count how often each integer appears.
# INPUT: 5 then 2 3 2 1 3
# OUTPUT: Counts for 1, 2 and 3.

n = int(input())
numbers = list(map(int, input().split()))
counts = {}

for number in numbers:
    # Start a new count at zero, then add one.
    if number not in counts:
        counts[number] = 0
    counts[number] += 1

for number in sorted(counts):
    print(number, counts[number])
