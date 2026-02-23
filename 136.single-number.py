# 4 ^ (1 ^ 1) ^ (2 ^ 2) and remember xor is commutative and associative and n ^ 0 = n

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r ^=i
        return r
        