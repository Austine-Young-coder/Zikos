# PROBLEM: Choose the maximum number of activities that do not overlap.
# INPUT: 4 then lines: 1 3 / 2 5 / 4 6 / 6 8
# OUTPUT: 3

n = int(input())
activities = []

for i in range(n):
    start, finish = map(int, input().split())
    activities.append([start, finish])

activities.sort(key=lambda activity: activity[1])  # Earliest finish first.
count = 0
last_finish = None

for start, finish in activities:
    if last_finish is None or start >= last_finish:
        count += 1
        last_finish = finish

print(count)
