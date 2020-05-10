# 1 pass solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxProfit = 0
        for idx, price in enumerate(prices):
            if prices[idx] < minPrice:
                minPrice = prices[idx]
            elif prices[idx] - minPrice > maxProfit:
                maxProfit = prices[idx] - minPrice
        return maxProfit
            