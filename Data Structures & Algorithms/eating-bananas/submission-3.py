class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkPossible(k):
            total = 0 

            for p in piles:
                needed = math.ceil(p/k)
                total += needed 
                if total > h:
                    return False 
            
            return True 
        
        upper = max(piles)
        lower = 1


        while lower < upper:
            mid = (upper + lower) // 2
            
            if checkPossible(mid): 
                upper = mid
            else:
                lower = mid + 1 
        
        return lower