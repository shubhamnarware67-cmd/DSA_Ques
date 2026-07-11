"""
Q391: Zigzag Iterator (Design)
================================
Problem: Iterate over two lists in zigzag fashion (alternating elements).

Example:
    v1=[1,2], v2=[3,4,5,6]
    next: 1,3,2,4,5,6
"""

class ZigzagIterator:
    def __init__(self, v1, v2):
        self.data = [iter(v) for v in [v1, v2] if v]
        self.idx = 0

    def next(self):
        val = next(self.data[self.idx])
        self.idx = (self.idx + 1) % len(self.data)
        return val

    def hasNext(self):
        # Try each iterator
        n = len(self.data)
        for _ in range(n):
            try:
                val = next(self.data[self.idx])
                # Push back by recreating
                import itertools
                self.data[self.idx] = itertools.chain([val], self.data[self.idx])
                return True
            except StopIteration:
                self.data.pop(self.idx)
                if not self.data: return False
                self.idx %= len(self.data)
        return False

def zigzag_simple(v1, v2):
    """Simple generator approach"""
    i1, i2 = iter(v1), iter(v2)
    done1 = done2 = False
    while not (done1 and done2):
        if not done1:
            try: yield next(i1)
            except StopIteration: done1 = True
        if not done2:
            try: yield next(i2)
            except StopIteration: done2 = True

if __name__ == "__main__":
    print(list(zigzag_simple([1,2], [3,4,5,6])))  # [1,3,2,4,5,6]
    print(list(zigzag_simple([1], [3,4,5,6])))    # [1,3,4,5,6]
