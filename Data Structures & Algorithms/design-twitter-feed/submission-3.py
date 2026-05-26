from collections import deque
class Twitter:

    def __init__(self):
        ## userFollowList{}: key = id, value = Set(ids), set would be o(1) and indepotent
        ## Option #1
        ## userTweets{}: key = userid, value = [(tweetIds, timestamp)] just append to end for new tweets,
        ## postTweet O(1), getNewsFeed: O(10m), where m is the follower list
        ## Option #2
        ## tweets: [], append to the end of the list, 
        ## postTweet O(1), getNewsFeed: O(n), n is number of posts

        self.userFollowList = defaultdict(set)
        self.userTweets = defaultdict(deque)
        self.postNumber = 0

    ## O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].appendleft((tweetId, self.postNumber))
        self.postNumber += 1
    

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        res = []
        seenTweets = set()

        recentTweets = []
        heapq.heapify(recentTweets)
        usersToCheck = self.userFollowList[userId]
        for u in usersToCheck:
            if u in self.userTweets:
                postNumber = -self.userTweets[u][0][1]
                tweetId = self.userTweets[u][0][0]
                heapq.heappush(recentTweets, (postNumber, tweetId, u, 0))
                seenTweets.add(tweetId)

        while recentTweets and len(res) < 10:
            discard, tweetId, uid, index = heapq.heappop(recentTweets)
            res.append(tweetId)

            if index + 1 < len(self.userTweets[uid]):
                newTweetId = self.userTweets[uid][index + 1][0]
                newPostNumber = self.userTweets[uid][index + 1][1]
                heapq.heappush(recentTweets, (-newPostNumber, newTweetId, uid, index + 1))
        
        self.unfollow(userId, userId)
        return res

        


    ## O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowList[followerId].add(followeeId)

    ## O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowList[followerId]:
            self.userFollowList[followerId].remove(followeeId)


