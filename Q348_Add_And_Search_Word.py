"""
Q348: Add and Search Word (Trie with Wildcard)
================================================
Problem: Design data structure supporting addWord and search.
search can use '.' as wildcard matching any letter.

Example:
    addWord("bad"), addWord("dad"), addWord("mad")
    search("pad") -> False
    search("bad") -> True
    search(".ad") -> True
    search("b..") -> True
"""

class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word): return node.is_end
            c = word[i]
            if c == '.':
                return any(dfs(child, i+1) for child in node.children.values())
            if c not in node.children: return False
            return dfs(node.children[c], i+1)
        return dfs(self, 0)

if __name__ == "__main__":
    wd = WordDictionary()
    for w in ["bad","dad","mad"]: wd.addWord(w)
    print(wd.search("pad"))  # False
    print(wd.search("bad"))  # True
    print(wd.search(".ad"))  # True
    print(wd.search("b.."))  # True
