# PROBLEM: Print the multiplication table of N from 1 to 10.
# INPUT: 3
# OUTPUT: 3 x 1 = 3 ... 3 x 10 = 30

n = int(input())

for i in range(1, 11):
    answer = n * i
    print(n, "x", i, "=", answer)
