"""
Q150: Design HashSet from Scratch
====================================
Problem: Implement MyHashSet without using built-in hash table libraries.
Support: add(key), remove(key), contains(key).
"""

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key):
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key):
        h = self._hash(key)
        return key in self.buckets[h]

if __name__ == "__main__":
    hs = MyHashSet()
    hs.add(1); hs.add(2)
    print(hs.contains(1))  # True
    print(hs.contains(3))  # False
    hs.add(2)
    print(hs.contains(2))  # True
    hs.remove(2)
    print(hs.contains(2))  # False
