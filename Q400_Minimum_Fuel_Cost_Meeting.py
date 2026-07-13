"""
Q400: Minimum Fuel Cost to Report to the Capital (DFS + Greedy)
================================================================
Problem: Tree with n cities. People travel to city 0. Cars hold 'seats'
people. Fuel cost = 1 per edge. Minimize total fuel used.

Example:
    roads=[[0,1],[0,2],[0,3]], seats=5 -> 3
    roads=[[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats=2 -> 7
"""

def minimum_fuel_cost(roads, seats):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v); graph[v].append(u)

    fuel = [0]

    def dfs(node, parent):
        people = 1  # This node's representative
        for child in graph[node]:
            if child != parent:
                people += dfs(child, node)
        if node != 0:
            import math
            fuel[0] += math.ceil(people / seats)
        return people

    dfs(0, -1)
    return fuel[0]

if __name__ == "__main__":
    print(minimum_fuel_cost([[0,1],[0,2],[0,3]], 5))  # 3
    print(minimum_fuel_cost([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2))  # 7
    print(minimum_fuel_cost([], 1))  # 0
