#Previous answer....but the problem is i couldnt get the right peak! i just used max(arr)
# class Solution(object):
#     def longestMountain(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: int
#         """
#         if len(arr) <3:
#             return 0
#         mi = arr.index(max(arr))
#         l,r = mi -1,mi+1
#         def computeLeft(arr, l):
#             while l > 0:
#                 if arr[l] > arr[l-1]:
#                     l -= 1   
#                 return l
#         def computeRight(arr,r):
#             while r < len(arr):
#                 if arr[r] > arr[r+1]:
#                     r += 1
#                 return r
#         l,r = computeLeft(arr,l),computeRight(arr,r)
#         return len(arr[l:r+1])

        

class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3: return 0
        ret = 0
        for i in range(1, len(arr) - 1):
            if arr[i-1] < arr[i] > arr[i + 1]:
                l=r=i
                while l>0 and arr[l] > arr[l - 1]:
                    l -= 1
                while r < len(arr) - 1 and arr[r] > arr[r+1]:
                     r+=1
                ret = max(ret,r-l+1)
        return ret