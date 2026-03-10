# here is a dynamic programming solution to the climbing stairs problem. The idea is to use an array `dp` where `dp[i]` represents the number of ways to climb `i` stairs. The base cases are defined for 0, 1, and 2 stairs, and then we fill the array iteratively using the relation that the number of ways to climb `i` stairs is the sum of the ways to climb `i-1` and `i-2` stairs.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        if n == 1: return 1
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]