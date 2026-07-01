"""
Q358: Minimum Adjacent Swaps to Make Valid Parentheses String
=============================================================
Problem: Given parentheses string, find minimum adjacent swaps to
make it valid. Unmatched ')' must be moved past unmatched '('.

Example:
    "]]][[["   -> 3  (each ] must swap to match a [)
    Actually uses '(' and ')': "))(()" -> 2
"""

def min_swaps_make_valid(s):
    result = 0
    balance = 0
    for c in s:
        if c == '(': balance += 1
        else:
            if balance > 0: balance -= 1
            else: result += 1  # Unmatched ')'
    return result

def min_swaps_brackets(s):
    # For '[' and ']'
    result = 0
    balance = 0
    for c in s:
        if c == '[': balance += 1
        elif c == ']':
            if balance > 0: balance -= 1
            else: result += 1
    return result

if __name__ == "__main__":
    print(min_swaps_make_valid("))(("))  # 2
    print(min_swaps_make_valid(")("))    # 1
    print(min_swaps_brackets("]]][[["))  # 3
