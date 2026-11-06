"""
IEEEXTREME 20.0 - ULTIMATE PYTHON 3 ALGORITHM SURVIVAL KIT (V3)
-------------------------------------------------------------------
This template contains the comprehensive A-Z algorithm reference 
extracted from the CS Academy Contest Archive taxonomy.
Sorted alphabetically for rapid contest access.
"""

import sys
import math
import bisect
import heapq
from collections import deque, defaultdict
from functools import cache

# Increase recursion depth for deep DFS/Tree traversals
sys.setrecursionlimit(200000)

# ==============================================================================
# A-B: BACKTRACKING, BFS, BINARY SEARCH, BITWISE
# ==============================================================================

# BACKTRACKING
# WHEN TO USE: Systematically generating all permutations/combinations.
# TIME COMPLEXITY: O(N!) or O(2^N)
def backtrack_permutations(elements):
    res = []
    def dfs(path, options):
        if not options:
            res.append(path)
            return
        for i in range(len(options)):
            dfs(path + [options[i]], options[:i] + options[i+1:])
    dfs([], elements)
    return res

# BREADTH-FIRST SEARCH (BFS)
# WHEN TO USE: Shortest path on unweighted graphs or flood fill.
# TIME COMPLEXITY: O(V + E)
def bfs_shortest_path(graph, start, target):
    queue = deque([(start, 0)]) # (node, distance)
    visited = {start}
    while queue:
        curr, dist = queue.popleft()
        if curr == target: return dist
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1

# BINARY SEARCH ON ANSWER
# WHEN TO USE: Optimization ("minimize the maximum"). Monotonic search space.
# TIME COMPLEXITY: O(N log(Range))
def binary_search_on_answer(low, high):
    def check(mid):
        return True # Replace with greedy validation logic
    best_ans = -1
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            best_ans = mid
            high = mid - 1  # Minimization. Use low = mid + 1 for maximization.
        else:
            low = mid + 1
    return best_ans

# BITWISE OPERATIONS (GRAY CODES & XOR)
# WHEN TO USE: Generating subsets, bitmask DP, or XOR basis.
def gray_code(n):
    # Generates the nth Gray code
    return n ^ (n >> 1)

# ==============================================================================
# C: CENTROID DECOMPOSITION, COMBINATORICS, CONVEX HULL
# ==============================================================================

# CENTROID DECOMPOSITION
# WHEN TO USE: O(N log N) path queries on trees.
# TIME COMPLEXITY: O(N log N)
def get_centroid(tree, n):
    # Simplified single centroid finder
    size = [1] * (n + 1)
    def dfs(u, p):
        is_centroid = True
        for v in tree[u]:
            if v != p:
                dfs(v, u)
                size[u] += size[v]
                if size[v] > n // 2: is_centroid = False
        if n - size[u] > n // 2: is_centroid = False
        if is_centroid: centroid[0] = u
    centroid = [-1]
    dfs(1, -1)
    return centroid[0]

# COMBINATORICS (nCr MOD p)
# WHEN TO USE: Counting arrangements under a modulo.
# TIME COMPLEXITY: O(R)
def nCr_mod(n, r, mod):
    if r > n or r < 0: return 0
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod - 2, mod)) % mod

# CONVEX HULL (MONOTONE CHAIN)
# WHEN TO USE: Smallest polygon enclosing a set of 2D points.
# TIME COMPLEXITY: O(N log N)
def convex_hull(points):
    points = sorted(points)
    if len(points) <= 1: return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

# ==============================================================================
# D: DFS, DIJKSTRA, DSU, DYNAMIC PROGRAMMING
# ==============================================================================

# DEPTH-FIRST SEARCH (DFS)
# WHEN TO USE: Deep traversal, cycle detection, connected components.
# TIME COMPLEXITY: O(V + E)
def dfs_components(n, graph):
    visited = set()
    components = []
    for i in range(1, n + 1):
        if i not in visited:
            stack = [i]
            visited.add(i)
            cluster = []
            while stack:
                curr = stack.pop()
                cluster.append(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            components.append(cluster)
    return components

# DIJKSTRA'S ALGORITHM
# WHEN TO USE: Shortest paths on weighted graphs.
# TIME COMPLEXITY: O(E log V)
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]: continue
        for neighbor, weight in graph[curr_node]:
            if curr_dist + weight < distances[neighbor]:
                distances[neighbor] = curr_dist + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
    return distances

