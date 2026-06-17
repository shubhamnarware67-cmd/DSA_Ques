"""
Q311: Tallest Billboard (DP)
==============================
Problem: Install billboard with two supports of equal height.
Each rod can be added to either support or discarded. Max height.

Example:
    [1,2,3,6] -> 6   (put 1+2+3 on one side, 6 on other)
    [1,2,3,4,5,6] -> 10
    [1,2] -> 0
"""

def tallest_billboard(rods):
    # dp[diff] = max height of shorter support with this difference
    dp = {0: 0}
    for r in rods:
        new_dp = dict(dp)
        for diff, short in dp.items():
            tall = short + diff
            # Add rod to taller side
            d1 = diff + r
            new_dp[d1] = max(new_dp.get(d1, 0), short)
            # Add rod to shorter side
            if r <= diff:
                d2 = diff - r
                new_dp[d2] = max(new_dp.get(d2, 0), short + r)
            else:
                d2 = r - diff
                new_dp[d2] = max(new_dp.get(d2, 0), tall)
        dp = new_dp
    return dp.get(0, 0)

if __name__ == "__main__":
    print(tallest_billboard([1,2,3,6]))      # 6
    print(tallest_billboard([1,2,3,4,5,6]))  # 10
    print(tallest_billboard([1,2]))          # 0
