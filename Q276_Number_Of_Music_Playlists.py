"""
Q276: Number of Music Playlists (DP)
======================================
Problem: Make a playlist of length goal using n songs where every song
played at least once and a song can only be replayed after k other songs.

Example:
    goal=3, n=3, k=1 -> 6
    goal=2, n=2, k=0 -> 2
"""

def num_music_playlists(n, goal, k):
    MOD = 10**9 + 7
    dp = [[0]*(n+1) for _ in range(goal+1)]
    dp[0][0] = 1
    for i in range(1, goal+1):
        for j in range(1, n+1):
            dp[i][j] += dp[i-1][j-1] * (n-j+1)          # Add new song
            dp[i][j] += dp[i-1][j] * max(0, j-k)         # Replay old song
            dp[i][j] %= MOD
    return dp[goal][n]

if __name__ == "__main__":
    print(num_music_playlists(3, 3, 1))  # 6
    print(num_music_playlists(2, 2, 0))  # 2
    print(num_music_playlists(2, 3, 0))  # 6
