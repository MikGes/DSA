# Here is a Python implementation of the solution to the "Maximum Subarray" problem using dynamic programming. The idea is to create a dp array where dp[i] represents the maximum subarray sum that ends at index i. We iterate through the input array and fill the dp array based on the relation: dp[i] = max(nums[i], dp[i-1] + nums[i]). Finally, we return the maximum value in the dp array, which will be the maximum subarray sum.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        for i, v in enumerate(nums):
          dp[i] = max(v, dp[i-1] + v)
        return max(dp)  
        