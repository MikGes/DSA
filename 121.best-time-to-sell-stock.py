#just use two pointer and implemet the greedy algorithm.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        p = 0
        while r!=len(prices):
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                p = max(p, prof)
            else:
                l = r
            r+=1
        return p
            