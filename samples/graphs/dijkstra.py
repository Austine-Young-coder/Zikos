# PROBLEM: Find shortest distances from start in a graph with non-negative weights.
# INPUT: N M, then M lines: a b weight, then start vertex.
# Edges are undirected. Output distances; -1 means unreachable.

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

start = int(input())
distance = [float("inf")] * n
distance[start] = 0
heap = [(0, start)]

while heap:
    current_distance, current = heapq.heappop(heap)

    if current_distance != distance[current]:
        continue  # Ignore an outdated heap entry.

    for neighbour, weight in graph[current]:
        new_distance = current_distance + weight
        if new_distance < distance[neighbour]:
            distance[neighbour] = new_distance
            heapq.heappush(heap, (new_distance, neighbour))

print(*(int(d) if d != float("inf") else -1 for d in distance))
