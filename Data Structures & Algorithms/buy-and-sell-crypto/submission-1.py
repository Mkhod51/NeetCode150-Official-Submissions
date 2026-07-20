class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        maxi = 0
        low = prices[0]


        for p in prices:
            low = min(low,p)
            maxi = max(maxi, p-low)
        
        return maxi


