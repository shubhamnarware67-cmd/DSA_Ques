"""
Q289: Design Search Autocomplete System (Trie + Priority Queue)
================================================================
Problem: Autocomplete with history. input(c) returns top 3 hot sentences
by frequency (ties: ASCII order). '#' signals end of sentence.

Example:
    sentences=["i love you","island","ironman","i love leetcode"]
    times=[5,3,2,2], input sequence: 'i',' ','#'
"""
import heapq
from collections import defaultdict

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.freq = defaultdict(int)
        for s, t in zip(sentences, times):
            self.freq[s] = t
        self.current = ""

    def input(self, c):
        if c == '#':
            self.freq[self.current] += 1
            self.current = ""
            return []
        self.current += c
        results = []
        for sentence, count in self.freq.items():
            if sentence.startswith(self.current):
                heapq.heappush(results, (-count, sentence))
        return [heapq.heappop(results)[1] for _ in range(min(3, len(results)))]

if __name__ == "__main__":
    acs = AutocompleteSystem(["i love you","island","ironman","i love leetcode"],[5,3,2,2])
    print(acs.input('i'))   # ["i love you","island","i love leetcode"]
    print(acs.input(' '))   # ["i love you","i love leetcode"]
    print(acs.input('#'))   # []
    print(acs.input('i'))   # ["i love you","island","i love leetcode"]
