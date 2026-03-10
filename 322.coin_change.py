# The coin change problem can be solved using dynamic programming. The idea is to create an array `dp` where `dp[i]` represents the minimum number of coins needed to make up the amount `i`. We initialize the array with a value greater than the maximum possible (amount + 1) and set `dp[0]` to 0 since no coins are needed to make up the amount of 0. We then iterate through each amount from 1 to the target amount and for each coin, we check if it can be used to make up the current amount. If it can, we update our `dp` array with the minimum number of coins needed.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] *(amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if (i - c) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if (dp[amount] !=amount + 1) else -1