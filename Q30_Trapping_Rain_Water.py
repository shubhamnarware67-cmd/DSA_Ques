"""
Q30: Trapping Rain Water
========================
Problem: Given n non-negative integers representing elevation heights,
compute how much water it can trap after raining.

Example:
    Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""

def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))              # 9
