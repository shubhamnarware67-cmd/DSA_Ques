"""
Q378: Minimum Speed to Arrive on Time (Binary Search)
======================================================
Problem: n trains each covering 1 unit distance. Speed is integer.
Each except last must travel complete hours. Find min speed to arrive in time.

Example:
    dist=[1,3,2], hour=6  -> 1
    dist=[1,3,2], hour=2.7 -> 3
    dist=[1,3,2], hour=1.9 -> -1
"""
import math

def min_speed_on_time(dist, hour):
    if len(dist) > math.ceil(hour): return -1

    def feasible(speed):
        total = 0.0
        for i, d in enumerate(dist):
            if i < len(dist)-1:
                total += math.ceil(d / speed)
            else:
                total += d / speed
        return total <= hour

    lo, hi = 1, 10**7
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid): hi = mid
        else: lo = mid + 1
    return lo if feasible(lo) else -1

if __name__ == "__main__":
    print(min_speed_on_time([1,3,2], 6))    # 1
    print(min_speed_on_time([1,3,2], 2.7))  # 3
    print(min_speed_on_time([1,3,2], 1.9))  # -1
