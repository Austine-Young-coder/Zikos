# PROBLEM: Find the total weight of a minimum spanning tree.
# INPUT: N M, followed by M lines: a b weight. Graph is undirected.
# Output -1 if the graph is disconnected.

n, m = map(int, input().split())
edges = []

for i in range(m):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

edges.sort()  # Consider edges from lowest weight to highest.
parent = list(range(n))

def find(vertex):
    # Follow parent links until reaching the representative.
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex

total = 0
used = 0

for weight, a, b in edges:
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_a] = root_b  # Join the two components.
        total += weight
        used += 1

if n == 0 or used == n - 1:
    print(total)
else:
    print(-1)
