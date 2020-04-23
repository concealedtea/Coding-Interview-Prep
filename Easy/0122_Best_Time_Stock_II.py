class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        totalProfit = 0
        for idx, val in enumerate(prices):
            if idx >= 1:
                if val > prices[idx - 1]: totalProfit += val - prices[idx-1]
        return totalProfit
                