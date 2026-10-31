from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Initialise everything 
        q = deque()
        res = [] 
        
        for i in range(k):
            while q and nums[q[0]] <= nums[i]:
                q.popleft()
            q.appendleft(i)
        
        res.append(nums[q[-1]])
        
        for i in range(k, len(nums)):
            while q and (nums[q[0]] <= nums[i] or q[0] <= i - k):
                q.popleft()
            while q and q[-1] <= i - k:
                q.pop()

            q.appendleft(i)
    
            
            res.append(nums[q[-1]])

        
        return res 
            
