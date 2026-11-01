class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path, seen):
            if len(path) == len(nums):
                res.append(path)
                return 
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue 
                
                seen.add(nums[i])
                path.append(nums[i])

                dfs(path.copy(), seen.copy())
            
                seen.remove(nums[i])
                path.pop()
            
        
        dfs([], set())
        return res 