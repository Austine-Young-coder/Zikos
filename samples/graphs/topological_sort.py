# PROBLEM: Output a topological order of a directed acyclic graph (DAG).
# INPUT: N M, followed by M directed edges a b meaning a comes before b.
# If a cycle exists, print IMPOSSIBLE.

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
indegree = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for vertex in range(n):
    if indegree[vertex] == 0:
        queue.append(vertex)

order = []
while queue:
    current = queue.popleft()
    order.append(current)

    for neighbour in graph[current]:
        indegree[neighbour] -= 1
        if indegree[neighbour] == 0:
            queue.append(neighbour)

if len(order) == n:
    print(*order)
else:
    print("IMPOSSIBLE")
