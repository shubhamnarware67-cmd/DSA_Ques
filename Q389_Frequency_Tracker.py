"""
Q389: Frequency Tracker (Design)
==================================
Problem: Design data structure that adds numbers, deletes numbers,
and checks if any number has given frequency — all O(1).

Example:
    add(3), add(3), hasFrequency(2)->True, add(3), hasFrequency(3)->True
    deleteOne(3), hasFrequency(2)->True, hasFrequency(3)->False
"""
from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)       # num -> frequency
        self.freq_count = defaultdict(int) # frequency -> count of nums

    def add(self, number):
        old_freq = self.freq[number]
        if old_freq > 0: self.freq_count[old_freq] -= 1
        self.freq[number] += 1
        self.freq_count[self.freq[number]] += 1

    def deleteOne(self, number):
        if self.freq[number] == 0: return
        old_freq = self.freq[number]
        self.freq_count[old_freq] -= 1
        self.freq[number] -= 1
        if self.freq[number] > 0:
            self.freq_count[self.freq[number]] += 1

    def hasFrequency(self, frequency):
        return self.freq_count[frequency] > 0

if __name__ == "__main__":
    ft = FrequencyTracker()
    ft.add(3); ft.add(3)
    print(ft.hasFrequency(2))  # True
    ft.add(3)
    print(ft.hasFrequency(3))  # True
    ft.deleteOne(3)
    print(ft.hasFrequency(2))  # True
    print(ft.hasFrequency(3))  # False
