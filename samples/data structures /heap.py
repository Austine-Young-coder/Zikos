# PROBLEM: Print and remove the smallest value using a min-heap.
# INPUT: 5 then 7 2 9 1 4
# OUTPUT: 1

import heapq

n = int(input())
numbers = list(map(int, input().split()))

heapq.heapify(numbers)  # Rearrange the list into a min-heap.
smallest = heapq.heappop(numbers)
print(smallest)
