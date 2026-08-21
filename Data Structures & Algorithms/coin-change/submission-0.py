class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0: # this coin is a possible way to build the this amount
                    # the number of ways is the current min or another amount + 1 (this coin)
                    dp[i] = min(dp[i], 1 + dp[i-c])
                    
        # if it is impossible (e.g. [2], 3), 3 - 2 = 1, but dp[1] = amount +1
        # so dp[3] = min(amount + 1, 1 + amount + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
            
