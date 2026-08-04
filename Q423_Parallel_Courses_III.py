"""
Q423: Parallel Courses III (Topological Sort + DP)
=====================================================
Problem: n courses with prerequisites and time[i] to complete each.
Find minimum months to complete all courses (can do multiple in parallel
once prerequisites done).

Example:
    n=3, relations=[[1,3],[2,3]], time=[3,2,5] -> 8
    n=5, relations=[[1,5],[2,5],[3,5],[3,4],[4,5]], time=[1,2,3,4,5] -> 12
"""
from collections import defaultdict, deque

def minimum_time(n, relations, time):
    graph = defaultdict(list)
    in_degree = [0] * (n+1)
    for u, v in relations:
        graph[u].append(v)
        in_degree[v] += 1

    finish_time = [0] * (n+1)
    queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])
    for i in queue:
        finish_time[i] = time[i-1]

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            finish_time[v] = max(finish_time[v], finish_time[u] + time[v-1])
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return max(finish_time)

if __name__ == "__main__":
    print(minimum_time(3, [[1,3],[2,3]], [3,2,5]))  # 8
    print(minimum_time(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1,2,3,4,5]))  # 12
