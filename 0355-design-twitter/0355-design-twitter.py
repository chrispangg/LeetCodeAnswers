class Twitter:

    def __init__(self):
        self.tweets = [] #[time, id, userId]
        heapify(self.tweets)
        self.time = 0
        self.following = defaultdict(list) #[userId,[followeeId]]

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(self.tweets, tuple([self.time, tweetId, userId]))
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        
        copyTweets = self.tweets.copy()
        while len(res) < 10 and copyTweets:
            time, tweetId, uId = heappop(copyTweets)
        
            if uId in self.following[userId] or uId == userId:
                res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)