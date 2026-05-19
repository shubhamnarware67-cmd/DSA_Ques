"""
Q188: Longest Consecutive Sequence
=====================================
Problem: Given unsorted array, return length of longest consecutive
elements sequence. Must be O(n).

Example:
    [100,4,200,1,3,2]   -> 4  ([1,2,3,4])
    [0,3,7,2,5,8,4,6,0,1] -> 9
"""

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

if __name__ == "__main__":
    print(longest_consecutive([100,4,200,1,3,2]))       # 4
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))   # 9
