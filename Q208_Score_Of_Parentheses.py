"""
Q208: Score of Parentheses (Stack)
=====================================
Problem: "()" = 1 point, "AB" = A+B points, "(A)" = 2*A points.
Given balanced parentheses string, compute the score.

Example:
    "()"     -> 1
    "(())"   -> 2
    "()()"   -> 2
    "(()(()))" -> 6
"""

def score_of_parentheses(s):
    stack = [0]
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2*v, 1)
    return stack[0]

if __name__ == "__main__":
    print(score_of_parentheses("()"))        # 1
    print(score_of_parentheses("(())"))      # 2
    print(score_of_parentheses("()()"))      # 2
    print(score_of_parentheses("(()(()))"))  # 6
