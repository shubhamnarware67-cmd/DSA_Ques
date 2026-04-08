"""
Q36: Count Primes (Sieve of Eratosthenes)
==========================================
Problem: Count the number of prime numbers less than n.

Example:
    Input: n = 10
    Output: 4  (2, 3, 5, 7)
"""

def count_primes(n):
    if n < 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return sum(sieve)

if __name__ == "__main__":
    print(count_primes(10))   # 4
    print(count_primes(100))  # 25
    print(count_primes(0))    # 0
