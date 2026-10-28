# PROBLEM: Schedule jobs with deadlines and profits, one unit of time each.
# Input: N, then N lines containing deadline and profit.
# Output: maximum total profit.

n = int(input())
jobs = []

for i in range(n):
    deadline, profit = map(int, input().split())
    jobs.append((profit, deadline))

jobs.sort(reverse=True)  # Consider the most profitable jobs first.
latest = max((job[1] for job in jobs), default=0)
slots = [False] * (latest + 1)
total_profit = 0

for profit, deadline in jobs:
    # Find the latest free time slot before this job's deadline.
    for time in range(min(deadline, latest), 0, -1):
        if not slots[time]:
            slots[time] = True
            total_profit += profit
            break

print(total_profit)
