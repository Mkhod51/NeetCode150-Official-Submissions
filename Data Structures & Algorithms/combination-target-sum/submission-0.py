class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path, curSum, target, ind):
            if curSum == target:
                res.append(path)
            
            if curSum >= target:
                return 
            
            for i in range(ind, len(nums)):
                path.append(nums[i])
                dfs(path.copy(), curSum + nums[i], target, i)
                path.pop()
            
        dfs([],0,target,0)

        return res 