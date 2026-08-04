"""
Q424: Count Ways to Build Rooms in an Ant Colony (Combinatorics + DFS)
=========================================================================
Problem: Tree structure. Each room (except 0) has a prevRoom built before it.
Count number of valid build orders. Mod 10^9+7.

Example:
    prevRoom=[-1,0,1] -> 1
    prevRoom=[-1,0,0,1,2] -> 6
"""
from collections import defaultdict
from math import factorial

def waysToBuildRooms(prevRoom):
    MOD = 10**9 + 7
    n = len(prevRoom)
    children = defaultdict(list)
    for i in range(1, n):
        children[prevRoom[i]].append(i)

    def dfs(node):
        # Returns (subtree_size, ways)
        size = 1
        ways = 1
        sizes = []
        for child in children[node]:
            csize, cways = dfs(child)
            sizes.append(csize)
            ways = ways * cways % MOD
            size += csize
        # Multiply by multinomial coefficient
        numerator = factorial(size - 1)
        denom = 1
        for s in sizes:
            denom *= factorial(s)
        ways = ways * (numerator // denom) % MOD
        return size, ways

    return dfs(0)[1]

if __name__ == "__main__":
    print(waysToBuildRooms([-1,0,1]))         # 1
    print(waysToBuildRooms([-1,0,0,1,2]))     # 6
