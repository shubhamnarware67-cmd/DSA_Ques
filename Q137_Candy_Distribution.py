"""
Q137: Candy (Greedy)
=====================
Problem: n children in a row with ratings. Give at least 1 candy each.
Children with higher rating than neighbors get more. Min total candies.

Example:
    [1,0,2] -> 5  (2,1,2)
    [1,2,2] -> 4  (1,2,1)
"""

def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)

if __name__ == "__main__":
    print(candy([1,0,2]))  # 5
    print(candy([1,2,2]))  # 4
    print(candy([1,3,2,2,1]))  # 7
