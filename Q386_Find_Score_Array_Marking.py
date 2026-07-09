"""
Q386: Find Score of Array After Marking All Elements (Heap)
============================================================
Problem: Repeatedly pick smallest unmarked element, add to score,
mark it and its neighbors. Return total score.

Example:
    [2,1,3,4,5,2] -> 7   (pick 1→mark 0,1,2; pick 2→mark 5; score=1+2=3? 
     Actually: mark 1 at idx1→mark 0,1,2; pick next smallest unmarked=2(idx5)→mark 4,5; 
     pick 4(idx3)→mark 3,4; score=1+2+4=7) ✓
    [2,3,5,1,3,2] -> 5
"""
import heapq

def find_score(nums):
    n = len(nums)
    heap = sorted((v, i) for i, v in enumerate(nums))
    marked = [False] * n
    score = 0
    for v, i in heap:
        if marked[i]: continue
        score += v
        marked[i] = True
        if i > 0:   marked[i-1] = True
        if i < n-1: marked[i+1] = True
    return score

if __name__ == "__main__":
    print(find_score([2,1,3,4,5,2]))  # 7
    print(find_score([2,3,5,1,3,2]))  # 5
