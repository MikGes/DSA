#Here make sure to sort out the array
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        md = float('inf')
        for i in range(1, len(arr)):
            md = min(md,arr[i] - arr[i-1])
        a = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == md:
                a.append([arr[i-1], arr[i]])
        return a