"""
Q200: Maximal Rectangle in Binary Matrix
==========================================
Problem: Given binary matrix, find largest rectangle containing only 1s.
Extends histogram approach (Q77) to 2D.

Example:
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]
    Output: 6
"""

def maximal_rectangle(matrix):
    if not matrix or not matrix[0]: return 0
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0
    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        max_area = max(max_area, largest_in_histogram(heights))
    return max_area

def largest_in_histogram(heights):
    stack = []
    max_area = 0
    heights = heights + [0]
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
              ["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximal_rectangle(matrix))  # 6
    print(maximal_rectangle([["0"]]))  # 0
