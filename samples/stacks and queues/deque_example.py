# PROBLEM: Demonstrate adding and removing items at both ends of a deque.
# INPUT: 3 then 10 20 30
# OUTPUT: Show the deque after operations.

from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
items = deque(numbers)

items.appendleft(5)  # Add at the front.
items.append(40)     # Add at the back.
print(list(items))

items.popleft()      # Remove from the front.
items.pop()          # Remove from the back.
print(list(items))
