class Solution:
    def climbStairs(self, n: int) -> int:
        

        prev = 1
        cur = 1 

        for i in range(2, n+1):
            tmp = cur 
            cur += prev 
            prev = tmp 
        
        return cur