# PROBLEM: Print common values and all distinct values from two lists.
# INPUT: first list: 1 2 3, second list: 2 3 4
# OUTPUT: common values then union values

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print("Common:", sorted(a & b))  # Values present in both sets.
print("All:", sorted(a | b))     # Values present in either set.
