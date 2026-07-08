"""
Q381: Fruit Into Baskets (Sliding Window — At Most 2 Types)
============================================================
Problem: Pick fruits with only 2 baskets (each holds 1 type).
Find max fruits you can collect from contiguous subarray.

Example:
    [1,2,1]       -> 3
    [0,1,2,2]     -> 3
    [1,2,3,2,2]   -> 4
"""
from collections import defaultdict

def total_fruit(fruits):
    basket = defaultdict(int)
    left = result = 0
    for right, f in enumerate(fruits):
        basket[f] += 1
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        result = max(result, right - left + 1)
    return result

if __name__ == "__main__":
    print(total_fruit([1,2,1]))      # 3
    print(total_fruit([0,1,2,2]))    # 3
    print(total_fruit([1,2,3,2,2]))  # 4
