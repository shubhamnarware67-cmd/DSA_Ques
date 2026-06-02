"""
Q234: Design Iterator for Flattening Nested List
==================================================
Problem: Design an iterator that flattens a nested list of integers.
Implement hasNext() and next().

Example:
    [[1,1],2,[1,1]] -> 1,1,2,1,1
    [1,[4,[6]]]     -> 1,4,6
"""

class NestedIterator:
    def __init__(self, nested_list):
        self.flat = []
        self._flatten(nested_list)
        self.index = 0

    def _flatten(self, lst):
        for item in lst:
            if isinstance(item, list):
                self._flatten(item)
            else:
                self.flat.append(item)

    def next(self):
        val = self.flat[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.flat)

if __name__ == "__main__":
    it = NestedIterator([[1,1],2,[1,1]])
    while it.hasNext():
        print(it.next(), end=' ')  # 1 1 2 1 1
    print()
    it2 = NestedIterator([1,[4,[6]]])
    while it2.hasNext():
        print(it2.next(), end=' ')  # 1 4 6
    print()
