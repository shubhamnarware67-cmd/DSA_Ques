"""
Q317: Perfect Squares (BFS / DP)
===================================
Problem: Given n, return minimum number of perfect squares that sum to n.

Example:
    n=12 -> 3  (4+4+4)
    n=13 -> 2  (4+9)
"""

def num_squares(n):
    # DP
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    squares = [i*i for i in range(1, int(n**0.5)+1)]
    for i in range(1, n+1):
        for sq in squares:
            if sq > i: break
            dp[i] = min(dp[i], dp[i-sq] + 1)
    return dp[n]

def num_squares_bfs(n):
    # BFS — guaranteed to find shortest path
    from collections import deque
    squares = [i*i for i in range(1, int(n**0.5)+1)]
    queue = deque([(n, 0)])
    visited = {n}
    while queue:
        num, steps = queue.popleft()
        for sq in squares:
            nxt = num - sq
            if nxt == 0: return steps + 1
            if nxt > 0 and nxt not in visited:
                visited.add(nxt); queue.append((nxt, steps+1))

if __name__ == "__main__":
    print(num_squares(12))      # 3
    print(num_squares(13))      # 2
    print(num_squares_bfs(12))  # 3
