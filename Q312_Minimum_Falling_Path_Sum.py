"""
Q312: Minimum Falling Path Sum II (Non-adjacent columns)
=========================================================
Problem: Falling path in matrix where each step can go to any column
EXCEPT the same column as the previous row. Find minimum sum path.

Example:
    [[1,2,3],[4,5,6],[7,8,9]] -> 13
    [[7]] -> 7
"""

def min_falling_path_sum_ii(grid):
    n = len(grid)
    prev = grid[0][:]
    for r in range(1, n):
        # Find 1st and 2nd minimums of prev row
        sorted_prev = sorted(range(n), key=lambda c: prev[c])
        min1_idx, min2_idx = sorted_prev[0], sorted_prev[1]
        curr = []
        for c in range(n):
            best_prev = prev[min1_idx] if c != min1_idx else prev[min2_idx]
            curr.append(grid[r][c] + best_prev)
        prev = curr
    return min(prev)

if __name__ == "__main__":
    print(min_falling_path_sum_ii([[1,2,3],[4,5,6],[7,8,9]]))  # 13
    print(min_falling_path_sum_ii([[7]]))                        # 7
    print(min_falling_path_sum_ii([[-73,61,43,-48,-36],
           [3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]))  # -192
