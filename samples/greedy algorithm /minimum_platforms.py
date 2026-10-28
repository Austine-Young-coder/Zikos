# PROBLEM: Find the minimum train platforms needed for arrival/departure times.
# INPUT: 3 / arrivals 900 940 950 / departures 910 1200 1120
# OUTPUT: 2
# Times are integers in HHMM format.

n = int(input())
arrivals = sorted(map(int, input().split()))
departures = sorted(map(int, input().split()))

i = 0
j = 0
platforms = 0
maximum = 0

while i < n and j < n:
    if arrivals[i] <= departures[j]:
        platforms += 1
        maximum = max(maximum, platforms)
        i += 1
    else:
        platforms -= 1
        j += 1

print(maximum)
