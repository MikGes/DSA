#when ever you see missing numbers in array make use of set.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = [i for i in range(1, len(nums)+1)]
        u = set(nums)
        a = []
        for i in n:
            if i not in u:
                a.append(i)
        return a
# The above code finds all numbers that disappeared in an array containing numbers from 1 to n.