# PROBLEM: Print the first index of target, or -1 if it is not present.
# INPUT: 5 / 4 8 2 9 6 / 9
# OUTPUT: 3

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
answer = -1

for i in range(n):  # Check positions from left to right.
    if numbers[i] == target:
        answer = i
        break  # Stop at the first match.

print(answer)
