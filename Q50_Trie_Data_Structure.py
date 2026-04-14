"""
Q50: Trie (Prefix Tree)
=======================
Problem: Implement a Trie with insert, search, and startsWith methods.
Used for autocomplete, spell checking, IP routing, etc.

Example:
    insert("apple")
    search("apple")    -> True
    search("app")      -> False
    startsWith("app")  -> True
    insert("app")
    search("app")      -> True
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))      # True
    print(trie.search("app"))        # False
    print(trie.starts_with("app"))   # True
    trie.insert("app")
    print(trie.search("app"))        # True
