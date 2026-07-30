
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ub = max(piles)
        lb = 1
        
        
        def checkRun(piles, h, n):
            hours = 0
            for p in piles:
                hours += math.ceil(p / n)
            
            return hours <= h




        print(lb, ub)
        left = lb
        right = ub
        curMin = ub
        while right > left:
            mid = int(left + (right - left) / 2)

            if checkRun(piles, h, mid):
                right = mid 
                curMin = min(curMin, mid)
            else:
                left = mid + 1
        
        return curMin
            
            
            
            