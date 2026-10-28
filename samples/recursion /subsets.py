# PROBLEM: Print every subset of a list of distinct integers.
# INPUT: 3 then 1 2 3
# OUTPUT: One possible order: [], [3], [2], [2,3], ...

def build_subsets(numbers, index, chosen):
    if index == len(numbers):
        print(chosen)
        return

    # First, do not include the current number.
    build_subsets(numbers, index + 1, chosen)

    # Then, include the current number.
    build_subsets(numbers, index + 1, chosen + [numbers[index]])

n = int(input())
numbers = list(map(int, input().split()))
build_subsets(numbers, 0, [])
