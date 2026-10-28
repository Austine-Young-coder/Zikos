# PROBLEM: Add N integers.
# INPUT: 4 then 2 4 6 8
# OUTPUT: 20

n = int(input())
numbers = list(map(int, input().split()))
total = 0

for number in numbers:
    total += number

print(total)
