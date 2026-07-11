"""
Q392: Peeking Iterator (Design)
=================================
Problem: Extend Iterator class with peek() that returns next value
without advancing, and hasNext().

Example:
    iter([1,2,3]), peek()->1, next()->1, next()->2, peek()->3, next()->3
"""

class Iterator:
    def __init__(self, nums):
        self._nums = iter(nums)
        self._next = None
        self._has = True
        self._advance()

    def _advance(self):
        try: self._next = next(self._nums)
        except StopIteration: self._has = False; self._next = None

    def hasNext(self): return self._has

    def next(self):
        val = self._next; self._advance(); return val

class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self._peeked = None
        self._has_peeked = False

    def peek(self):
        if not self._has_peeked:
            self._peeked = self.it.next()
            self._has_peeked = True
        return self._peeked

    def next(self):
        if self._has_peeked:
            val = self._peeked; self._has_peeked = False; return val
        return self.it.next()

    def hasNext(self):
        return self._has_peeked or self.it.hasNext()

if __name__ == "__main__":
    pi = PeekingIterator(Iterator([1,2,3]))
    print(pi.peek())    # 1
    print(pi.next())    # 1
    print(pi.next())    # 2
    print(pi.peek())    # 3
    print(pi.hasNext()) # True
    print(pi.next())    # 3
    print(pi.hasNext()) # False
