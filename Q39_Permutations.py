"""
Q39: Permutations - Backtracking
==================================
Problem: Given an array nums of distinct integers,
return all possible permutations.

Example:
    Input:  [1, 2, 3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

def permute(nums):
    result = []
    def backtrack(current, remaining):
        if not remaining:
            result.append(list(current))
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()
    backtrack([], nums)
    return result

if __name__ == "__main__":
    perms = permute([1, 2, 3])
    for p in perms:
        print(p)
    print(f"Total: {len(perms)}")  # 6
