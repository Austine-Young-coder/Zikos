# PROBLEM: Maximize value in a bag when you may take fractions of items.
# INPUT: 3 / weights 10 20 30 / values 60 100 120 / capacity 50
# OUTPUT: 240.0

n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())

items = []
for i in range(n):
    # Store value per weight, weight, and value.
    items.append((values[i] / weights[i], weights[i], values[i]))

items.sort(reverse=True)  # Take the best value-per-weight first.
total_value = 0

for ratio, weight, value in items:
    if capacity == 0:
        break

    if weight <= capacity:
        total_value += value  # Take the whole item.
        capacity -= weight
    else:
        total_value += ratio * capacity  # Take only the available fraction.
        capacity = 0

print(total_value)
