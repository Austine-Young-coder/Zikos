# PROBLEM: Find the smallest and largest number in a non-empty list.
# INPUT: 5 then 8 2 9 1 4
# OUTPUT: 1 9

n = int(input())
numbers = list(map(int, input().split()))

smallest = numbers[0]
largest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

print(smallest, largest)
