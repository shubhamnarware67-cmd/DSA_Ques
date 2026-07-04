"""
Q377: Cutting Ribbons (Binary Search)
=======================================
Problem: Cut ribbons into k pieces of same positive length. Maximize length.

Example:
    ribbons=[9,7,5], k=3 -> 5   (9->5+4, 7->5+2, 5->5 = three 5s)
    ribbons=[7,5,9], k=4 -> 4   (9->4+4+1, 7->4+3, 5->4+1 = four 4s)
"""

def max_length(ribbons, k):
    def can_cut(length):
        return sum(r // length for r in ribbons) >= k

    lo, hi = 1, max(ribbons)
    result = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_cut(mid):
            result = mid; lo = mid + 1
        else:
            hi = mid - 1
    return result

if __name__ == "__main__":
    print(max_length([9,7,5], 3))   # 5
    print(max_length([7,5,9], 4))   # 4
    print(max_length([5,7,9], 22))  # 1
