#Description: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#So if the array is sorted, u can use r and l to find the other 2 numbers bu targeting hte number in the for loop.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = sorted(nums)
        a = []
        if s[0] > 0:
            return []
        for i,t in enumerate(s):
            l = i+1
            r = len(s) - 1
            while l < r:
                if t + s[l] + s[r] == 0:
                    if [t,s[l], s[r]] not in a:
                        a.append([t,s[l], s[r]])
                        l += 1
                if t + s[l] + s[r] < 0:
                    l += 1
                else: r -= 1

        return a

        