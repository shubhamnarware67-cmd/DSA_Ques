"""
Q245: Aho-Corasick Algorithm (Multi-Pattern Search)
=====================================================
Problem: Search for multiple patterns simultaneously in O(n + m + k)
where n=text length, m=total pattern length, k=occurrences found.

Example:
    patterns=["he","she","his","hers"]
    text="ushers"
    -> he at 1, she at 1, hers at 2
"""
from collections import defaultdict, deque

class AhoCorasick:
    def __init__(self):
        self.goto = [defaultdict(int)]
        self.fail = [0]
        self.output = [[]]
        self.size = 1

    def add_pattern(self, pattern, idx):
        curr = 0
        for ch in pattern:
            if ch not in self.goto[curr]:
                self.goto.append(defaultdict(int))
                self.fail.append(0)
                self.output.append([])
                self.goto[curr][ch] = self.size
                self.size += 1
            curr = self.goto[curr][ch]
        self.output[curr].append(idx)

    def build(self):
        queue = deque()
        for ch, s in self.goto[0].items():
            queue.append(s)
        while queue:
            r = queue.popleft()
            for ch, s in self.goto[r].items():
                queue.append(s)
                state = self.fail[r]
                while state and ch not in self.goto[state]:
                    state = self.fail[state]
                self.fail[s] = self.goto[state].get(ch, 0)
                if self.fail[s] == s: self.fail[s] = 0
                self.output[s] += self.output[self.fail[s]]

    def search(self, text, patterns):
        results = []
        curr = 0
        for i, ch in enumerate(text):
            while curr and ch not in self.goto[curr]:
                curr = self.fail[curr]
            curr = self.goto[curr].get(ch, 0)
            for idx in self.output[curr]:
                start = i - len(patterns[idx]) + 1
                results.append((start, patterns[idx]))
        return results

if __name__ == "__main__":
    patterns = ["he","she","his","hers"]
    ac = AhoCorasick()
    for i, p in enumerate(patterns): ac.add_pattern(p, i)
    ac.build()
    print(ac.search("ushers", patterns))  # [(1,'he'),(1,'she'),(2,'hers')]
