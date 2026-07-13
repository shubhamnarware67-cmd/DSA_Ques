"""
Q399: Detonate the Maximum Bombs (Graph BFS/DFS)
=================================================
Problem: Bombs[i]=[x,y,r]. Detonating bomb i also detonates bomb j if
distance(i,j) <= r[i]. Find max bombs detonated by triggering one.

Example:
    [[2,1,3],[6,1,4]] -> 2
    [[1,1,5],[10,10,5]] -> 1
"""
from collections import defaultdict, deque

def maximum_detonation(bombs):
    n = len(bombs)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            xi, yi, ri = bombs[i]
            xj, yj, _ = bombs[j]
            if (xi-xj)**2 + (yi-yj)**2 <= ri**2:
                graph[i].append(j)

    def bfs(start):
        visited = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb); queue.append(nb)
        return len(visited)

    return max(bfs(i) for i in range(n))

if __name__ == "__main__":
    print(maximum_detonation([[2,1,3],[6,1,4]]))     # 2
    print(maximum_detonation([[1,1,5],[10,10,5]]))   # 1
    print(maximum_detonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))  # 5
