"""
Q441: Parse Lisp Expression (Recursive Parsing)
==================================================
Problem: Evaluate Lisp-like expression with let, add, mult.

Example:
    "(add 1 2)" -> 3
    "(mult 3 (add 2 3))" -> 15
    "(let x 2 (mult x (let x 3 y 4 (add x y))))" -> 14
"""

def evaluate(expression):
    def parse(expr, scope):
        if expr[0] != '(':
            if expr[0].isdigit() or expr[0] == '-':
                return int(expr)
            return lookup(expr, scope)
        # Remove outer parens
        inner = expr[1:-1]
        tokens = tokenize(inner)
        if tokens[0] == 'add':
            return parse(tokens[1], scope) + parse(tokens[2], scope)
        elif tokens[0] == 'mult':
            return parse(tokens[1], scope) * parse(tokens[2], scope)
        elif tokens[0] == 'let':
            new_scope = dict(scope)
            i = 1
            while i < len(tokens) - 2:
                new_scope[tokens[i]] = parse(tokens[i+1], new_scope)
                i += 2
            return parse(tokens[-1], new_scope)

    def lookup(var, scope):
        return scope[var]

    def tokenize(s):
        tokens = []
        i = 0
        depth = 0
        start = 0
        while i < len(s):
            if s[i] == '(': depth += 1
            elif s[i] == ')': depth -= 1
            elif s[i] == ' ' and depth == 0:
                tokens.append(s[start:i])
                start = i + 1
            i += 1
        tokens.append(s[start:])
        return tokens

    return parse(expression, {})

if __name__ == "__main__":
    print(evaluate("(add 1 2)"))                                    # 3
    print(evaluate("(mult 3 (add 2 3))"))                           # 15
    print(evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))   # 14
