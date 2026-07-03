"""
Q368: Task Assignment (Two Pointers after sorting)
====================================================
Problem: Assign k tasks to k workers. Each worker gets 2 tasks.
Minimize maximum work time. Pair hardest with easiest.

Example:
    k=3, tasks=[1,3,5,3,1,4] -> [[0,2],[4,5],[1,3]]
    indices (0-indexed, sorted tasks): min→max pairs
"""

def task_assignment(k, tasks):
    indexed = sorted(enumerate(tasks), key=lambda x: x[1])
    pairs = []
    for i in range(k):
        pairs.append([indexed[i][0], indexed[2*k-1-i][0]])
    return pairs

def min_max_work(k, tasks):
    tasks_sorted = sorted(tasks)
    return max(tasks_sorted[i] + tasks_sorted[2*k-1-i] for i in range(k))

if __name__ == "__main__":
    print(task_assignment(3, [1,3,5,3,1,4]))  # pairs of indices
    print(min_max_work(3, [1,3,5,3,1,4]))     # 6
