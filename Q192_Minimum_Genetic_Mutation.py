"""
Q192: Minimum Genetic Mutation (BFS)
======================================
Problem: Gene string mutation from start to end, change one char at a time.
Each intermediate must be in gene bank. Return min mutations or -1.

Example:
    start="AACCGGTT", end="AACCGGTA", bank=["AACCGGTA"] -> 1
    start="AACCGGTT", end="AAACGGTA", bank=["AACCGGTA","AACCGCTA","AAACGGTA"] -> 2
"""
from collections import deque

def min_mutation(start, end, bank):
    bank_set = set(bank)
    if end not in bank_set: return -1
    queue = deque([(start, 0)])
    visited = {start}
    genes = 'ACGT'
    while queue:
        curr, steps = queue.popleft()
        if curr == end: return steps
        for i in range(len(curr)):
            for g in genes:
                if g != curr[i]:
                    next_gene = curr[:i] + g + curr[i+1:]
                    if next_gene in bank_set and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, steps+1))
    return -1

if __name__ == "__main__":
    print(min_mutation("AACCGGTT","AACCGGTA",["AACCGGTA"]))  # 1
    print(min_mutation("AACCGGTT","AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]))  # 2