# DISJOINT SET UNION (DSU)
# WHEN TO USE: Dynamic connectivity, Kruskal's MST.
# TIME COMPLEXITY: O(alpha(N)) ~ O(1)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]: self.rank[root_i] += 1
            return True
        return False

# DYNAMIC PROGRAMMING: BITMASK DP (TSP)
# TIME COMPLEXITY: O(2^N * N^2)
def tsp_bitmask(n, dist):
    @cache
    def dp(mask, pos):
        if mask == (1 << n) - 1: return dist[pos][0] # Return to start
        ans = float('inf')
        for nxt in range(n):
            if (mask & (1 << nxt)) == 0:
                ans = min(ans, dist[pos][nxt] + dp(mask | (1 << nxt), nxt))
        return ans
    return dp(1, 0)

# DYNAMIC PROGRAMMING: DIGIT DP
# TIME COMPLEXITY: O(Digits * States)
def solve_digit_dp(upper_bound_str):
    @cache
    def dp(idx, is_tight, running_sum):
        if idx == len(upper_bound_str): return 1 if running_sum == 10 else 0
        limit = int(upper_bound_str[idx]) if is_tight else 9
        ans = 0
        for digit in range(limit + 1):
            ans += dp(idx + 1, is_tight and (digit == limit), running_sum + digit)
        return ans
    return dp(0, True, 0)

# ==============================================================================
# E-G: EULERIAN PATH, FENWICK TREE, GAME THEORY, GAUSSIAN ELIMINATION, GREEDY
# ==============================================================================

# EULERIAN PATH (HIERHOLZER'S)
# WHEN TO USE: Tracing a continuous path through every edge exactly once.
# TIME COMPLEXITY: O(V + E)
def find_eulerian_path(start_node, graph):
    stack = [start_node]
    path = []
    while stack:
        curr = stack[-1]
        if graph[curr]:
            stack.append(graph[curr].pop())
        else:
            path.append(stack.pop())
    return path[::-1]

# FENWICK TREE (BINARY INDEXED TREE)
# WHEN TO USE: Prefix sums with point updates.
# TIME COMPLEXITY: O(log N)
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    def add(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

# GAME THEORY (NIM / SPRAGUE-GRUNDY)
# WHEN TO USE: Determining winning/losing states in impartial games.
def nim_winner(piles):
    # If XOR sum > 0, First Player wins. If == 0, Second Player wins.
    xor_sum = 0
    for p in piles: xor_sum ^= p
    return "First" if xor_sum > 0 else "Second"

# GAUSSIAN ELIMINATION (XOR BASIS)
# WHEN TO USE: Finding max XOR subset or independent vectors.
# TIME COMPLEXITY: O(N log(Max_Val))
def insert_xor_basis(basis, mask):
    for b in basis:
        mask = min(mask, mask ^ b)
    if mask > 0:
        basis.append(mask)
        basis.sort(reverse=True)

# GREEDY (INTERVAL SCHEDULING)
# WHEN TO USE: Maximize non-overlapping intervals (Sweep line variant).
# TIME COMPLEXITY: O(N log N)
def greedy_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1]) # Sort by end time
    count = 0
    last_end = -float('inf')
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count

# ==============================================================================
# H-L: HASHING, KMP, LOWEST COMMON ANCESTOR
# ==============================================================================

# HASHING (RABIN-KARP)
# WHEN TO USE: Substring comparisons in O(1) time after O(N) prep.
def compute_hash(s, p=31, m=10**9 + 9):
    hash_value = 0
    p_pow = 1
    for char in s:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value

# KMP ALGORITHM (STRING MATCHING)
# WHEN TO USE: Deterministic substring search in O(N).
def kmp_search(text, pattern):
    def compute_lps(p):
        lps = [0] * len(p)
        length, i = 0, 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0: length = lps[length - 1]
                else: i += 1
        return lps
    lps, i, j, matches = compute_lps(pattern), 0, 0, []
    while i < len(text):
        if pattern[j] == text[i]: i, j = i + 1, j + 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0: j = lps[j - 1]
            else: i += 1
    return matches

