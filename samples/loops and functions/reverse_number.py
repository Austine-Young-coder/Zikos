# PROBLEM: Reverse the digits of a non-negative integer.
# INPUT: 1234
# OUTPUT: 4321

n = int(input())
reversed_number = 0

while n > 0:
    last_digit = n % 10  # Get the rightmost digit.
    reversed_number = reversed_number * 10 + last_digit
    n = n // 10  # Remove the digit we just used.

print(reversed_number)
