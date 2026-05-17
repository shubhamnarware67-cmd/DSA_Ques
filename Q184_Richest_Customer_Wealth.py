"""
Q184: Richest Customer Wealth
==============================
Problem: Given m x n integer grid accounts where accounts[i][j] is
bank j's amount for customer i. Return maximum wealth (row sum).

Example:
    [[1,2,3],[3,2,1]]    -> 6
    [[1,5],[7,3],[3,5]]  -> 10
"""

def maximum_wealth(accounts):
    return max(sum(row) for row in accounts)

if __name__ == "__main__":
    print(maximum_wealth([[1,2,3],[3,2,1]]))     # 6
    print(maximum_wealth([[1,5],[7,3],[3,5]]))   # 10
    print(maximum_wealth([[2,8,7],[7,1,3],[1,9,5]]))  # 17
