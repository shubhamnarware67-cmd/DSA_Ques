"""
Q218: Hamiltonian Path / Traveling Salesman (Bitmask DP)
=========================================================
Problem: Find shortest Hamiltonian path visiting all nodes exactly once.
Classic TSP with bitmask DP. O(n^2 * 2^n).

Example:
    dist=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    Shortest tour = 80  (0->1->3->2->0)
"""

def tsp_bitmask(dist):
    n = len(dist)
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at node 0, visited = {0}
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask >> u & 1): continue
            if dp[mask][u] == INF: continue
            for v in range(n):
                if mask >> v & 1: continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
    full = (1 << n) - 1
    return min(dp[full][u] + dist[u][0] for u in range(n))

if __name__ == "__main__":
    dist = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    print(f"Min TSP tour: {tsp_bitmask(dist)}")  # 80