# LOWEST COMMON ANCESTOR (BINARY LIFTING)
# WHEN TO USE: Tree path distances in O(log N).
def precompute_lca(n, root, tree):
    LOG = 20
    up = [[-1] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)
    def dfs(node, parent):
        up[node][0] = parent
        for i in range(1, LOG):
            if up[node][i-1] != -1:
                up[node][i] = up[up[node][i-1]][i-1]
        for neighbor in tree[node]:
            if neighbor != parent:
                depth[neighbor] = depth[node] + 1
                dfs(neighbor, node)
    dfs(root, -1)
    return up, depth

# ==============================================================================
# M-O: MATRIX EXPONENTIATION, MAXIMUM FLOW, MEDIAN MAINTENANCE, MO'S ALGORITHM
# ==============================================================================

# MATRIX EXPONENTIATION
# WHEN TO USE: O(log N) linear recurrences for massive N.
def mat_mult(A, B, MOD):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % MOD for j in range(len(B[0]))] for i in range(len(A))]

def mat_pow(mat, p, MOD):
    res = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat))]
    base = mat
    while p:
        if p % 2 == 1: res = mat_mult(res, base, MOD)
        base = mat_mult(base, base, MOD)
        p //= 2
    return res

# MAXIMUM FLOW (DINIC'S ALGORITHM)
# WHEN TO USE: Network flow, Bipartite Matching.
# TIME COMPLEXITY: O(V^2 E)
class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.level = []
    def add_edge(self, u, v, cap):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])
    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v, cap, rev_idx in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0
    def dfs(self, u, t, flow, ptr):
        if u == t or not flow: return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed
        return 0
    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if not pushed: break
                flow += pushed
        return flow

# MEDIAN MAINTENANCE (TWO HEAPS)
# WHEN TO USE: Finding the running median dynamically.
# TIME COMPLEXITY: O(log N) per insert
class MedianFinder:
    def __init__(self):
        self.low = []  # max-heap (invert values)
        self.high = [] # min-heap
    def add_num(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    def get_median(self):
        if len(self.low) > len(self.high): return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2

# MO'S ALGORITHM (SQRT DECOMPOSITION)
# WHEN TO USE: Offline range queries without updates.
# TIME COMPLEXITY: O(Q * N^0.5)
def mos_algorithm(array, queries):
    n = len(array)
    block_size = int(n ** 0.5)
    # Queries format: (L, R, original_index)
    queries.sort(key=lambda q: (q[0] // block_size, q[1] if (q[0] // block_size) % 2 == 0 else -q[1]))
    curr_l, curr_r, curr_ans = 0, -1, 0
    answers = [0] * len(queries)
    
    for l, r, q_idx in queries:
        while curr_l > l: curr_l -= 1; curr_ans += array[curr_l] # Add logic
        while curr_r < r: curr_r += 1; curr_ans += array[curr_r] # Add logic
        while curr_l < l: curr_ans -= array[curr_l]; curr_l += 1 # Remove logic
        while curr_r > r: curr_ans -= array[curr_r]; curr_r -= 1 # Remove logic
        answers[q_idx] = curr_ans
    return answers

# ==============================================================================
# R-S: RANGE MIN QUERY, SEGMENT TREE, SIEVE, SLIDING WINDOW, SCC, SWEEP LINE
# ==============================================================================

# RANGE MINIMUM QUERY (SPARSE TABLE)
# WHEN TO USE: O(1) static range min queries after O(N log N) prep.
def build_sparse_table(arr):
    n = len(arr)
    LOG = int(math.log2(n)) + 1
    st = [[0] * LOG for _ in range(n)]
    for i in range(n): st[i][0] = arr[i]
    for j in range(1, LOG):
        for i in range(n - (1 << j) + 1):
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])
    return st

def query_sparse_table(st, L, R):
    j = int(math.log2(R - L + 1))
    return min(st[L][j], st[R - (1 << j) + 1][j])

# SEGMENT TREE
# WHEN TO USE: Range queries with active point updates.
# TIME COMPLEXITY: O(log N) updates & queries
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n): self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    def query(self, l, r):
        res = 0
        l += self.n; r += self.n
        while l < r:
            if l % 2 == 1: res += self.tree[l]; l += 1
            if r % 2 == 1: r -= 1; res += self.tree[r]
            l //= 2; r //= 2
        return res

