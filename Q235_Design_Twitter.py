"""
Q235: Design Twitter (OOP + Heap)
===================================
Problem: Design simplified Twitter with:
postTweet(userId, tweetId), getNewsFeed(userId) -> 10 most recent tweets
from user and their followees, follow(u,v), unfollow(u,v).
"""
import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # Decreasing for max-heap behavior

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for user in users:
            if self.tweets[user]:
                t, tid = self.tweets[user][-1]
                heap.append((t, tid, user, len(self.tweets[user])-1))
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            t, tid, user, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                t2, tid2 = self.tweets[user][idx-1]
                heapq.heappush(heap, (t2, tid2, user, idx-1))
        return feed

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)

if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    tw.postTweet(1, 3)
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))  # [6,3,5]
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))  # [3,5]
