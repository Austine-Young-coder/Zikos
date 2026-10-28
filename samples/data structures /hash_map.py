# PROBLEM: Store names and scores, then print the score for a name.
# INPUT: 3, then lines Alice 10 / Bob 15 / Eve 12, then Bob
# OUTPUT: 15

n = int(input())
scores = {}

for i in range(n):
    name, score = input().split()
    scores[name] = int(score)  # Save each score under its name.

wanted = input().strip()
print(scores.get(wanted, "NOT FOUND"))
