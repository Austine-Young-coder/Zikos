# PROBLEM: Find the sum of a list using recursion.
# INPUT: 4 then 2 4 6 8
# OUTPUT: 20

def add_numbers(numbers, index):
    if index == len(numbers):  # Stop when we reach the end.
        return 0
    return numbers[index] + add_numbers(numbers, index + 1)

n = int(input())
numbers = list(map(int, input().split()))
print(add_numbers(numbers, 0))
