import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        start = [(-nums[i], i) for i in range(l,r + 1)]
        heapq.heapify(start)
        ret = []

        while r < len(nums):
            heapq.heappush(start, (-nums[r], r))
            while (start[0][1]) < l:
                heapq.heappop(start)
            
            ret.append(-start[0][0])

            
            r += 1 
            l += 1

        return ret

        
        
            