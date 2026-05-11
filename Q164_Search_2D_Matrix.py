"""
Q164: Search a 2D Matrix
=========================
Problem: Given m x n matrix where each row is sorted and first element
of each row > last element of previous row. Search for target. O(log(mn)).

Example:
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> True
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13 -> False
"""

def search_matrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target: return True
        elif val < target: left = mid + 1
        else: right = mid - 1
    return False

if __name__ == "__main__":
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(search_matrix(m, 3))   # True
    print(search_matrix(m, 13))  # False
