"""
Q92: Next Permutation
======================
Problem: Find next lexicographically greater permutation in-place.
If no such exists, rearrange to lowest order (sorted ascending).

Example:
    [1,2,3] -> [1,3,2]
    [3,2,1] -> [1,2,3]
    [1,1,5] -> [1,5,1]
"""

def next_permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    # Reverse from i+1 to end
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1; right -= 1

if __name__ == "__main__":
    a = [1,2,3]; next_permutation(a); print(a)  # [1,3,2]
    b = [3,2,1]; next_permutation(b); print(b)  # [1,2,3]
    c = [1,1,5]; next_permutation(c); print(c)  # [1,5,1]