# SIEVE OF ERATOSTHENES
# WHEN TO USE: O(N log log N) prime generation.
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i): is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

# SLIDING WINDOW (WITH DEQUE)
# WHEN TO USE: Tracking max/min in a moving window. O(N)
def sliding_window_max(arr, k):
    q = deque()
    res = []
    for i, val in enumerate(arr):
        while q and q[0] < i - k + 1: q.popleft()
        while q and arr[q[-1]] < val: q.pop()
        q.append(i)
        if i >= k - 1: res.append(arr[q[0]])
    return res

# STRONGLY CONNECTED COMPONENTS (KOSARAJU'S ALGORITHM)
# WHEN TO USE: Shrinking cyclic graphs into DAGs, 2-SAT.
def kosaraju_scc(n, edges):
    graph, rev_graph = defaultdict(list), defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)
    visited, stack = set(), []
    def dfs1(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited: dfs1(neighbor)
        stack.append(node)
    for i in range(1, n + 1):
        if i not in visited: dfs1(i)
    visited.clear()
    sccs = []
    def dfs2(node, current_scc):
        visited.add(node)
        current_scc.append(node)
        for neighbor in rev_graph[node]:
            if neighbor not in visited: dfs2(neighbor, current_scc)
    while stack:
        node = stack.pop()
        if node not in visited:
            current_scc = []
            dfs2(node, current_scc)
            sccs.append(current_scc)
    return sccs

# SWEEP LINE ALGORITHM
# WHEN TO USE: Finding maximum concurrent overlapping intervals/events.
def sweep_line_max_overlap(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda x: (x[0], x[1]))
    current_overlap, max_overlap = 0, 0
    for coord, event_type in events:
        current_overlap += event_type
        if current_overlap > max_overlap: max_overlap = current_overlap
    return max_overlap

# ==============================================================================
# T-Z: TERNARY SEARCH, TOPOLOGICAL SORT, TRIE, TWO POINTERS, Z-ALGORITHM
# ==============================================================================

# TERNARY SEARCH
# WHEN TO USE: Finding extremum (min/max) of a unimodal function.
def ternary_search(low, high):
    def f(x): return x # Replace with mathematical unimodal function
    for _ in range(200): # Fixed iterations handles precision easily
        m1 = low + (high - low) / 3
        m2 = high - (high - low) / 3
        if f(m1) < f(m2):
            low = m1
        else:
            high = m2
    return low

# TOPOLOGICAL SORT (KAHN'S ALGORITHM)
# WHEN TO USE: Ordering dependencies on Directed Acyclic Graphs.
def kahn_topological_sort(n, edges):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []
    while queue:
        curr = queue.popleft()
        topo_order.append(curr)
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0: queue.append(neighbor)
    return topo_order if len(topo_order) == n else "CYCLE DETECTED"

# TRIE (PREFIX TREE)
# WHEN TO USE: Prefix dictionary lookups or XOR Maximum searches.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children: node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

# TWO POINTERS
# WHEN TO USE: O(N) searching for sum pairs in a sorted array.
def two_pointers_target_sum(sorted_arr, target):
    l, r = 0, len(sorted_arr) - 1
    while l < r:
        curr_sum = sorted_arr[l] + sorted_arr[r]
        if curr_sum == target: return (sorted_arr[l], sorted_arr[r])
        elif curr_sum < target: l += 1
        else: r -= 1
    return None

# Z-ALGORITHM
# WHEN TO USE: String pattern matching in O(N).
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r - l] == s[r]: r += 1
            z[i], r = r - l, r - 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r - l] == s[r]: r += 1
                z[i], r = r - l, r - 1
    return z
