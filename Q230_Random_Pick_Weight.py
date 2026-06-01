"""
Q230: Random Pick with Weight (Prefix Sum + Binary Search)
============================================================
Problem: Given array w where w[i] is weight of index i, implement
pickIndex() which randomly picks index with probability w[i]/sum(w).

Example:
    w=[1,3] -> pickIndex() returns 0 with prob 0.25, 1 with prob 0.75
"""
import random
import bisect

class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)

if __name__ == "__main__":
    sol = Solution([1, 3])
    results = [sol.pickIndex() for _ in range(1000)]
    print(f"Index 0: {results.count(0)/10:.1f}%")  # ~25%
    print(f"Index 1: {results.count(1)/10:.1f}%")  # ~75%
