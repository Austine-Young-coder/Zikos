# PROBLEM: Every number appears twice except one; find the unique number.
# INPUT: 5 then 4 1 2 1 2
# OUTPUT: 4

n = int(input())
numbers = list(map(int, input().split()))
answer = 0

# XOR of equal values is zero, so pairs cancel out.
for number in numbers:
    answer = answer ^ number

print(answer)
