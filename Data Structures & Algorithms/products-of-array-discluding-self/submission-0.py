class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixList = [0 for _ in range(n)]
        suffixList = [0 for _ in range(n)]

        prefix = 1
        for i in range(n):
            prefixList[i] = prefix 
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            suffixList[i] = suffix 
            suffix *= nums[i]
        
        return [ x * y for x,y in zip(prefixList, suffixList)]

