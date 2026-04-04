"""
Q4: Valid Parentheses
=====================
Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Example:
    Input: s = "()[]{}"
    Output: True
    Input: s = "(]"
    Output: False
"""

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

if __name__ == "__main__":
    print(is_valid("()[]{}"))   # True
    print(is_valid("(]"))       # False
    print(is_valid("([)]"))     # False
    print(is_valid("{[]}"))     # True
