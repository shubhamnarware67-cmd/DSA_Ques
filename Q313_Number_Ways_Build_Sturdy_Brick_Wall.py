"""
Q313: Number of Ways to Build Sturdy Brick Wall (DP + Bitmask)
===============================================================
Problem: Build wall of height h and width n using bricks of width 1 and 2.
No vertical crack can span entire height. Count ways.

Example:
    n=3, h=2 -> 9
    n=2, h=1 -> 2
"""

def build_wall(n, h):
    MOD = 10**9 + 7

    def gen_rows(width):
        rows = []
        def build(pos, mask):
            if pos == width:
                rows.append(mask); return
            build(pos+1, mask | (1 << pos))         # Brick of width 1
            if pos+1 < width:
                build(pos+2, mask | (1 << pos+1))   # Brick of width 2
        build(0, 0)
        return rows

    def compatible(r1, r2):
        return not (r1 & r2)  # No shared crack positions

    rows = gen_rows(n)
    m = len(rows)
    adj = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if compatible(rows[i], rows[j]):
                adj[i].append(j)

    dp = [1] * m
    for _ in range(h-1):
        new_dp = [0] * m
        for i in range(m):
            for j in adj[i]:
                new_dp[j] = (new_dp[j] + dp[i]) % MOD
        dp = new_dp
    return sum(dp) % MOD

if __name__ == "__main__":
    print(build_wall(3, 2))  # 9
    print(build_wall(2, 1))  # 2
