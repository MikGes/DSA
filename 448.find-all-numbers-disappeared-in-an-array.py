#when ever you see missing numbers in array make use of set.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        a = []
        t = set(nums) # here i made this to pass the time limit reached error as the original includes duplicates.
        for i in range(1, n+1):
            if i not in t:
             a.append(i)
        return a  
# The above code finds all numbers that disappeared in an array containing numbers from 1 to n.