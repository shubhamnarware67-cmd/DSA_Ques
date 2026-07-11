"""
Q393: Implement Rand10() Using Rand7() (Rejection Sampling)
============================================================
Problem: Given rand7() which generates uniform [1,7], implement rand10() 
generating uniform [1,10].

Key insight: rand7() * 7 + rand7() gives uniform [1,49], take [1,40].
"""
import random

def rand7():
    return random.randint(1, 7)

def rand10():
    while True:
        row = rand7()
        col = rand7()
        idx = (row - 1) * 7 + col  # Uniform [1,49]
        if idx <= 40:
            return 1 + (idx - 1) % 10

def test_distribution(n=100000):
    from collections import Counter
    results = Counter(rand10() for _ in range(n))
    print("Distribution (should be ~10% each):")
    for k in sorted(results):
        print(f"  {k}: {results[k]/n*100:.1f}%")

if __name__ == "__main__":
    samples = [rand10() for _ in range(20)]
    print("Sample values:", samples)
    print("All in [1,10]:", all(1 <= v <= 10 for v in samples))
    test_distribution()
