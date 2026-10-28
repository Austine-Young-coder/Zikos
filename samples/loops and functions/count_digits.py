# PROBLEM: Count the digits in an integer.
# INPUT: 5024
# OUTPUT: 4

n = abs(int(input()))  # abs() also handles negative integers.
if n == 0:
    print(1)  # Zero has one digit.
else:
    count = 0
    while n > 0:
        count += 1
        n = n // 10  # Remove the last digit.
    print(count)
