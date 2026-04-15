"""
Q56: Majority Element (Boyer-Moore Voting)
==========================================
Problem: Given array of size n, return the element that appears
more than n/2 times. (Always exists)

Example:
    [3,2,3]       -> 3
    [2,2,1,1,1,2,2] -> 2
"""

def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

if __name__ == "__main__":
    print(majority_element([3,2,3]))           # 3
    print(majority_element([2,2,1,1,1,2,2]))   # 2
