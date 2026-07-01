"""
Q366: IPO - Maximize Capital (Greedy + Two Heaps)
==================================================
Problem: Choose at most k projects to maximize final capital.
Each project has profit and minimum capital requirement.

Example:
    k=2, w=0, profits=[1,2,3], capital=[0,1,1] -> 4
    k=3, w=0, profits=[1,2,3], capital=[0,1,2] -> 6
"""
import heapq

def find_maximized_capital(k, w, profits, capital):
    available = []  # Max-heap by profit (negate)
    locked = sorted(zip(capital, profits))
    i = 0
    for _ in range(k):
        # Unlock all projects we can afford
        while i < len(locked) and locked[i][0] <= w:
            heapq.heappush(available, -locked[i][1])
            i += 1
        if not available: break
        w -= heapq.heappop(available)  # Gain max profit
    return w

if __name__ == "__main__":
    print(find_maximized_capital(2, 0, [1,2,3], [0,1,1]))  # 4
    print(find_maximized_capital(3, 0, [1,2,3], [0,1,2]))  # 6
