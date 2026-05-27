"""
Q209: Longest Subarray of 1s After Deleting One Element
=========================================================
Problem: Given binary array, delete one element. Return length of
longest subarray containing only 1s.

Example:
    [1,1,0,1]         -> 3
    [0,1,1,1,0,1,1,0,1] -> 5
    [1,1,1]            -> 2  (must delete one)
"""

def longest_subarray(nums):
    left = zeros = result = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        result = max(result, right - left)  # -1 because we delete one
    return result

if __name__ == "__main__":
    print(longest_subarray([1,1,0,1]))            # 3
    print(longest_subarray([0,1,1,1,0,1,1,0,1]))  # 5
    print(longest_subarray([1,1,1]))               # 2
