#Here we combine the concepts of sliding window and the left and right pointer concepts
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        res = float('inf')
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
        if res == float('inf'):return 0
        else:
            return res
            