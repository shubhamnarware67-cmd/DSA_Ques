"""
Q232: Fisher-Yates Shuffle (Perfect Shuffle)
==============================================
Problem: Implement an algorithm to shuffle an array uniformly at random.
Every permutation must be equally likely. O(n) time.

Example:
    [1,2,3,4,5] -> some random permutation
    reset()     -> [1,2,3,4,5] (original)
"""
import random

class Solution:
    def __init__(self, nums):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self):
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

if __name__ == "__main__":
    sol = Solution([1,2,3,4,5])
    print("Shuffled:", sol.shuffle())
    print("Reset:   ", sol.reset())
    print("Shuffled:", sol.shuffle())
