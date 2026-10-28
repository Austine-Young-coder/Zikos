# PROBLEM: Sort numbers using Python's built-in sorting method.
# INPUT: 5 then 9 2 7 1 5
# OUTPUT: 1 2 5 7 9

n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()  # Python's built-in sort is usually the best default choice.
print(*numbers)
