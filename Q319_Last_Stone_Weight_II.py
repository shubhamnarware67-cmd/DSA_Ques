"""
Q319: Last Stone Weight II (Subset Sum / 0-1 Knapsack)
=======================================================
Problem: Smash stones, result is |x-y|. Find minimum possible weight
of last stone. (Equivalent to: partition into 2 groups, minimize difference)

Example:
    [2,7,4,1,8,1] -> 1
    [31,26,33,21,40] -> 5
"""

def last_stone_weight_ii(stones):
    total = sum(stones)
    target = total // 2
    dp = {0}
    for stone in stones:
        dp = {s + stone for s in dp} | dp
    # Find largest sum <= target
    best = max(s for s in dp if s <= target)
    return total - 2 * best

if __name__ == "__main__":
    print(last_stone_weight_ii([2,7,4,1,8,1]))     # 1
    print(last_stone_weight_ii([31,26,33,21,40]))   # 5
