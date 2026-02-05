#Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Approch: Use a hash map to store the indices of the numbers as you iterate through the list. For each number, check if the complement (target - current number) exists in the hash map.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i,num in enumerate(nums):
            d = target - num
            if d in h:
                return i, h[target - num]
            h[num] = i