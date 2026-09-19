"""
Q442: Basic Calculator III (Full Expression: +,-,*,/,())
============================================================
Problem: Evaluate expression string with +,-,*,/,(),spaces. No leading zeros
issue, integer division truncates toward zero.

Example:
    "1+1"        -> 2
    "6-4/2"      -> 4
    "2*(5+5*2)/3+(6/2+8)" -> 21
"""

def calculate(s):
    def helper(it):
        stack = []
        num = 0
        sign = '+'
        while True:
            c = next(it, None)
            if c is not None and c.isdigit():
                num = num*10 + int(c)
            if c == '(':
                num = helper(it)
            if c is None or c in '+-*/)':
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                elif sign == '*': stack.append(stack.pop()*num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev/num))
                num = 0
                if c is not None: sign = c
                if c is None or c == ')':
                    return sum(stack)

    s = s.replace(' ', '')
    return helper(iter(s))

if __name__ == "__main__":
    print(calculate("1+1"))                       # 2
    print(calculate("6-4/2"))                     # 4
    print(calculate("2*(5+5*2)/3+(6/2+8)"))       # 21
