#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#
# https://leetcode-cn.com/problems/design-twitter/description/
#
# algorithms
# Medium (41.47%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 39K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
  '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
#
# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：
#
#
# postTweet(userId, tweetId): 创建一条新的推文
# getNewsFeed(userId):
# 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
# follow(followerId, followeeId): 关注一个用户
# unfollow(followerId, followeeId): 取消关注一个用户
#
#
# 示例:
#
#
# Twitter twitter = new Twitter();
#
# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
# twitter.postTweet(1, 5);
#
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# twitter.getNewsFeed(1);
#
# // 用户1关注了用户2.
# twitter.follow(1, 2);
#
# // 用户2发送了一个新推文 (推文id = 6).
# twitter.postTweet(2, 6);
#
# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# twitter.getNewsFeed(1);
#
# // 用户1取消关注了用户2.
# twitter.unfollow(1, 2);
#
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
# twitter.getNewsFeed(1);
#
#
#

# @lc code=start
class Tweet:
    # 定义推文的ID、时间、下一条推文
    def __init__(self, tid: int, time: int) -> None:
        self.tid = tid
        self.time = time
        self.next = None

class User:
    # 定义用户ID、用户关注的人、用户所发的推文列表
    def __init__(self, uid: int):
        self.uid = uid
        self.following = set()
        self.tweetlst = None
        self.follow(uid)

    def post(self, tid: int, time: int) -> None:
        tweet = Tweet(tid, time)
        tweet.next = self.tweetlst
        self.tweetlst = tweet

    def follow(self, uid: int) -> None:
        if uid not in self.following: self.following.add(uid)

    def unfollow(self, uid: int) -> None:
        # one cannot unfollow itself
        if uid != self.uid and uid in self.following: self.following.remove(uid)

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.id2user = {}
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.id2user: self.id2user[userId] = User(userId)
        user = self.id2user[userId]
        user.post(tweetId, self.timestamp)
        self.timestamp += 1

    # 获取用户的following对象的推文，然后堆排序取前10个
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        heap, user = [], self.id2user.get(userId)
        if not user: return []
        for uid in user.following:
            tweets = self.id2user[uid].tweetlst
            while tweets:
                heap.append(tweets)
                tweets = tweets.next
        return [twt.tid for twt in heapq.nlargest(10, heap, key= lambda twt: twt.time)]


    # 定义 followerId 去关注 followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.id2user: self.id2user[followerId] = User(followerId)
        if followeeId not in self.id2user: self.id2user[followeeId] = User(followeeId)
        self.id2user[followerId].follow(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.id2user: self.id2user[followerId].unfollow(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

