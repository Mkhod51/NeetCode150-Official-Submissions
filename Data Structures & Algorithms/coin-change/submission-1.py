class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i] = minimum number of coins to make up i amount 
        #return dp[amount]
        coins.sort()
        dp = [0] + [float("inf")] * (amount)
        print(amount, dp)
        
        for i in range(1, amount + 1):
            for c in coins:
                target = i - c 
                if target < 0:
                    continue 
                    
                dp[i] = min(dp[target] + 1, dp[i])
        
        return dp[amount] if dp[amount] != float("inf") else -1