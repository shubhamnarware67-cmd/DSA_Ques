"""
Q252: Largest Component Size by Common Factor (Union-Find)
===========================================================
Problem: Given integer array, two values are connected if they share
a common factor > 1. Return size of largest connected component.

Example:
    [4,6,15,35] -> 4  (all connected: 4-6 via 2, 6-15 via 3, 15-35 via 5)
    [20,50,9,63] -> 2
"""

def largest_component_size(nums):
    parent = {}
    def find(x):
        if x not in parent: parent[x] = x
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        parent[find(x)] = find(y)

    for num in nums:
        d = 2
        while d * d <= num:
            if num % d == 0:
                union(num, d)
                union(num, num // d)
            d += 1

    from collections import Counter
    count = Counter(find(n) for n in nums)
    return max(count.values())

if __name__ == "__main__":
    print(largest_component_size([4,6,15,35]))   # 4
    print(largest_component_size([20,50,9,63]))  # 2
    print(largest_component_size([2,3,6,7,4,12,21,39]))  # 8
