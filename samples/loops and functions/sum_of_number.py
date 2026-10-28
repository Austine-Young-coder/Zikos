
# PROBLEM sample:
# Given N integers, calculate and print their sum.
#
# Example input:
# 5
# 2 4 6 8 10
#
# Example output:
# 30

import sys

# Read input efficiently.
assert sys.stdin is not None
input = sys.stdin.readline

def solve():
    # Read the number of integers.
    n = int(input())

    # Read the integers into a list.
    numbers = list(map(int, input().split()))

    # Start the total at zero.
    total = 0

    # Add each number to the total.
    for number in numbers:
        total += number

    # Print the final sum.
    print(total)


# Run the solution.
if __name__ == "__main__":
    solve()
