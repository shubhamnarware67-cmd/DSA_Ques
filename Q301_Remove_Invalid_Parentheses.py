"""
Q301: Remove Invalid Parentheses (BFS)
========================================
Problem: Remove minimum number of invalid parentheses to make the input
string valid. Return all possible results.

Example:
    "()())()" -> ["()()()", "(())()"]
    "(a)())()" -> ["(a)()()", "(a())()"]
    ")("       -> [""]
"""
from collections import deque

def remove_invalid_parentheses(s):
    def is_valid(string):
        count = 0
        for c in string:
            if c == '(': count += 1
            elif c == ')':
                count -= 1
                if count < 0: return False
        return count == 0

    visited = {s}
    queue = deque([s])
    result = []
    found = False

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            curr = queue.popleft()
            if is_valid(curr):
                result.append(curr)
                found = True
            if not found:
                for i in range(len(curr)):
                    if curr[i] not in '()': continue
                    nxt = curr[:i] + curr[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        if found:
            break
    return result

if __name__ == "__main__":
    print(remove_invalid_parentheses("()())()"))   # ["()()()", "(())()"]
    print(remove_invalid_parentheses(")("))         # [""]
