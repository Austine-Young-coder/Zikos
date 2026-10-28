# PROBLEM: Count how many times target appears in a list.
# INPUT: 6 2 / 1 2 2 2 4 5
# OUTPUT: 3

n, target = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0

for number in numbers:
    if number == target:
        count += 1  # Increase the count for every match.

print(count)
