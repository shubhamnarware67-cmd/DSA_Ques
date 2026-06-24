"""
Q318: Minimum Cost Tree From Leaf Values (Monotonic Stack)
===========================================================
Problem: Build binary tree from array (leaves in inorder). Non-leaf nodes
have value = product of max leaves in each subtree. Minimize sum of non-leaf values.

Example:
    [6,2,4]    -> 32  (6*4 + 2*4 = 24+8=32)
    [4,11]     -> 44
"""

def mct_from_leaf_values(arr):
    stack = [float('inf')]
    result = 0
    for num in arr:
        while stack[-1] <= num:
            mid = stack.pop()
            result += mid * min(stack[-1], num)
        stack.append(num)
    while len(stack) > 2:
        result += stack.pop() * stack[-1]
    return result

if __name__ == "__main__":
    print(mct_from_leaf_values([6,2,4]))  # 32
    print(mct_from_leaf_values([4,11]))   # 44
    print(mct_from_leaf_values([15,13,5,3,15]))  # 232? Let's verify
