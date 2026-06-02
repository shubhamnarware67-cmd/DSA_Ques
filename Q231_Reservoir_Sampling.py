"""
Q231: Reservoir Sampling
==========================
Problem: Given a stream of unknown length, sample k elements uniformly
at random. Each element has equal probability k/n of being selected.

Example:
    stream = [1,2,3,4,5,6,7,8,9,10], k=3
    -> 3 random elements with equal probability
"""
import random

def reservoir_sample(stream, k):
    reservoir = stream[:k]
    for i in range(k, len(stream)):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir

class StreamSampler:
    """For true streams — processes one element at a time"""
    def __init__(self, k):
        self.k = k
        self.reservoir = []
        self.count = 0

    def process(self, val):
        self.count += 1
        if len(self.reservoir) < self.k:
            self.reservoir.append(val)
        else:
            j = random.randint(0, self.count - 1)
            if j < self.k:
                self.reservoir[j] = val

if __name__ == "__main__":
    stream = list(range(1, 101))
    sample = reservoir_sample(stream, 10)
    print(f"Sample of 10 from 1-100: {sorted(sample)}")

    sampler = StreamSampler(3)
    for val in [10,20,30,40,50]:
        sampler.process(val)
    print(f"Stream sample: {sampler.reservoir}")
