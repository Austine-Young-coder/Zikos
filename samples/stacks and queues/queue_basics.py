# PROBLEM: Demonstrate a first-in, first-out queue.
# INPUT: 3 then 10 20 30
# OUTPUT: First item removed is 10.

from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
queue = deque(numbers)

if queue:
    print("Removed:", queue.popleft())  # Remove the oldest item.
    print("Remaining:", list(queue))
