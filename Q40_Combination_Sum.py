"""
Q40: Combination Sum - Backtracking
=====================================
Problem: Given an array of distinct integers candidates and a target,
return all unique combinations where the chosen numbers sum to target.
The same number may be chosen unlimited times.

Example:
    candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
"""

def combination_sum(candidates, target):
    result = []
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(list(current))
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    backtrack(0, [], target)
    return result

if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))   # [[2,2,3],[7]]
    print(combination_sum([2, 3, 5], 8))       # [[2,2,2,2],[2,3,3],[3,5]]
