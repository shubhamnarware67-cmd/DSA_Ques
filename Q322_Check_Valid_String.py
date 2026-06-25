"""
Q322: Valid Parenthesis String (Greedy)
=========================================
Problem: '*' can be '(', ')' or empty. Check if string is valid.

Example:
    "()"    -> True
    "(*)"   -> True
    "(*))"  -> True
    "(((*)" -> False
"""

def check_valid_string(s):
    # Track range of possible open-paren counts
    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1; hi += 1
        elif c == ')':
            lo = max(lo-1, 0); hi -= 1
        else:  # '*'
            lo = max(lo-1, 0); hi += 1
        if hi < 0: return False
    return lo == 0

if __name__ == "__main__":
    print(check_valid_string("()"))     # True
    print(check_valid_string("(*)"))    # True
    print(check_valid_string("(*))"))   # True
    print(check_valid_string("(((*)" )) # False
