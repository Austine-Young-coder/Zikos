# PROBLEM: Determine whether an integer is prime.
# INPUT: 17
# OUTPUT: YES

n = int(input())

if n < 2:
    print("NO")
else:
    prime = True

    # A factor larger than the square root has a matching smaller factor.
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1

    print("YES" if prime else "NO")
