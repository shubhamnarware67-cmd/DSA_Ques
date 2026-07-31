"""
Q415: Minimum Cost to Make Array Equal (Weighted Median)
==========================================================
Problem: Make all elements equal to some target. Cost of changing 
nums[i] to target = |nums[i]-target| * cost[i]. Minimize total cost.

Example:
    nums=[1,3,5,2], cost=[2,3,1,14] -> 8
    nums=[2,3,1,14], cost=[1,3,5,2] -> 1
"""

def min_cost(nums, cost):
    pairs = sorted(zip(nums, cost))
    total_cost = sum(cost)
    target_idx = 0
    cum = 0
    for i, (n, c) in enumerate(pairs):
        cum += c
        if cum * 2 >= total_cost:
            target_idx = i
            break
    target = pairs[target_idx][0]
    return sum(abs(n - target) * c for n, c in pairs)

if __name__ == "__main__":
    print(min_cost([1,3,5,2], [2,3,1,14]))   # 8
    print(min_cost([2,3,1,14], [1,3,5,2]))   # 1
