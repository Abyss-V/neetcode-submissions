class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(list)
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
    
       
        heapq.heappush(self.tweets[userId],((self.timestamp*-1),-tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        r = []
        heapq.heapify(r)
      
        for t in self.tweets[userId]:
            heapq.heappush(r,t)
        for f in self.followers[userId]:
            r = r + self.tweets[f]
    
        heapq.heapify(r)
        ret = []
  
        while r:
            p = heapq.heappop(r)
            ret.append(-p[1])

        return ret[:10] if len(ret) > 10 else ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for i,u in enumerate(self.followers[followerId]):
            if u == followeeId:
                self.followers[followerId].pop(i)
                break
