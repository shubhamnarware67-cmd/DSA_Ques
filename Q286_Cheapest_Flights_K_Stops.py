"""
Q286: Cheapest Flights Within K Stops (Bellman-Ford / BFS)
===========================================================
Problem: Find cheapest price from src to dst with at most k stops.
Return -1 if no such route.

Example:
    n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1 -> 200
"""

def find_cheapest_price(n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0
    for _ in range(k+1):
        temp = prices[:]
        for u, v, w in flights:
            if prices[u] != float('inf') and prices[u] + w < temp[v]:
                temp[v] = prices[u] + w
        prices = temp
    return prices[dst] if prices[dst] != float('inf') else -1

if __name__ == "__main__":
    print(find_cheapest_price(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))  # 200
    print(find_cheapest_price(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))  # 500
