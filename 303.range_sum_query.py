# Here is the implementation of the NumArray class that allows for efficient range sum queries using a prefix sum array.
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]
        for num in nums:
            self.dp.append(self.dp[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """ 
        return self.dp[right + 1] - self.dp[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)