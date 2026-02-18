#here use dictionary but i can use the sliding window concept which is commendted out beneath
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <=k:
                return True
            d[v] = i
        return False 
    
    # seen = set()
    # for i, num in enumerate(num):
    #     if i in seen:
    #         return True
    #     seen.add(num)
    #     if len(seen) > k:
    #         seen.remove(nums[i - k])
    #     return False