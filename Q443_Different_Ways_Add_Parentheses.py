"""
Q443: Different Ways to Add Parentheses (Divide and Conquer)
================================================================
Problem: Given expression with +,-,*, return all results from all
possible ways to group numbers and operators.

Example:
    "2-1-1" -> [0,2]
    "2*3-4*5" -> [-34,-14,-10,-10,10]
"""
from functools import lru_cache

def diff_ways_to_compute(expression):
    @lru_cache(None)
    def compute(expr):
        if expr.isdigit():
            return [int(expr)]
        results = []
        for i, c in enumerate(expr):
            if c in '+-*':
                left = compute(expr[:i])
                right = compute(expr[i+1:])
                for l in left:
                    for r in right:
                        if c == '+': results.append(l+r)
                        elif c == '-': results.append(l-r)
                        else: results.append(l*r)
        return results
    return compute(expression)

if __name__ == "__main__":
    print(sorted(diff_ways_to_compute("2-1-1")))      # [0,2]
    print(sorted(diff_ways_to_compute("2*3-4*5")))    # [-34,-14,-10,-10,10]
