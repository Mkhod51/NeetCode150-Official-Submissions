class Twitter:
    class User:
        def __init__(self, userID):
            self.userID = userID
            self.followSet = set([userID])
            self.tweetSet = set()
    

    def __init__(self):
        #Keep track of user profiles create 
        self.userSet = set()

        #userID -> userObj
        self.users = {}

        self.tweetsArray = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        userObj = self.getUser(userId)
        userObj.tweetSet.add(tweetId)
        self.tweetsArray.append(tweetId)


    def getNewsFeed(self, userId: int) -> List[int]:
        userObj = self.getUser(userId)
        allowedSet = set()
        res = []
        for following in userObj.followSet:
            allowedSet = allowedSet | self.users[following].tweetSet 
        
        right = len(self.tweetsArray) - 1
        count = 0
        while right >= 0 and count < 10:
            curTweet = self.tweetsArray[right]
            if curTweet in allowedSet:
                res.append(curTweet)
                count += 1
            right -= 1 

        return res
        
    def getUser(self, userId):
        if userId not in self.userSet:
            userObj = self.User(userId)
            self.userSet.add(userId)
            self.users[userId] = userObj 
        else:
            userObj = self.users[userId]
        
        return userObj

    def follow(self, followerId: int, followeeId: int) -> None:
        userObj = self.getUser(followerId)
        userObj.followSet.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        userObj = self.getUser(followerId)
        userObj.followSet.discard(followeeId)

