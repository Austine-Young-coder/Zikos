# PROBLEM: Sort non-negative integers by counting how often each appears.
# INPUT: 6 then 3 1 2 3 0 2
# OUTPUT: 0 1 2 2 3 3
# Assumption: values are small non-negative integers.

n = int(input())
numbers = list(map(int, input().split()))

if n == 0:
    print()
else:
    counts = [0] * (max(numbers) + 1)  # One counter for each possible value.

    for number in numbers:
        counts[number] += 1  # Record another occurrence.

    answer = []
    for number in range(len(counts)):
        # Repeat each value as many times as it occurred.
        answer.extend([number] * counts[number])

    print(*answer)
