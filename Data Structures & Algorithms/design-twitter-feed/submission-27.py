class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(dict)
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
    
       
        self.tweets[userId].append(((self.timestamp*-1),-tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        r = []

        r.extend(self.tweets[userId][-10:])

        for f in self.followers[userId].keys():
            r.extend(self.tweets[f][-10:])
    
        heapq.heapify(r)
        ret = []
        k = 10
        while r and k:
            p = heapq.heappop(r)
            ret.append(-p[1])
            k-=1

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId][followeeId] = 1
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            del self.followers[followerId][followeeId]


# Time:
# __init__: O(1)
# postTweet: O(1) amortized
# getNewsFeed: O(nlogn)
# follow: O(1) average
# unfollow: O(1) average

# Total space: O(N*m + N*M)