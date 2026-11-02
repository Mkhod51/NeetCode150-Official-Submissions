class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = 1 
        curMax = 1 
        best = max(nums)

        for n in nums:
            if n < 0:
                curMin, curMax = curMax, curMin 
            
            curMax = max(n, curMax * n)
            curMin = min(n, curMin * n)
            best = max(best, curMax)
        
        return best 