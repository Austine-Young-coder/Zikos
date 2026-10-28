# PROBLEM: Demonstrate adding to and removing from a stack.
# INPUT: 3 then 10 20 30
# OUTPUT: Top item, then popped item.

n = int(input())
stack = list(map(int, input().split()))

# The last list item is the top of this stack.
if stack:
    print("Top:", stack[-1])
    removed = stack.pop()
    print("Removed:", removed)
    print("Remaining:", stack)
