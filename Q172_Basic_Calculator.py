"""
Q172: Basic Calculator (Stack)
================================
Problem: Implement a calculator to evaluate a simple expression string
containing +, -, (, ) and spaces.

Example:
    "1 + 1"           -> 2
    " 2-1 + 2 "       -> 3
    "(1+(4+5+2)-3)+(6+8)" -> 23
"""

def calculate(s):
    stack = []
    result = 0
    number = 0
    sign = 1
    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch == '+':
            result += sign * number
            number = 0; sign = 1
        elif ch == '-':
            result += sign * number
            number = 0; sign = -1
        elif ch == '(':
            stack.append(result)
            stack.append(sign)
            result = 0; sign = 1
        elif ch == ')':
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()
    result += sign * number
    return result

if __name__ == "__main__":
    print(calculate("1 + 1"))               # 2
    print(calculate(" 2-1 + 2 "))           # 3
    print(calculate("(1+(4+5+2)-3)+(6+8)")) # 23
