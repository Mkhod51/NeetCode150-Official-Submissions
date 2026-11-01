class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()

        def dfs(path, ind):
            if tuple(path) not in seen:
                res.append(path.copy())
                seen.add(tuple(path))
            
            for i in range(ind, len(nums)):
                path.append(nums[i])
                dfs(path.copy(), i+1)
                path.pop()
        
        dfs([], 0)
        return res