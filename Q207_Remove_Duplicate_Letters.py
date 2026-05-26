"""
Q207: Remove Duplicate Letters (Greedy + Stack)
================================================
Problem: Given string, remove duplicate letters so that each letter
appears once. Result must be smallest lexicographically.

Example:
    "bcabc" -> "abc"
    "cbacdcbc" -> "acdb"
"""

def remove_duplicate_letters(s):
    last_idx = {c: i for i, c in enumerate(s)}
    stack = []
    in_stack = set()
    for i, c in enumerate(s):
        if c not in in_stack:
            while stack and stack[-1] > c and last_idx[stack[-1]] > i:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)
    return ''.join(stack)

if __name__ == "__main__":
    print(remove_duplicate_letters("bcabc"))     # "abc"
    print(remove_duplicate_letters("cbacdcbc"))  # "acdb"
