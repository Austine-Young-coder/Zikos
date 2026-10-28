# PROBLEM: Find the length of the longest common subsequence of two strings.
# INPUT: ABCD / ACBD
# OUTPUT: 3

a = input().strip()
b = input().strip()
rows = len(a) + 1
cols = len(b) + 1

# dp[i][j] stores the answer for the first i and j characters.
dp = [[0] * cols for _ in range(rows)]

for i in range(1, rows):
    for j in range(1, cols):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # Ignore one character from either string.
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
