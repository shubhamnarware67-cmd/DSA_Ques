"""
Q248: Paint House (DP)
=======================
Problem: Paint n houses with 3 colors (cost[i][j] = cost of painting house i
with color j). Adjacent houses must have different colors. Find min cost.

Example:
    costs=[[17,2,17],[16,16,5],[14,3,19]] -> 10  (paint: 1,2,1 = 2+5+3)
"""

def min_cost(costs):
    if not costs: return 0
    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][0], costs[i-1][1])
    return min(costs[-1])

def min_cost_k_colors(costs, k):
    """Generalized to k colors using O(nk) DP"""
    if not costs: return 0
    prev = costs[0][:]
    for i in range(1, len(costs)):
        curr = []
        for j in range(k):
            min_prev = min(prev[m] for m in range(k) if m != j)
            curr.append(costs[i][j] + min_prev)
        prev = curr
    return min(prev)

if __name__ == "__main__":
    print(min_cost([[17,2,17],[16,16,5],[14,3,19]]))   # 10
    print(min_cost_k_colors([[17,2,17],[16,16,5],[14,3,19]], 3))  # 10
