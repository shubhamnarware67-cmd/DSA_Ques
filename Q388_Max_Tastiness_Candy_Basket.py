"""
Q388: Maximum Tastiness of Candy Basket (Binary Search)
========================================================
Problem: Pick k candies from n to form basket. Maximize minimum
absolute difference between any two candy prices.

Example:
    price=[13,5,1,8,21,2], k=3 -> 8  (pick 1,8,21? min diff=7. pick 1,9,21? 
     sorted: [1,2,5,8,13,21]. k=3: try 8: 1+8=9≤21, 9+8=17≤21 -> yes! -> 8)
    price=[1,3,1], k=2 -> 2
"""

def maximum_tastiness(price, k):
    price.sort()

    def can_pick(min_diff):
        count = 1
        last = price[0]
        for i in range(1, len(price)):
            if price[i] - last >= min_diff:
                count += 1
                last = price[i]
        return count >= k

    lo, hi = 0, price[-1] - price[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can_pick(mid): lo = mid
        else: hi = mid - 1
    return lo

if __name__ == "__main__":
    print(maximum_tastiness([13,5,1,8,21,2], 3))  # 8
    print(maximum_tastiness([1,3,1], 2))            # 2
    print(maximum_tastiness([7,7,7,7], 2))          # 0
