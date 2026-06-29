"""
Q350: Snapshot Array (Binary Search + Versioning)
===================================================
Problem: Array supporting set(index,val), snap() returns snap_id,
get(index, snap_id) returns value at that snapshot.

Example:
    SnapshotArray(3)
    set(0,5), snap() -> 0, set(0,6), get(0,0) -> 5
"""
import bisect

class SnapshotArray:
    def __init__(self, length):
        self.snap_id = 0
        self.data = [[[0, 0]] for _ in range(length)]

    def set(self, index, val):
        if self.data[index][-1][0] == self.snap_id:
            self.data[index][-1][1] = val
        else:
            self.data[index].append([self.snap_id, val])

    def snap(self):
        sid = self.snap_id
        self.snap_id += 1
        return sid

    def get(self, index, snap_id):
        arr = self.data[index]
        # Binary search for largest snap_id <= target
        pos = bisect.bisect_right(arr, [snap_id, float('inf')]) - 1
        return arr[pos][1]

if __name__ == "__main__":
    sa = SnapshotArray(3)
    sa.set(0, 5)
    print(sa.snap())       # 0
    sa.set(0, 6)
    print(sa.get(0, 0))    # 5
    print(sa.get(0, 1))    # 6 (after snap 0, value changed to 6)
