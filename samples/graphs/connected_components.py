# PROBLEM: Count connected components in an undirected graph.
# INPUT: N M, followed by M undirected edges.

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
components = 0

for start in range(n):
    if visited[start]:
        continue

    components += 1
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()
        for neighbour in graph[current]:
            if not visited[neighbour]:
                visited[neighbour] = True
                stack.append(neighbour)

print(components)
