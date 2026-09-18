class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = nums[0], nums[0]
        best = nums[0]

        for n in nums[1:]:
            if n == 0:
                curMax, curMin = 1,1
            tmp = curMax
            curMax = max(n * curMax, n*curMin, n)
            curMin = min(n*tmp, n*curMin, n)
            best = max(curMax, best)
        
        return best