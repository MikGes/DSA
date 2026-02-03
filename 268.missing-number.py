#Description: Given an array nums containing n distinct numbers in the range [0, n], return the only number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return sum(i for i in range(0,n+1)) - sum(nums)