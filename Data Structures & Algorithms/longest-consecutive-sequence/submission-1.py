class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        starts = set()

        if not nums:
            return 0

        for n in hs:
            if (n-1) not in hs:
                starts.add(n)
        
        max = 1

        for n in starts:
            streak = 1
             
            while (n+1) in hs:
                streak += 1 
                n = n+1
            
            if max < streak:
                max = streak 
        
        return max 
            
                
