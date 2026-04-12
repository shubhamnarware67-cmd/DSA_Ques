"""
Q38: Subsets (Power Set) - Backtracking
=========================================
Problem: Given an integer array of unique elements,
return all possible subsets (the power set).

Example:
    Input:  [1, 2, 3]
    Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
"""

def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result

if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    print(f"Total subsets: {len(subsets([1,2,3]))}")  # 8
