# PROBLEM: Find the next smaller value to the right of each number.
# INPUT: 4 then 4 2 5 1
# OUTPUT: 2 1 1 -1

n = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
    # If current value is smaller, it answers earlier positions.
    while stack and numbers[stack[-1]] > numbers[i]:
        old_index = stack.pop()
        answer[old_index] = numbers[i]
    stack.append(i)

print(*answer)
