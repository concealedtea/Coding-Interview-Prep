class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones) - 1):
            stones = sorted(stones)
            stones.append(stones.pop() - stones.pop())
        return stones[0]
            
            