"""
Q175: Minimum Remove to Make Valid Parentheses
================================================
Problem: Given string with '(', ')' and lowercase letters, remove
minimum invalid parentheses to make it valid. Return result string.

Example:
    "lee(t(c)o)de)" -> "lee(t(c)o)de"
    "a)b(c)d"       -> "ab(c)d"
    "))(("           -> ""
"""

def min_remove_to_make_valid(s):
    s = list(s)
    stack = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    for i in stack:
        s[i] = ''
    return ''.join(s)

if __name__ == "__main__":
    print(min_remove_to_make_valid("lee(t(c)o)de)"))  # "lee(t(c)o)de"
    print(min_remove_to_make_valid("a)b(c)d"))         # "ab(c)d"
    print(min_remove_to_make_valid("))(("))             # ""
