"""
Q330: Maximum Number of Coins You Can Get (Greedy)
===================================================
Problem: 3n piles of coins. In each round: you pick pile 2, Bob picks pile 1
(largest). You can choose which piles go to which round. Max your coins.

Example:
    [2,4,1,2,7,8] -> 9   (rounds: [8,7,4] and [2,2,1]; you take 7+2=9? no wait)
    [2,4,5]        -> 4
    [9,8,7,6,5,1,2,3,4] -> 18
"""

def max_coins(piles):
    piles.sort()
    n = len(piles) // 3
    return sum(piles[n + i*2 + 1] for i in range(n))

    # Explanation: Remove n smallest (Bob always gets 1 pile).
    # From remaining 2n piles, take every 2nd (your share).

if __name__ == "__main__":
    print(max_coins([2,4,1,2,7,8]))           # 9
    print(max_coins([2,4,5]))                  # 4
    print(max_coins([9,8,7,6,5,1,2,3,4]))     # 18
