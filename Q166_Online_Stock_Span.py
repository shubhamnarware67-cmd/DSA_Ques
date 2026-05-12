"""
Q166: Online Stock Span (Monotonic Stack)
==========================================
Problem: Design class that collects stock prices and returns span —
number of consecutive days (including today) where price <= today's price.

Example:
    prices: 100,80,60,70,60,75,85
    spans:   1,  1, 1, 2, 1, 4,  6
"""

class StockSpanner:
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

if __name__ == "__main__":
    ss = StockSpanner()
    prices = [100,80,60,70,60,75,85]
    print([ss.next(p) for p in prices])  # [1,1,1,2,1,4,6]
