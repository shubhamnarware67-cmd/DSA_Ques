"""
Q450: My Calendar III (Sweep Line / Ordered Map)
====================================================
Problem: Book events [start,end). Return max k-booking (max overlap)
after each booking.

Example:
    book(10,20)->1, book(50,60)->1, book(10,40)->2, book(5,15)->3, book(5,10)->3, book(25,55)->3
"""
from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.delta = SortedDict()

    def book(self, start, end):
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1
        active = best = 0
        for v in self.delta.values():
            active += v
            best = max(best, active)
        return best

# Fallback without sortedcontainers
class MyCalendarThreeSimple:
    def __init__(self):
        self.delta = {}

    def book(self, start, end):
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1
        active = best = 0
        for k in sorted(self.delta):
            active += self.delta[k]
            best = max(best, active)
        return best

if __name__ == "__main__":
    cal = MyCalendarThreeSimple()
    print(cal.book(10,20))  # 1
    print(cal.book(50,60))  # 1
    print(cal.book(10,40))  # 2
    print(cal.book(5,15))   # 3
    print(cal.book(5,10))   # 3
    print(cal.book(25,55))  # 3
