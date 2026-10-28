# PROBLEM: Answer range-sum queries and update one array value.
# INPUT: N, N numbers, Q, then queries:
# 1 index value = update; 2 left right = sum inclusive.
# Indices are zero-based.

n = int(input())
numbers = list(map(int, input().split()))
q = int(input())

# Simple beginner version: use a loop for each range sum.
# This is not a fast segment tree, but shows the query behavior.
for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        index, value = query[1], query[2]
        numbers[index] = value
    else:
        left, right = query[1], query[2]
        print(sum(numbers[left:right + 1]))
