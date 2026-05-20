"""
Q193: Word Ladder (BFS - Shortest Transformation)
===================================================
Problem: Given beginWord, endWord, and wordList, return number of words
in shortest transformation sequence. Each step changes one letter.

Example:
    begin="hit", end="cog", wordList=["hot","dot","dog","lot","log","cog"] -> 5
    (hit->hot->dot->dog->cog)
"""
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set: return 0
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    while queue:
        word, length = queue.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word == endWord: return length + 1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, length+1))
    return 0

if __name__ == "__main__":
    print(ladder_length("hit","cog",["hot","dot","dog","lot","log","cog"]))  # 5
    print(ladder_length("hit","cog",["hot","dot","dog","lot","log"]))        # 0
