"""
Q52: Container With Most Water (Two Pointers)
==============================================
Problem: Given n vertical lines, find two lines that together with
the x-axis form a container that holds the most water.

Example:
    Input:  [1,8,6,2,5,4,8,3,7]
    Output: 49
"""

def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

if __name__ == "__main__":
    print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
    print(max_area([1,1]))                  # 1
