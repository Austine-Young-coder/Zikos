# PROBLEM: Visit reachable vertices using Depth-First Search.
# INPUT: N M, then M undirected edges, then start vertex.

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = int(input())
visited = [False] * n
order = []
stack = [start]

while stack:
    current = stack.pop()

    if visited[current]:
        continue

    visited[current] = True
    order.append(current)

    # Reverse neighbours so the traversal order is easier to follow.
    for neighbour in reversed(graph[current]):
        if not visited[neighbour]:
            stack.append(neighbour)

print(*order)
