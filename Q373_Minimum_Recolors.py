"""
Q373: Minimum Recolors to Get K Consecutive Black Blocks (Sliding Window)
=========================================================================
Problem: String of 'W' (white) and 'B' (black) blocks. Min recolors to
get k consecutive black blocks.

Example:
    "WBBWWBBWBW", k=7 -> 3
    "WBWBBBW",    k=2 -> 0
"""

def minimum_recolors(blocks, k):
    whites = blocks[:k].count('W')
    min_recolors = whites
    for i in range(k, len(blocks)):
        whites += (blocks[i] == 'W') - (blocks[i-k] == 'W')
        min_recolors = min(min_recolors, whites)
    return min_recolors

if __name__ == "__main__":
    print(minimum_recolors("WBBWWBBWBW", 7))  # 3
    print(minimum_recolors("WBWBBBW", 2))      # 0
