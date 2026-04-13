"""
Q43: LRU Cache
==============
Problem: Design a data structure that follows the Least Recently Used (LRU) cache.
Implement get(key) and put(key, value) with O(1) average time complexity.

Example:
    LRUCache(2)
    put(1,1), put(2,2), get(1) -> 1
    put(3,3)  # evicts key 2
    get(2)    -> -1
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1); lru.put(2, 2)
    print(lru.get(1))    # 1
    lru.put(3, 3)
    print(lru.get(2))    # -1 (evicted)
    print(lru.get(3))    # 3
