"""
Q151: Design HashMap from Scratch
===================================
Problem: Implement MyHashMap without built-in hash libraries.
Support: put(key, value), get(key), remove(key).

Example:
    put(1,1), put(2,2), get(1)->1, get(3)->-1
    put(2,1), get(2)->1, remove(2), get(2)->-1
"""

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[h]):
            if k == key:
                self.buckets[h][i] = (key, value)
                return
        self.buckets[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key: return v
        return -1

    def remove(self, key):
        h = self._hash(key)
        self.buckets[h] = [(k, v) for k, v in self.buckets[h] if k != key]

if __name__ == "__main__":
    hm = MyHashMap()
    hm.put(1, 1); hm.put(2, 2)
    print(hm.get(1))   # 1
    print(hm.get(3))   # -1
    hm.put(2, 1)
    print(hm.get(2))   # 1
    hm.remove(2)
    print(hm.get(2))   # -1
