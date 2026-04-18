"""
Q77: Largest Rectangle in Histogram (Stack)
=============================================
Problem: Given array of bar heights in histogram, find the area of
the largest rectangle.

Example:
    [2,1,5,6,2,3] -> 10
"""

def largest_rectangle_area(heights):
    stack = []  # Monotonic increasing stack (index)
    max_area = 0
    heights.append(0)  # Sentinel
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area

if __name__ == "__main__":
    print(largest_rectangle_area([2,1,5,6,2,3]))  # 10
    print(largest_rectangle_area([2,4]))           # 4
