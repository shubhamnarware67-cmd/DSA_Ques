"""
Q170: Evaluate Reverse Polish Notation (Stack)
================================================
Problem: Evaluate the value of an arithmetic expression in RPN.
Valid operators: +, -, *, /. Division truncates toward zero.

Example:
    ["2","1","+","3","*"] -> 9   ((2+1)*3)
    ["4","13","5","/","+"] -> 6  (4+(13/5))
"""

def eval_rpn(tokens):
    stack = []
    ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
           '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    return stack[0]

if __name__ == "__main__":
    print(eval_rpn(["2","1","+","3","*"]))        # 9
    print(eval_rpn(["4","13","5","/","+"]))        # 6
    print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22
