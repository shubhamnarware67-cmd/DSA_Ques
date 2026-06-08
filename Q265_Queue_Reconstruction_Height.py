"""
Q265: Queue Reconstruction by Height (Greedy)
===============================================
Problem: people[i]=[h,k] where h=height, k=people in front with h>=height.
Reconstruct the queue.

Example:
    [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    -> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
"""

def reconstruct_queue(people):
    # Sort: taller first; same height -> smaller k first
    people.sort(key=lambda x: (-x[0], x[1]))
    result = []
    for p in people:
        result.insert(p[1], p)
    return result

if __name__ == "__main__":
    p = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(reconstruct_queue(p))
    # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
