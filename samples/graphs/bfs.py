# PROBLEM: Visit all vertices reachable from a starting vertex using BFS.
# INPUT: N M, then M undirected edges, then start vertex.
# Vertices are numbered from 0 to N-1.

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # Remove this line for a directed graph.

start = int(input())
visited = [False] * n
queue = deque([start])
visited[start] = True
order = []

while queue:
    current = queue.popleft()
    order.append(current)

    for neighbour in graph[current]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)

print(*order)
