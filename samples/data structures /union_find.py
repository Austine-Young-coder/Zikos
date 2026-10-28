# PROBLEM: Process connections and report whether two items are connected.
# INPUT: N Q, then queries: 1 a b to connect; 2 a b to check.
# Items are numbered from 0 to N-1.

n, q = map(int, input().split())
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Compress the path.
    return parent[x]

for i in range(q):
    kind, a, b = map(int, input().split())
    root_a = find(a)
    root_b = find(b)

    if kind == 1:
        parent[root_a] = root_b  # Join the groups.
    else:
        print("YES" if root_a == root_b else "NO")
