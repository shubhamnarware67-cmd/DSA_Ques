"""
Q404: Number of Smooth Descent Periods of a Stock (Math)
=========================================================
Problem: Count number of smooth descent periods where prices decrease
by exactly 1 each day. Single day also counts.

Example:
    [3,2,1,4] -> 7
    [8,6,7,7] -> 4
    [1]        -> 1
"""

def get_descent_periods(prices):
    result = 1
    length = 1
    for i in range(1, len(prices)):
        if prices[i] == prices[i-1] - 1:
            length += 1
        else:
            length = 1
        result += length
    return result

if __name__ == "__main__":
    print(get_descent_periods([3,2,1,4]))  # 7
    print(get_descent_periods([8,6,7,7]))  # 4
    print(get_descent_periods([1]))         # 1
