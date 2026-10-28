# PROBLEM: For each number, find the next greater number to its right.
# INPUT: 4 then 4 5 2 10
# OUTPUT: 5 10 10 -1

n = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
    # Resolve earlier numbers smaller than this number.
    while stack and numbers[stack[-1]] < numbers[i]:
        old_index = stack.pop()
        answer[old_index] = numbers[i]
    stack.append(i)  # Save this index for later.

print(*answer)
