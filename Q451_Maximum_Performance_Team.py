"""
Q451: Maximum Performance of a Team (Greedy + Heap)
=====================================================
Problem: Choose at most k engineers. Performance = sum(speed) * min(efficiency).
Maximize performance mod 10^9+7.

Example:
    n=6, speed=[2,10,3,1,5,8], efficiency=[5,4,3,9,7,2], k=2 -> 60
    n=6, speed=[2,10,3,1,5,8], efficiency=[5,4,3,9,7,2], k=3 -> 68
"""
import heapq

def max_performance(n, speed, efficiency, k):
    MOD = 10**9 + 7
    engineers = sorted(zip(efficiency, speed), reverse=True)
    heap = []
    speed_sum = 0
    best = 0
    for eff, spd in engineers:
        heapq.heappush(heap, spd)
        speed_sum += spd
        if len(heap) > k:
            speed_sum -= heapq.heappop(heap)
        best = max(best, speed_sum * eff)
    return best % MOD

if __name__ == "__main__":
    print(max_performance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2))  # 60
    print(max_performance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))  # 68
