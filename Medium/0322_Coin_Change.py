# Bottom down DP solution
# Uses O(N+C) where N is amount and C is number of different coins
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = [float('inf')] * (amount + 1)
        cache[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    cache[i] = min(cache[i-coin]+1, cache[i])
        if cache[amount] == float('inf'): return -1
        return cache[amount]
        