#Descripyion: Okay remember you have the number and their indices in the dictionary....you can use it to constrct the ret array by checking in the dictionary by iterating through them

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = {}
        s = sorted(nums)
        for i,num in enumerate(s):
           if num not in c:
            c[num] = i
        ret = []
        for i in nums:
            ret.append(c[i])
        return ret