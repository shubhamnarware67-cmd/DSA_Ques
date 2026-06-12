"""
Q288: Maximum XOR of Two Numbers in an Array (Trie)
====================================================
Problem: Given integer array, return maximum XOR of any two numbers.

Example:
    [3,10,5,25,2,8] -> 28  (5 XOR 25 = 28)
    [0]              -> 0
"""

class TrieNode:
    def __init__(self):
        self.children = [None, None]

def find_maximum_xor(nums):
    root = TrieNode()
    for num in nums:
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    max_xor = 0
    for num in nums:
        node = root
        curr_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit
            if node.children[want]:
                curr_xor = (curr_xor << 1) | 1
                node = node.children[want]
            else:
                curr_xor = curr_xor << 1
                node = node.children[bit]
        max_xor = max(max_xor, curr_xor)
    return max_xor

if __name__ == "__main__":
    print(find_maximum_xor([3,10,5,25,2,8]))  # 28
    print(find_maximum_xor([14,70,53,83,49,91,36,80,92,51,66,70]))  # 127
